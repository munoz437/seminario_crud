from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('docentes',views.docentes,name='docentes'),
    path('docentes/crear',views.crear,name='crearDocente'),
    path('docentes/eliminar/<int:id>',views.eliminar,name='eliminarDocente'),
    path('docentes/editar/<int:id>',views.editar,name='editarDocente'),

]