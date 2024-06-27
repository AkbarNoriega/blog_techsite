from django.contrib import admin
from .models import Post

# Registro del modelo Post para que aparezca en el administrador de Django
admin.site.register(Post)
