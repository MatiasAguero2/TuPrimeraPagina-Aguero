
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    alumnos = models.ManyToManyField(Estudiante, related_name='cursos_inscritos') # Relación muchos a muchos

    def __str__(self):
        return self.nombre

class Examen(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.curso} - {self.fecha}"

class Calificacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Nota de {self.estudiante.nombre} en {self.examen.curso.nombre}: {self.nota}"