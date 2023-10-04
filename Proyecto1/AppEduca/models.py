from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    especialidad = models.CharField(max_length=30)

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

class Entrega_de_proyecto(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entrega = models.BooleanField()
