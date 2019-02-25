# Generated by Django 2.1.5 on 2019-02-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissions', '0003_auto_20190210_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country_emissions',
            name='Country_Code',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Country_Name',
            field=models.CharField(max_length=31),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Indicator_Code',
            field=models.CharField(max_length=53),
        ),
        migrations.AlterField(
            model_name='country_emissions',
            name='Indicator_Name',
            field=models.CharField(max_length=52),
        ),
        migrations.AlterField(
            model_name='country_population',
            name='Country_Code',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='country_population',
            name='Indicator_Code',
            field=models.CharField(max_length=51),
        ),
        migrations.AlterField(
            model_name='country_population',
            name='Indicator_Name',
            field=models.CharField(max_length=50),
        ),
    ]