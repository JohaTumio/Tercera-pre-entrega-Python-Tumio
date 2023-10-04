from django.contrib import admin
from .models import Curso, Entrega_de_proyecto, Estudiante, Profesor

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Entrega_de_proyecto)
admin.site.register(Profesor)
