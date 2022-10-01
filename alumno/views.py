from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Alumno
from .forms import AlumnoForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def alumnos(request):
    alumnos=Alumno.objects.all()#se consulta los alumnos
    return render(request, 'alumnos/index.html',{'alumnos': alumnos})#nombre y valor 

def crear(request):
    formulario= AlumnoForm(request.POST or None, request.FILES or None)
    if (formulario.is_valid()):
        formulario.save()
        return redirect('alumnos')
    return render(request, 'alumnos/crear.html',{'formulario': formulario})

def editar(request,id):
    curso=Alumno.objects.get(id=id)
    formulario= AlumnoForm(request.POST or None, request.FILES or None,instance=curso)
    if (formulario.is_valid() and request.POST):
        formulario.save()
        return redirect('alumnos')
    return render(request, 'alumnos/editar.html',{'formulario': formulario})

def eliminar(request,id):
    curso=Alumno.objects.get(id=id)
    curso.delete()
    return redirect('alumnos')

