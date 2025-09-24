from django import forms
from .models import Estudiante, Curso, Examen, Calificacion

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'email']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'alumnos'] # Ahora el formulario de curso también tiene el campo alumnos

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['curso', 'fecha']

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['estudiante', 'examen', 'nota']

class BuscarEstudianteForm(forms.Form):
    query = forms.CharField(label="Buscar Estudiante por nombre", max_length=100)