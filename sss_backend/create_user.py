#!/usr/bin/env python
"""
Script simple para crear un usuario de prueba
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sss_backend.settings')

try:
    django.setup()
    
    from django.contrib.auth.models import User
    
    print("🚀 CREANDO USUARIO DE PRUEBA")
    print("=" * 40)
    
    # Datos del usuario de prueba
    username = "admin"
    email = "admin@sss.com"
    password = "admin123"
    first_name = "Administrador"
    last_name = "SSS"
    
    # Verificar si el usuario ya existe
    if User.objects.filter(username=username).exists():
        print(f"❌ El usuario '{username}' ya existe")
        print("💡 Puedes usar las credenciales existentes o cambiar el username")
    else:
        # Crear superusuario
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        print(f"✅ Usuario creado exitosamente:")
        print(f"   Username: {user.username}")
        print(f"   Email: {user.email}")
        print(f"   Contraseña: {password}")
        print(f"   Superusuario: {'✅' if user.is_superuser else '❌'}")
        print(f"   Activo: {'✅' if user.is_active else '❌'}")
        print()
        print("🔗 Ahora puedes:")
        print("   1. Ir a http://localhost:8000/admin/ para el panel de administración")
        print("   2. Ir a http://localhost:8000/ para el login del sistema")
        print(f"   3. Usar las credenciales: {username} / {password}")
    
    # Mostrar usuarios existentes
    print("\n👥 USUARIOS EXISTENTES:")
    print("-" * 30)
    users = User.objects.all()
    for user in users:
        print(f"• {user.username} ({user.email}) - {'Superuser' if user.is_superuser else 'Usuario normal'}")

except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Asegúrate de que Django esté configurado correctamente")
    print("💡 Verifica que la base de datos esté funcionando")
