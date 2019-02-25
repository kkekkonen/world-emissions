from django.urls import path
from . import views
urlpatterns = [
    path('update_emissions/', views.update_emissions),
    path('update_population/', views.update_population),
    path('population_json/', views.population_json),
    path('emission_json/', views.emission_json),
    path('country_population/<slug:country_code>', views.country_population_json),
]
