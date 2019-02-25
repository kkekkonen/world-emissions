from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
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

@user_passes_test(lambda u: u.is_superuser)
def update_emissions(request):
    try:
        Country_emissions.objects.all().delete()
        import_emissions()
        return HttpResponse("import completed", status=200)
    except Exception as e:
        return HttpResponse(e, status=400)

@user_passes_test(lambda u: u.is_superuser)
def update_population(request):
    try:
        Country_population.objects.all().delete()
        import_population()
        return HttpResponse("import completed", status=200)
    except Exception as e:
        return HttpResponse(e, status=400)

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
