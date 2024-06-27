from django.db import models
from django.utils import timezone

# Modelo de datos para las publicaciones del blog
class Post(models.Model):
    title = models.CharField(max_length=200)  # Título de la publicacion
    content = models.TextField()  # Contenido de la publicacion
    created_at = models.DateTimeField(default=timezone.now)  # Fecha y hora de creacion
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Imagen opcional para la publicacion
    price = models.DecimalField(max_digits=10, decimal_places=2) #Precio del articulo
    def __str__(self):
        return self.title  # Representación en cadena del objeto, muestra el título
