from django.shortcuts import render, redirect
from AppEduca.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario, EntregaFormulario, BuscaCursoForm, BuscaEstudianteForm
from AppEduca.models import Curso, Estudiante, Profesor, Entrega_de_proyecto

def inicio(request):
    cursos = []
    estudiantes = []

    if request.method == "POST":
        # Formulario de búsqueda de cursos
        cursoForm = BuscaCursoForm(request.POST)
        if cursoForm.is_valid():
            informacion_curso = cursoForm.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=informacion_curso["curso"])

        # Formulario de búsqueda de estudiantes
        estudianteForm = BuscaEstudianteForm(request.POST)
        if estudianteForm.is_valid():
            informacion_estudiante = estudianteForm.cleaned_data
            estudiantes = Estudiante.objects.filter(nombre__icontains=informacion_estudiante["nombre"])
        return render(request, "AppEduca/resBusqForm.html", {"cursos": cursos, "estudiantes": estudiantes})

    else:
        cursoForm = BuscaCursoForm()
        estudianteForm = BuscaEstudianteForm()
    return render(request, "AppEduca/index.html", {"cursoForm":cursoForm, "estudianteForm":estudianteForm})


def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], especialidad=informacion["especialidad"])
            profesor.save()
            return redirect("Inicio")
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "AppEduca/profesores.html", {"miFormulario": miFormulario})

def entrega_de_proyectos(request):
    if request.method == "POST":
        miFormulario = EntregaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entregaDeProyecto = Entrega_de_proyecto(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entrega=informacion["entrega"])
            entregaDeProyecto.save()
            return redirect("Inicio")
    else:
        miFormulario = EntregaFormulario()
    return render(request, "AppEduca/entrega_de_proyectos.html", {"miFormulario": miFormulario})

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return redirect("Inicio")
    else:
        miFormulario = CursoFormulario()
    return render(request, "AppEduca/cursos.html", {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], edad=informacion["edad"], email=informacion["email"])
            estudiante.save()
            return redirect("Inicio")
    else:
        miFormulario = EstudianteFormulario()
    return render(request, "AppEduca/estudiantes.html", {"miFormulario": miFormulario})


