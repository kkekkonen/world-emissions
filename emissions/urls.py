from django.urls import path
from . import views
urlpatterns = [
    path('admin_tools/', views.admin_tools, name='admin_tools'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login/', views.login, name='login'),
    path('population_json/', views.population_json),
    path('emission_json/', views.emission_json),
    path('country_population/<slug:country_code>', views.country_population_json),
]
