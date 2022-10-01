from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('alumnos',views.alumnos,name='alumnos'),
    path('alumnos/crear',views.crear,name='crearAlumno'),
    path('alumnos/eliminar/<int:id>',views.eliminar,name='eliminarAlumno'),
    path('alumnos/editar/<int:id>',views.editar,name='editarAlumno'),

]