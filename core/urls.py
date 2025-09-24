from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('estudiante/nuevo/', views.nuevo_estudiante, name="nuevo_estudiante"),
    path('curso/nuevo/', views.nuevo_curso, name="nuevo_curso"),
    path('examen/nuevo/', views.nuevo_examen, name="nuevo_examen"),
    path('buscar/', views.buscar_estudiante, name="buscar_estudiante"),
    path('caida/', views.pagina_caida, name="pagina_caida"),
]