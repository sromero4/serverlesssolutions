# Sistema de Gestión Multi-Proyecto SSS

Este documento describe la implementación del sistema de gestión multi-proyecto que permite a los usuarios seleccionar entre diferentes proyectos (Restaurant y Conjunto) después del login.

## 🎯 Características Principales

### 🔐 **Sistema de Autenticación Multi-Proyecto**
- **Login único**: Un solo login para acceder a todos los proyectos
- **Selección de proyecto**: Interfaz elegante para elegir el proyecto deseado
- **Dashboards específicos**: Cada proyecto tiene su propio dashboard personalizado
- **Navegación fluida**: Cambio fácil entre proyectos sin re-login

### 🎨 **Diseño con Gradientes Cálidos**
- **Paleta de colores cálidos**: Tonos naranjas, amarillos y rosas
- **Gradientes modernos**: Efectos visuales atractivos y profesionales
- **Interfaz responsiva**: Adaptable a todos los dispositivos
- **Animaciones suaves**: Transiciones elegantes y efectos visuales

## 🏗️ **Arquitectura del Sistema**

### **Flujo de Navegación**
```
Login → Selección de Proyecto → Dashboard Específico
  ↓           ↓                    ↓
Usuario    Restaurant/Conjunto   Datos del Proyecto
```

### **Estructura de Proyectos**

#### **1. Proyecto Restaurant**
- **Base de datos**: `cholaoscaleno`
- **Modelos principales**:
  - Pedidos
  - Productos
  - Ingredientes
  - Inventarios
  - Jornadas
  - Usuarios

#### **2. Proyecto Conjunto**
- **Base de datos**: `napoli`
- **Modelos principales**:
  - Torres
  - Apartamentos
  - Habitantes
  - Propietarios
  - Personas
  - Usuarios

## 📁 **Estructura de Archivos**

```
sss_backend/
├── auth_app/
│   ├── views.py                 # Vistas de autenticación y dashboards
│   ├── urls.py                  # URLs de autenticación
│   └── ...
├── templates/
│   └── auth/
│       ├── project_selection.html    # Selección de proyecto
│       ├── restaurant_dashboard.html # Dashboard Restaurant
│       ├── conjunto_dashboard.html   # Dashboard Conjunto
│       └── login.html               # Login original
└── static/
    ├── css/
    │   └── main.css            # Estilos principales
    └── js/
        └── main.js             # JavaScript principal
```

## 🚀 **URLs del Sistema**

### **Autenticación**
- `/auth/login/` - Página de login
- `/auth/logout/` - Cerrar sesión
- `/auth/project-selection/` - Selección de proyecto

### **Dashboards por Proyecto**
- `/auth/restaurant/` - Dashboard del proyecto Restaurant
- `/auth/conjunto/` - Dashboard del proyecto Conjunto

## 🎨 **Diseño y Estilos**

### **Gradientes Cálidos Implementados**

#### **Selección de Proyecto**
```css
background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
```

#### **Dashboard Restaurant**
```css
background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
header: linear-gradient(135deg, #ff6b6b 0%, #ff8e8e 100%);
```

#### **Dashboard Conjunto**
```css
background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 50%, #fcb69f 100%);
header: linear-gradient(135deg, #ffc107 0%, #ffeb3b 100%);
```

### **Elementos Visuales**
- **Cards con glassmorphism**: Efecto de vidrio esmerilado
- **Iconografía consistente**: Font Awesome para todos los iconos
- **Animaciones suaves**: Hover effects y transiciones
- **Responsive design**: Adaptable a móviles y tablets

## 📊 **Funcionalidades por Dashboard**

### **Dashboard Restaurant**
- **Estadísticas en tiempo real**:
  - Total de pedidos
  - Productos en menú
  - Ingredientes disponibles
  - Inventarios activos
  - Pedidos del día
  - Ventas del día

- **Acciones rápidas**:
  - Nuevo pedido
  - Agregar producto
  - Gestionar ingredientes
  - Ver reportes

- **Actividad reciente**:
  - Últimos pedidos
  - Productos agregados
  - Actualizaciones de inventario

### **Dashboard Conjunto**
- **Estadísticas en tiempo real**:
  - Total de torres
  - Apartamentos disponibles
  - Habitantes registrados
  - Propietarios activos
  - Personas en el sistema

