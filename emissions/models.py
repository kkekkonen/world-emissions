from django.db import models

class Country_population(models.Model):
	Country_Name = models.CharField(max_length=30)
	Country_Code = models.CharField(max_length=5)
	Indicator_Name = models.CharField(max_length=50)
	Indicator_Code = models.CharField(max_length=51)
	population_values = models.TextField()

class Country_emissions(models.Model):
	Country_Name = models.CharField(max_length=31)
	Country_Code = models.CharField(max_length=4)
	Indicator_Name = models.CharField(max_length=52)
	Indicator_Code = models.CharField(max_length=53)
	emission_values = models.TextField()
