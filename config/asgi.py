"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# Importa el módulo os para interactuar con el sistema operativo
import os

# Importa la función get_asgi_application desde django.core.asgi
# Esta función se usa para obtener la aplicación ASGI de Django
from django.core.asgi import get_asgi_application

# Establece una variable de entorno llamada 'DJANGO_SETTINGS_MODULE'
# Si ya está establecida, esta línea no la cambiará
# 'config.settings' es el módulo de configuración de Django que se usará
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Llama a get_asgi_application() para obtener la aplicación ASGI
# Esta aplicación servirá para manejar solicitudes ASGI (Asynchronous Server Gateway Interface)
application = get_asgi_application()