- **Acciones rápidas**:
  - Nueva torre
  - Nuevo apartamento
  - Registrar habitante
  - Ver reportes

- **Actividad reciente**:
  - Nuevos habitantes
  - Apartamentos creados
  - Torres agregadas

## 🔧 **Configuración Técnica**

### **Conexiones a Base de Datos**
```python
# Restaurant - Base de datos cholaoscaleno
with connections['cholaoscaleno'].cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM pedido")

# Conjunto - Base de datos napoli
with connections['napoli'].cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM apartamento")
```

### **Funciones de Estadísticas**
- `get_restaurant_stats()`: Obtiene estadísticas del proyecto Restaurant
- `get_conjunto_stats()`: Obtiene estadísticas del proyecto Conjunto
- **Manejo de errores**: Fallback a datos de ejemplo si hay problemas de conexión

## 🎯 **Características de UX/UI**

### **Experiencia de Usuario**
1. **Login intuitivo**: Formulario simple y claro
2. **Selección visual**: Cards atractivas para elegir proyecto
3. **Dashboards informativos**: Información relevante y accionable
4. **Navegación fluida**: Cambio fácil entre proyectos
5. **Feedback visual**: Mensajes y animaciones informativas

### **Elementos de Diseño**
- **Glassmorphism**: Efectos de vidrio esmerilado
- **Gradientes cálidos**: Paleta de colores acogedora
- **Iconografía consistente**: Font Awesome en todo el sistema
- **Tipografía moderna**: Google Fonts (Inter)
- **Animaciones suaves**: Transiciones elegantes

## 📱 **Responsive Design**

### **Breakpoints**
- **Desktop**: > 768px - Layout completo con sidebar
- **Tablet**: 768px - Layout adaptado
- **Mobile**: < 768px - Layout vertical optimizado

### **Adaptaciones Móviles**
- **Sidebar colapsable**: En móviles se convierte en menú superior
- **Cards apiladas**: En pantallas pequeñas
- **Botones táctiles**: Optimizados para touch
- **Texto legible**: Tamaños apropiados para móviles

## 🚀 **Instalación y Uso**

### **1. Configuración de Base de Datos**
Asegúrate de que las bases de datos estén configuradas:
- `cholaoscaleno` para Restaurant
- `napoli` para Conjunto

### **2. Ejecutar el Sistema**
```bash
cd sss_backend
python manage.py runserver
```

### **3. Acceso**
1. Navega a `http://localhost:8000/`
2. Inicia sesión con tus credenciales
3. Selecciona el proyecto deseado
4. Explora el dashboard específico

## 🔮 **Próximas Mejoras**

### **Funcionalidades Planificadas**
- **Dashboard personalizable**: Widgets configurables
- **Notificaciones en tiempo real**: WebSockets para actualizaciones
- **Reportes avanzados**: Gráficos y análisis detallados
- **Integración de APIs**: Conexión con servicios externos
- **Modo oscuro**: Tema alternativo para usuarios

### **Mejoras Técnicas**
- **Caché de estadísticas**: Optimización de consultas
- **Paginación**: Para listas largas de datos
- **Búsqueda avanzada**: Filtros y búsqueda en tiempo real
- **Exportación de datos**: PDF, Excel, CSV
- **Auditoría**: Log de actividades del usuario

## 🛠️ **Desarrollo y Extensión**

### **Agregar Nuevo Proyecto**
1. **Crear nueva base de datos** en `settings.py`
2. **Agregar función de estadísticas** en `views.py`
3. **Crear template de dashboard** específico
4. **Registrar URL** en `urls.py`
5. **Agregar card de selección** en `project_selection.html`

### **Personalizar Dashboards**
- **Modificar estadísticas**: Editar funciones `get_*_stats()`
- **Cambiar colores**: Actualizar gradientes en CSS
- **Agregar funcionalidades**: Nuevas acciones rápidas
- **Personalizar sidebar**: Menús específicos por proyecto

## 📞 **Soporte**

Para soporte técnico, preguntas o sugerencias sobre el sistema multi-proyecto, contacta al equipo de desarrollo.

---

**Nota**: Este sistema está diseñado para ser escalable y fácil de mantener. La arquitectura modular permite agregar nuevos proyectos sin afectar los existentes.
