from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Página principal
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Detalle de la publicación
    path('post/new/', views.post_new, name='post_new'),  # Crear nueva publicación
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  # Editar publicación
]
