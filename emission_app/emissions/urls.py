from django.urls import path
from . import views
urlpatterns = [
    path('update_database/', views.update_database),
    path('population_json/', views.population_json),
    path('emission_json/', views.emission_json),
    path('country_population/<slug:country_code>', views.country_population_json),
]
