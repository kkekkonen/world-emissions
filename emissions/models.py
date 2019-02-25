from django.db import models

class Country_population(models.Model):
	Country_Name = models.CharField(max_length=50)
	Country_Code = models.CharField(max_length=5)
	Indicator_Name = models.CharField(max_length=50)
	Indicator_Code = models.CharField(max_length=50)
	population_values = models.TextField()

class Country_emissions(models.Model):
	Country_Name = models.CharField(max_length=50)
	Country_Code = models.CharField(max_length=5)
	Indicator_Name = models.CharField(max_length=50)
	Indicator_Code = models.CharField(max_length=50)
	emission_values = models.TextField()
