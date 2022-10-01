from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Docente
from .forms import DocenteForm

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def docentes(request):
    docentes=Docente.objects.all()#se consulta los docentes
    return render(request, 'docentes/index.html',{'docentes': docentes})#nombre y valor 

def crear(request):
    formulario= DocenteForm(request.POST or None, request.FILES or None)
    if (formulario.is_valid()):
        formulario.save()
        return redirect('docentes')
    return render(request, 'docentes/crear.html',{'formulario': formulario})

def editar(request,id):
    curso=Docente.objects.get(id=id)
    formulario= DocenteForm(request.POST or None, request.FILES or None,instance=curso)
    if (formulario.is_valid() and request.POST):
        formulario.save()
        return redirect('docentes')
    return render(request, 'docentes/editar.html',{'formulario': formulario})

def eliminar(request,id):
    curso=Docente.objects.get(id=id)
    curso.delete()
    return redirect('docentes')

