from django.shortcuts import render, redirect
from .models import Estudiante, Curso, Examen
from .forms import EstudianteForm, CursoForm, ExamenForm, BuscarEstudianteForm


def home(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "core/home.html", {"estudiantes": estudiantes})


def nuevo_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = EstudianteForm()
    return render(request, "core/estudiante_form.html", {"form": form})


def nuevo_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CursoForm()
    return render(request, "core/curso_form.html", {"form": form})


def nuevo_examen(request):
    if request.method == "POST":
        form = ExamenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pagina_caida")
    else:
        form = ExamenForm()
    return render(request, "core/examen_form.html", {"form": form})


def buscar_estudiante(request):
    resultados = []
    if request.method == "POST":
        form = BuscarEstudianteForm(request.POST)
        if form.is_valid():
            termino = form.cleaned_data["query"]
            resultados = Estudiante.objects.filter(nombre__icontains=termino)
    else:
        form = BuscarEstudianteForm()
    return render(request, "core/buscar.html", {"form": form, "resultados": resultados})


def pagina_caida(request):
    return render(request, "core/pagina_caida.html")