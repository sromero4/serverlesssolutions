#!/usr/bin/env python
"""
Script de prueba para la autenticación del sistema SSS
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sss_backend.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password

def test_password_encoding():
    """Probar la codificación de contraseñas"""
    print("🔐 PRUEBA DE CODIFICACIÓN DE CONTRASEÑAS")
    print("=" * 50)
    
    # Crear una contraseña de prueba
    password = "test123"
    
    # Codificar la contraseña
    hashed_password = make_password(password)
    print(f"Contraseña original: {password}")
    print(f"Contraseña codificada: {hashed_password}")
    print(f"Algoritmo usado: {hashed_password.split('$')[0]}")
    
    # Verificar la contraseña
    is_valid = check_password(password, hashed_password)
    print(f"Verificación: {'✅ Válida' if is_valid else '❌ Inválida'}")
    print()

def test_user_authentication():
    """Probar la autenticación de usuarios"""
    print("👤 PRUEBA DE AUTENTICACIÓN DE USUARIOS")
    print("=" * 50)
    
    # Listar usuarios existentes
    users = User.objects.all()
    print(f"Usuarios en la base de datos: {users.count()}")
    
    for user in users:
        print(f"- Username: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Activo: {'✅' if user.is_active else '❌'}")
        print(f"  Staff: {'✅' if user.is_staff else '❌'}")
        print(f"  Superuser: {'✅' if user.is_superuser else '❌'}")
        print()
    
    # Probar autenticación
    if users.exists():
        test_user = users.first()
        print(f"Probando autenticación con usuario: {test_user.username}")
        
        # Probar con contraseña correcta (si es admin)
        if test_user.is_superuser:
            print("⚠️  Este es un superusuario. Necesitas la contraseña real.")
        else:
            # Probar con contraseña por defecto
            test_password = "password123"
            user = authenticate(username=test_user.username, password=test_password)
            if user:
                print(f"✅ Autenticación exitosa con contraseña: {test_password}")
            else:
                print(f"❌ Autenticación fallida con contraseña: {test_password}")
    else:
        print("❌ No hay usuarios en la base de datos")
        print("💡 Crea un superusuario con: python manage.py createsuperuser")

def create_test_user():
    """Crear un usuario de prueba"""
    print("👤 CREANDO USUARIO DE PRUEBA")
    print("=" * 50)
    
    username = "testuser"
    password = "test123"
    email = "test@example.com"
    
    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        print(f"❌ El usuario '{username}' ya existe")
        return
    
    # Crear usuario
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name="Test",
        last_name="User"
    )
    
    print(f"✅ Usuario creado exitosamente:")
    print(f"   Username: {user.username}")
    print(f"   Email: {user.email}")
    print(f"   Contraseña: {password}")
    print(f"   Activo: {'✅' if user.is_active else '❌'}")
    
    # Probar autenticación
    auth_user = authenticate(username=username, password=password)
    if auth_user:
        print(f"✅ Autenticación exitosa")
    else:
        print(f"❌ Error en la autenticación")

def show_database_info():
    """Mostrar información de la base de datos"""
    print("🗄️  INFORMACIÓN DE LA BASE DE DATOS")
    print("=" * 50)
    
    from django.conf import settings
    
    db_config = settings.DATABASES['default']
    print(f"Motor: {db_config['ENGINE']}")
    print(f"Nombre: {db_config['NAME']}")
    print(f"Host: {db_config['HOST']}")
    print(f"Puerto: {db_config['PORT']}")
    print(f"Usuario: {db_config['USER']}")
    print()

if __name__ == "__main__":
    print("🚀 SISTEMA DE PRUEBA DE AUTENTICACIÓN SSS")
    print("=" * 60)
    print()
    
    try:
        show_database_info()
        test_password_encoding()
        test_user_authentication()
        
        # Preguntar si crear usuario de prueba
        print("¿Deseas crear un usuario de prueba? (y/n): ", end="")
        response = input().lower().strip()
        
        if response in ['y', 'yes', 's', 'si']:
            create_test_user()
        
        print("\n✅ Pruebas completadas")
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        print("💡 Asegúrate de que Django esté configurado correctamente")
