from django.urls import path
from .views import *

urlpatterns = [
    path('registrar_ingrediente/', CrearIngrediente.as_view(), name="registrar_ingrediente"),
    path('listar_ingredientes/', ListarIngrediente.as_view(), name="listar_ingrediente"),
    path('editar_ingrediente/<int:pk>/', EditarIngrediente.as_view(), name="editar_ingrediente"),
    path('eliminar_ingrediente/', eliminar_ingrediente, name="eliminar_ingrediente"),
]