from django.db import models

class Country_population(models.Model):
	Country_Name = models.CharField(max_length=30)
	Country_Code = models.CharField(max_length=3)
	Indicator_Name = models.CharField(max_length=30)
	Indicator_Code = models.CharField(max_length=30)
	population_values = models.TextField()

class Country_emissions(models.Model):
	Country_Name = models.CharField(max_length=30)
	Country_Code = models.CharField(max_length=3)
	Indicator_Name = models.CharField(max_length=30)
	Indicator_Code = models.CharField(max_length=30)
	emission_values = models.TextField()
