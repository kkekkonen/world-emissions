from django.db import models

class Country_population(models.Model):
	Country_Name = models.CharField(max_length=60)
	Country_Code = models.CharField(max_length=5)
	Indicator_Name = models.CharField(max_length=60)
	Indicator_Code = models.CharField(max_length=60)
	population_values = models.TextField()

class Country_emissions(models.Model):
	Country_Name = models.CharField(max_length=60)
	Country_Code = models.CharField(max_length=5)
	Indicator_Name = models.CharField(max_length=60)
	Indicator_Code = models.CharField(max_length=60)
	emission_values = models.TextField()
