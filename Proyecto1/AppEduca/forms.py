from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=30)
    comision = forms.IntegerField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=30)

class EntregaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaDeEntrega = forms.DateField(label='Fecha de Entrega', widget=forms.DateInput(attrs={'placeholder':'mes/día/año'}))
    entrega = forms.BooleanField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField(max_length=30)

class BuscaEstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    