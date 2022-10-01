from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('cursos',views.cursos,name='cursos'),
    path('cursos/crear',views.crear,name='crearCurso'),
    path('cursos/eliminar/<int:id>',views.eliminar,name='eliminarCurso'),
    path('cursos/editar/<int:id>',views.editar,name='editarCurso'),

]