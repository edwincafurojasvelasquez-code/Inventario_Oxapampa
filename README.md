# Sistema de Inventario Oxapampa

Aplicación web para la gestión de inventario de una tienda, desarrollada como trabajo final del curso.

## Descripción

El sistema permite a un usuario autenticado registrar, listar, editar y eliminar productos, además de visualizar un dashboard con el total de productos registrados.

## Tecnologías utilizadas

- Python 3
- Flask (framework web)
- Jinja2 (motor de plantillas)
- SQLite (base de datos)
- Bootstrap 5 (diseño e interfaz)

## Funcionalidades

- Inicio de sesión con usuario y contraseña
- Dashboard con resumen de productos
- Registrar nuevos productos
- Listar todos los productos
- Editar productos existentes
- Eliminar productos
- Cerrar sesión

## Estructura del proyecto

INVENTARIO-OXAPAMPA/
├── app.py                  # Rutas y lógica principal de Flask
├── database.py             # Conexión y creación de tablas en SQLite
├── models.py                # Clase Producto (CRUD)
├── static/
│   └── css/
│       └── estilos.css
├── templates/
│   ├── layout.html          # Plantilla base
│   ├── index.html           # Página de inicio
│   ├── login.html           # Inicio de sesión
│   ├── dashboard.html       # Panel principal
│   ├── productos.html       # Listado de productos
│   ├── nuevo_producto.html  # Formulario de registro
│   └── editar_producto.html # Formulario de edición
└── requirements.txt

## Instalación y ejecución

1. Clonar el repositorio:

git clone https://github.com/edwincafurojasvelasquez-code/Inventario_Oxapampa.git

2. Instalar las dependencias:

pip install -r requirements.txt

3. Ejecutar la aplicación:

python app.py

4. Abrir en el navegador:

http://127.0.0.1:5000

La base de datos (`inventario.db`) y el usuario administrador se crean automáticamente al iniciar la aplicación por primera vez.

## Credenciales de acceso

- **Usuario:** admin
- **Contraseña:** 123456

## Autor

Edwin Rojas