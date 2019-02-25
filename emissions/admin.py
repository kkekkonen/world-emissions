from django.contrib import admin
from .models import Country_population, Country_emissions
# Register your models here.

admin.site.register(Country_population)
admin.site.register(Country_emissions)
