from django.urls import path, include
from . import views

app_name = 'mapas'

urlpatterns = [
    path('', views.panel_principal, name="panel_principal"),
]
