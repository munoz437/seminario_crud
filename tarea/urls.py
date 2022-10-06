from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('tareas',views.tareas,name='tareas'),
    path('tareas/crear',views.crear,name='crearTarea'),
    path('tareas/eliminar/<int:id>',views.eliminar,name='eliminarTarea'),
    path('tareas/editar/<int:id>',views.editar,name='editarTarea'),

]