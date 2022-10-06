from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarea
from .forms import TareaForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def tareas(request):
    tareas=Tarea.objects.all()#se consulta los tareas
    return render(request, 'tareas/index.html',{'tareas': tareas})#nombre y valor 

def crear(request):
    formulario= TareaForm(request.POST or None, request.FILES or None)
    if (formulario.is_valid()):
        formulario.save()
        return redirect('tareas')
    return render(request, 'tareas/crear.html',{'formulario': formulario})

def editar(request,id):
    curso=Tarea.objects.get(id=id)
    formulario= TareaForm(request.POST or None, request.FILES or None,instance=curso)
    if (formulario.is_valid() and request.POST):
        formulario.save()
        return redirect('tareas')
    return render(request, 'tareas/editar.html',{'formulario': formulario})

def eliminar(request,id):
    curso=Tarea.objects.get(id=id)
    curso.delete()
    return redirect('tareas')

