from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.db import connections


def login_view(request):
    """
    Vista de login con diseño moderno
    """
    if request.user.is_authenticated:
        return redirect('auth:project_selection')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f'¡Bienvenido, {user.first_name or user.username}!')
                    return redirect('auth:project_selection')
                else:
                    messages.error(request, 'Tu cuenta está desactivada. Contacta al administrador.')
            else:
                # Verificar si el usuario existe para dar un mensaje más específico
                from django.contrib.auth.models import User
                try:
                    user_exists = User.objects.get(username=username)
                    messages.error(request, 'Contraseña incorrecta. Por favor, verifica tu contraseña.')
                except User.DoesNotExist:
                    messages.error(request, 'Usuario no encontrado. Por favor, verifica tu nombre de usuario.')
        else:
            messages.error(request, 'Por favor, completa todos los campos.')
    
    return render(request, 'auth/login.html')


def logout_view(request):
    """
    Vista de logout
    """
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('auth:login')


def project_selection_view(request):
    """
    Vista de selección de proyecto
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    return render(request, 'auth/project_selection.html', {
        'user': request.user
    })


def restaurant_dashboard_view(request):
    """
    Dashboard específico para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener estadísticas del proyecto Restaurant
    restaurant_stats = get_restaurant_stats()
    
    return render(request, 'auth/restaurant_dashboard.html', {
        'user': request.user,
        'stats': restaurant_stats,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def conjunto_dashboard_view(request):
    """
    Dashboard específico para el proyecto Conjunto
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener estadísticas del proyecto Conjunto
    conjunto_stats = get_conjunto_stats()
    
    return render(request, 'auth/conjunto_dashboard.html', {
        'user': request.user,
        'stats': conjunto_stats,
        'project_name': 'Conjunto',
        'project_icon': 'fas fa-building'
    })


def dashboard_view(request):
    """
    Vista del dashboard general (redirige a selección de proyecto)
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    return redirect('auth:project_selection')


def get_restaurant_stats():
    """
    Obtener estadísticas del proyecto Restaurant
    """
    try:
        # Usar la conexión específica del proyecto restaurant
        with connections['cholaoscaleno'].cursor() as cursor:
            # Contar pedidos
            cursor.execute("SELECT COUNT(*) FROM pedido")
            total_pedidos = cursor.fetchone()[0]
            
            # Contar productos
            cursor.execute("SELECT COUNT(*) FROM producto")
            total_productos = cursor.fetchone()[0]
            
            # Contar ingredientes
            cursor.execute("SELECT COUNT(*) FROM ingrediente")
            total_ingredientes = cursor.fetchone()[0]
            
            # Contar inventarios
            cursor.execute("SELECT COUNT(*) FROM inventario")
            total_inventarios = cursor.fetchone()[0]
            
            # Pedidos del día
            cursor.execute("SELECT COUNT(*) FROM pedido WHERE DATE(ped_fechacreacion) = CURRENT_DATE")
            pedidos_hoy = cursor.fetchone()[0]
            
            return {
                'total_pedidos': total_pedidos,
                'total_productos': total_productos,
                'total_ingredientes': total_ingredientes,
                'total_inventarios': total_inventarios,
                'pedidos_hoy': pedidos_hoy
            }
    except Exception as e:
        # En caso de error, retornar datos de ejemplo
        return {
            'total_pedidos': 0,
            'total_productos': 0,
            'total_ingredientes': 0,
            'total_inventarios': 0,
            'pedidos_hoy': 0
        }


def get_conjunto_stats():
    """
    Obtener estadísticas del proyecto Conjunto
    """
    try:
        # Usar la conexión específica del proyecto conjunto
        with connections['napoli'].cursor() as cursor:
            # Contar apartamentos
            cursor.execute("SELECT COUNT(*) FROM apartamento")
            total_apartamentos = cursor.fetchone()[0]
            
            # Contar torres
            cursor.execute("SELECT COUNT(*) FROM torre")
            total_torres = cursor.fetchone()[0]
            
            # Contar habitantes
            cursor.execute("SELECT COUNT(*) FROM habitante")
            total_habitantes = cursor.fetchone()[0]
            
            # Contar propietarios
            cursor.execute("SELECT COUNT(*) FROM propietario")
            total_propietarios = cursor.fetchone()[0]
            
            # Contar personas
            cursor.execute("SELECT COUNT(*) FROM persona")
            total_personas = cursor.fetchone()[0]
            
            return {
                'total_apartamentos': total_apartamentos,
                'total_torres': total_torres,
                'total_habitantes': total_habitantes,
                'total_propietarios': total_propietarios,
                'total_personas': total_personas
            }
    except Exception as e:
        # En caso de error, retornar datos de ejemplo
        return {
            'total_apartamentos': 0,
            'total_torres': 0,
            'total_habitantes': 0,
            'total_propietarios': 0,
            'total_personas': 0
        }


def restaurant_users_view(request):
    """
    Vista de gestión de usuarios para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener usuarios del proyecto Restaurant
    restaurant_users = get_restaurant_users()
    
    return render(request, 'auth/restaurant_users.html', {
        'user': request.user,
        'users': restaurant_users,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_user_view(request):
    """
    Vista para agregar nuevo usuario al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        is_staff = request.POST.get('is_staff') == 'on'
        
        if username and email and password:
            try:
                # Crear usuario en la base de datos principal
                from django.contrib.auth.models import User
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    is_staff=is_staff
                )
                
                messages.success(request, f'Usuario "{username}" creado exitosamente.')
                return redirect('auth:restaurant_users')
                
            except Exception as e:
                messages.error(request, f'Error al crear usuario: {str(e)}')
        else:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
    
    return render(request, 'auth/restaurant_add_user.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_edit_user_view(request, user_id):
    """
    Vista para editar usuario del proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    try:
        from django.contrib.auth.models import User
        user_to_edit = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
        return redirect('auth:restaurant_users')
    
    if request.method == 'POST':
        user_to_edit.username = request.POST.get('username')
        user_to_edit.email = request.POST.get('email')
        user_to_edit.first_name = request.POST.get('first_name')
        user_to_edit.last_name = request.POST.get('last_name')
        user_to_edit.is_staff = request.POST.get('is_staff') == 'on'
        user_to_edit.is_active = request.POST.get('is_active') == 'on'
        
        # Cambiar contraseña si se proporciona
        new_password = request.POST.get('password')
        if new_password:
            user_to_edit.set_password(new_password)
        
        try:
            user_to_edit.save()
            messages.success(request, f'Usuario "{user_to_edit.username}" actualizado exitosamente.')
            return redirect('auth:restaurant_users')
        except Exception as e:
            messages.error(request, f'Error al actualizar usuario: {str(e)}')
    
    return render(request, 'auth/restaurant_edit_user.html', {
        'user': request.user,
        'user_to_edit': user_to_edit,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_delete_user_view(request, user_id):
    """
    Vista para eliminar usuario del proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    try:
        from django.contrib.auth.models import User
        user_to_delete = User.objects.get(id=user_id)
        
        # No permitir eliminar el usuario actual
        if user_to_delete.id == request.user.id:
            messages.error(request, 'No puedes eliminar tu propio usuario.')
            return redirect('auth:restaurant_users')
        
        username = user_to_delete.username
        user_to_delete.delete()
        messages.success(request, f'Usuario "{username}" eliminado exitosamente.')
        
    except User.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
    except Exception as e:
        messages.error(request, f'Error al eliminar usuario: {str(e)}')
    
    return redirect('auth:restaurant_users')


def get_restaurant_users():
    """
    Obtener lista de usuarios del proyecto Restaurant
    """
    try:
        from django.contrib.auth.models import User
        users = User.objects.all().order_by('-date_joined')
        return users
    except Exception as e:
        return []


# ===== MÓDULO DE PEDIDOS =====
def restaurant_pedidos_view(request):
    """
    Vista de gestión de pedidos para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener pedidos del proyecto Restaurant
    pedidos = get_restaurant_pedidos()
    
    return render(request, 'auth/restaurant_pedidos.html', {
        'user': request.user,
        'pedidos': pedidos,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_pedido_view(request):
    """
    Vista para agregar nuevo pedido al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        mesa = request.POST.get('mesa')
        tipo = request.POST.get('tipo')
        subtotal = request.POST.get('subtotal', 0)
        propina = request.POST.get('propina', 0)
        total = request.POST.get('total', 0)
        adicional = request.POST.get('adicional')
        metodo_pago = request.POST.get('metodo_pago')
        
        if mesa and tipo and total:
            try:
                # Crear pedido en la base de datos
                with connections['cholaoscaleno'].cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO pedido (ped_mesa, ped_tipo, ped_subtotal, ped_propina, ped_total, 
                                          ped_adicional, ped_metodopago, ped_fechacreacion, usu_codigo, jor_codigo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), %s, %s)
                    """, [mesa, tipo, subtotal, propina, total, adicional, metodo_pago, request.user.id, 1])
                
                messages.success(request, f'Pedido de mesa {mesa} creado exitosamente.')
                return redirect('auth:restaurant_pedidos')
                
            except Exception as e:
                messages.error(request, f'Error al crear pedido: {str(e)}')
        else:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
    
    return render(request, 'auth/restaurant_add_pedido.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def get_restaurant_pedidos():
    """
    Obtener lista de pedidos del proyecto Restaurant
    """
    try:
        with connections['cholaoscaleno'].cursor() as cursor:
            cursor.execute("""
                SELECT p.*, u.username, j.jor_iniciofechahora
                FROM pedido p
                LEFT JOIN auth_user u ON p.usu_codigo = u.id
                LEFT JOIN jornada j ON p.jor_codigo = j.jor_codigo
                ORDER BY p.ped_fechacreacion DESC
                LIMIT 50
            """)
            columns = [col[0] for col in cursor.description]
            pedidos = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return pedidos
    except Exception as e:
        return []


# ===== MÓDULO DE PRODUCTOS =====
def restaurant_productos_view(request):
    """
    Vista de gestión de productos para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener productos del proyecto Restaurant
    productos = get_restaurant_productos()
    
    return render(request, 'auth/restaurant_productos.html', {
        'user': request.user,
        'productos': productos,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_producto_view(request):
    """
    Vista para agregar nuevo producto al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')
        
        if nombre and precio:
            try:
                # Crear producto en la base de datos
                with connections['cholaoscaleno'].cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO producto (prod_nombre, prod_descripcion, prod_precio, prod_imagen, 
                                           prod_fechacreacion, est_codigo, usu_codigo)
                        VALUES (%s, %s, %s, %s, NOW(), %s, %s)
                    """, [nombre, descripcion, precio, imagen, 1, request.user.id])
                
                messages.success(request, f'Producto "{nombre}" creado exitosamente.')
                return redirect('auth:restaurant_productos')
                
            except Exception as e:
                messages.error(request, f'Error al crear producto: {str(e)}')
        else:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
    
    return render(request, 'auth/restaurant_add_producto.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def get_restaurant_productos():
    """
    Obtener lista de productos del proyecto Restaurant
    """
    try:
        with connections['cholaoscaleno'].cursor() as cursor:
            cursor.execute("""
                SELECT p.*, u.username, e.est_nombre
                FROM producto p
                LEFT JOIN auth_user u ON p.usu_codigo = u.id
                LEFT JOIN estado e ON p.est_codigo = e.est_codigo
                ORDER BY p.prod_fechacreacion DESC
                LIMIT 50
            """)
            columns = [col[0] for col in cursor.description]
            productos = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return productos
    except Exception as e:
        return []


# ===== MÓDULO DE INGREDIENTES =====
def restaurant_ingredientes_view(request):
    """
    Vista de gestión de ingredientes para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener ingredientes del proyecto Restaurant
    ingredientes = get_restaurant_ingredientes()
    
    return render(request, 'auth/restaurant_ingredientes.html', {
        'user': request.user,
        'ingredientes': ingredientes,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_ingrediente_view(request):
    """
    Vista para agregar nuevo ingrediente al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        tipo_producto = request.POST.get('tipo_producto', 1)
        tipo_cantidad = request.POST.get('tipo_cantidad', 1)
        
        if nombre and cantidad:
            try:
                # Crear ingrediente en la base de datos
                with connections['cholaoscaleno'].cursor() as cursor:
                    cursor.execute("""
                        INSERT INTO ingrediente (ing_nombre, ing_cantidad, ing_fechacreacion, 
                                              usu_codigo, tipprod_codigo, tipcant_codigo)
                        VALUES (%s, %s, NOW(), %s, %s, %s)
                    """, [nombre, cantidad, request.user.id, tipo_producto, tipo_cantidad])
                
                messages.success(request, f'Ingrediente "{nombre}" creado exitosamente.')
                return redirect('auth:restaurant_ingredientes')
                
            except Exception as e:
                messages.error(request, f'Error al crear ingrediente: {str(e)}')
        else:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
    
    return render(request, 'auth/restaurant_add_ingrediente.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def get_restaurant_ingredientes():
    """
    Obtener lista de ingredientes del proyecto Restaurant
    """
    try:
        with connections['cholaoscaleno'].cursor() as cursor:
            cursor.execute("""
                SELECT i.*, u.username, tp.tipprod_nombre, tc.tipcant_nombre
                FROM ingrediente i
                LEFT JOIN auth_user u ON i.usu_codigo = u.id
                LEFT JOIN tipoproducto tp ON i.tipprod_codigo = tp.tipprod_codigo
                LEFT JOIN tipocantidad tc ON i.tipcant_codigo = tc.tipcant_codigo
                ORDER BY i.ing_fechacreacion DESC
                LIMIT 50
            """)
            columns = [col[0] for col in cursor.description]
            ingredientes = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return ingredientes
    except Exception as e:
        return []


# ===== MÓDULO DE INVENTARIO =====
def restaurant_inventario_view(request):
    """
    Vista de gestión de inventario para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener inventarios del proyecto Restaurant
    inventarios = get_restaurant_inventarios()
    
    return render(request, 'auth/restaurant_inventario.html', {
        'user': request.user,
        'inventarios': inventarios,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_inventario_view(request):
    """
    Vista para agregar nuevo inventario al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        try:
            # Crear inventario en la base de datos
            with connections['cholaoscaleno'].cursor() as cursor:
                cursor.execute("""
                    INSERT INTO inventario (inv_fechahora, usu_codigo)
                    VALUES (NOW(), %s)
                """, [request.user.id])
            
            messages.success(request, 'Inventario creado exitosamente.')
            return redirect('auth:restaurant_inventario')
            
        except Exception as e:
            messages.error(request, f'Error al crear inventario: {str(e)}')
    
    return render(request, 'auth/restaurant_add_inventario.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def get_restaurant_inventarios():
    """
    Obtener lista de inventarios del proyecto Restaurant
    """
    try:
        with connections['cholaoscaleno'].cursor() as cursor:
            cursor.execute("""
                SELECT i.*, u.username
                FROM inventario i
                LEFT JOIN auth_user u ON i.usu_codigo = u.id
                ORDER BY i.inv_fechahora DESC
                LIMIT 50
            """)
            columns = [col[0] for col in cursor.description]
            inventarios = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return inventarios
    except Exception as e:
        return []


# ===== MÓDULO DE JORNADAS =====
def restaurant_jornadas_view(request):
    """
    Vista de gestión de jornadas para el proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    # Obtener jornadas del proyecto Restaurant
    jornadas = get_restaurant_jornadas()
    
    return render(request, 'auth/restaurant_jornadas.html', {
        'user': request.user,
        'jornadas': jornadas,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def restaurant_add_jornada_view(request):
    """
    Vista para agregar nueva jornada al proyecto Restaurant
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if request.method == 'POST':
        inicio_fecha = request.POST.get('inicio_fecha')
        inicio_hora = request.POST.get('inicio_hora')
        fin_fecha = request.POST.get('fin_fecha')
        fin_hora = request.POST.get('fin_hora')
        pedido_total = request.POST.get('pedido_total', 0)
        venta_total = request.POST.get('venta_total', 0)
        
        if inicio_fecha and inicio_hora:
            try:
                # Crear jornada en la base de datos
                with connections['cholaoscaleno'].cursor() as cursor:
                    inicio_datetime = f"{inicio_fecha} {inicio_hora}"
                    fin_datetime = f"{fin_fecha} {fin_hora}" if fin_fecha and fin_hora else None
                    
                    cursor.execute("""
                        INSERT INTO jornada (jor_iniciofechahora, jor_finfechahora, jor_pedidototal, 
                                          jor_ventatotal, jor_fechacreacion, usu_codigo)
                        VALUES (%s, %s, %s, %s, NOW(), %s)
                    """, [inicio_datetime, fin_datetime, pedido_total, venta_total, request.user.id])
                
                messages.success(request, 'Jornada creada exitosamente.')
                return redirect('auth:restaurant_jornadas')
                
            except Exception as e:
                messages.error(request, f'Error al crear jornada: {str(e)}')
        else:
            messages.error(request, 'Por favor, completa la fecha y hora de inicio.')
    
    return render(request, 'auth/restaurant_add_jornada.html', {
        'user': request.user,
        'project_name': 'Restaurant',
        'project_icon': 'fas fa-utensils'
    })


def get_restaurant_jornadas():
    """
    Obtener lista de jornadas del proyecto Restaurant
    """
    try:
        with connections['cholaoscaleno'].cursor() as cursor:
            cursor.execute("""
                SELECT j.*, u.username
                FROM jornada j
                LEFT JOIN auth_user u ON j.usu_codigo = u.id
                ORDER BY j.jor_iniciofechahora DESC
                LIMIT 50
            """)
            columns = [col[0] for col in cursor.description]
            jornadas = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return jornadas
    except Exception as e:
        return []


def login_api(request):
    """
    API endpoint para login (para uso con AJAX si es necesario)
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': f'¡Bienvenido, {user.first_name or user.username}!',
                    'redirect_url': '/auth/project-selection/'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Credenciales inválidas'
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Por favor, completa todos los campos'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
