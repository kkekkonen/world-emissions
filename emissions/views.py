from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login as auth_login, authenticate as auth_authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.urls import reverse
from .models import Country_emissions, Country_population
import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import json

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

default_headers = ['Country_Name', 'Country_Code', 'Indicator_Name','Indicator_Code']

def import_population():
    #this function imports the emission csv and creates a population model for each country.
    resp = urlopen('http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv')
    zipfile = ZipFile(BytesIO(resp.read()))
    for filename in zipfile.namelist():
        if filename.startswith('API'):
            df = pd.read_csv(zipfile.open(filename), skiprows=4)
            df = df.replace({pd.np.nan: None})
            for index, row in df.iterrows():
                country_dict = {}
                number_dict = {}
                for header_spaced in df.columns.values:
                    header = header_spaced.replace(' ', '_')
                    if is_number(header):
                        if row[header_spaced]:
                            number_dict[header] = row[header_spaced]
                    elif header in default_headers:
                        country_dict[header] = row[header_spaced]
                    else:
                        pass
                country_dict['population_values'] = json.dumps(number_dict)
                country_population = Country_population(**country_dict)
                country_population.save()

def import_emissions():
    #this function imports the emission csv and creates a emission model for each country.
    resp = urlopen('http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv')
    zipfile = ZipFile(BytesIO(resp.read()))
    for filename in zipfile.namelist():
        if filename.startswith('API'):
            df = pd.read_csv(zipfile.open(filename), skiprows=4)
            df = df.replace({pd.np.nan: None})
            for index, row in df.iterrows():
                country_dict = {}
                number_dict = {}
                for header_spaced in df.columns.values:
                    header = header_spaced.replace(' ', '_')
                    if is_number(header):
                        if row[header_spaced]:
                            number_dict[header] = row[header_spaced]
                    elif header in default_headers:
                        country_dict[header] = row[header_spaced]
                    else:
                        pass
                country_dict['emission_values'] = json.dumps(number_dict)
                country_emissions = Country_emissions(**country_dict)
                country_emissions.save()

def emission_json(request):
    if request.method == 'GET':
        emissions = Country_emissions.objects.all()
        response = [{
             'name': r.Country_Name,
             'Country_Code': r.Country_Code,
             'Indicator_Name': r.Indicator_Name,
             'Indicator_Code': r.Indicator_Code,
             'data': json.loads(r.emission_values),
        } for r in emissions]
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse(status=405)

def population_json(request):
    if request.method == 'GET':
        population = Country_population.objects.all()
        response = [{
             'Country_Name': r.Country_Name,
             'Country_Code': r.Country_Code,
             'Indicator_Name': r.Indicator_Name,
             'Indicator_Code': r.Indicator_Code,
             'data': json.loads(r.population_values),
        } for r in population]
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse(status=405)

def country_population_json(request, country_code):
    if request.method == 'GET':
        population = Country_population.objects.get(Country_Code=country_code)
        response = {
             'Country_Name': population.Country_Name,
             'Country_Code': population.Country_Code,
             'Indicator_Name': population.Indicator_Name,
             'Indicator_Code': population.Indicator_Code,
             'data': json.loads(population.population_values),
        }
        return JsonResponse(response, safe=False)
    else:
        return HttpResponse(status=405)

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = auth_authenticate(request, username=username, password=raw_password)
        if user is not None:
            auth_login(request, user)
            return redirect(reverse('admin_tools'))
        else:
            return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login', )

@user_passes_test(lambda u: u.is_superuser)
def admin_tools(request):
    message = None
    if request.method == "POST":
        if 'population' in request.POST:
            try:
                Country_population.objects.all().delete()
                import_population()
                message = 'population import successful'
            except Exception as e:
                message = 'population import failed'
        elif 'emissions' in request.POST:
            try:
                Country_emissions.objects.all().delete()
                import_emissions()
                message = 'emission import successful'
            except Exception as e:
                message = 'emission import failed'
        context = {'message': message}
        return render(request, 'admin_tools.html', context)
    else:
        return render(request, 'admin_tools.html')
