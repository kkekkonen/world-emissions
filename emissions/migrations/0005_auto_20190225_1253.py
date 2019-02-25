# Generated by Django 2.1.5 on 2019-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0004_auto_20190225_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_emissions',
            name='Country_Code',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Country_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Indicator_Code',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Indicator_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='country_population',
            name='Country_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='country_population',
            name='Indicator_Code',
            field=models.CharField(max_length=50),
        ),
    ]
