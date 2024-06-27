from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Definición de las rutas principales del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el administrador de Django
    path('', include('blog.urls')),  # Incluir las rutas de la aplicación de blog
]

# Servir archivos de medios en modo de depuración
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
