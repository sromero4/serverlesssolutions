from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('project-selection/', views.project_selection_view, name='project_selection'),
    
    # Restaurant Dashboard
    path('restaurant/', views.restaurant_dashboard_view, name='restaurant_dashboard'),
    
    # Restaurant - Usuarios
    path('restaurant/users/', views.restaurant_users_view, name='restaurant_users'),
    path('restaurant/users/add/', views.restaurant_add_user_view, name='restaurant_add_user'),
    path('restaurant/users/edit/<int:user_id>/', views.restaurant_edit_user_view, name='restaurant_edit_user'),
    path('restaurant/users/delete/<int:user_id>/', views.restaurant_delete_user_view, name='restaurant_delete_user'),
    
    # Restaurant - Pedidos
    path('restaurant/pedidos/', views.restaurant_pedidos_view, name='restaurant_pedidos'),
    path('restaurant/pedidos/add/', views.restaurant_add_pedido_view, name='restaurant_add_pedido'),
    
    # Restaurant - Productos
    path('restaurant/productos/', views.restaurant_productos_view, name='restaurant_productos'),
    path('restaurant/productos/add/', views.restaurant_add_producto_view, name='restaurant_add_producto'),
    
    # Restaurant - Ingredientes
    path('restaurant/ingredientes/', views.restaurant_ingredientes_view, name='restaurant_ingredientes'),
    path('restaurant/ingredientes/add/', views.restaurant_add_ingrediente_view, name='restaurant_add_ingrediente'),
    
    # Restaurant - Inventario
    path('restaurant/inventario/', views.restaurant_inventario_view, name='restaurant_inventario'),
    path('restaurant/inventario/add/', views.restaurant_add_inventario_view, name='restaurant_add_inventario'),
    
    # Restaurant - Jornadas
    path('restaurant/jornadas/', views.restaurant_jornadas_view, name='restaurant_jornadas'),
    path('restaurant/jornadas/add/', views.restaurant_add_jornada_view, name='restaurant_add_jornada'),
    
    # Conjunto Dashboard
    path('conjunto/', views.conjunto_dashboard_view, name='conjunto_dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/login/', views.login_api, name='login_api'),
]
