from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('cursos',views.cursos,name='cursos'),
    path('cursos/crear',views.crear,name='crear'),
    path('cursos/editar',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('cursos/editar/<int:id>',views.editar,name='editar'),

]