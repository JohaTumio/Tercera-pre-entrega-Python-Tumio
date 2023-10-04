from django.urls import path
from AppEduca import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entrega_de_proyectos', views.entrega_de_proyectos, name="Entrega_de_proyectos"),
    
]