from django.shortcuts import render, redirect
from django.http import HttpResponse



from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from publica.forms import PlantaForm
from publica.models import Planta,Categoria

# Create your views here.

def index(request):
    return render(request, 'publica/index.html')

def nosotros(request):
    return render(request, 'publica/nosotros.html')

def contacto(request):
    return render(request, 'publica/contacto.html')

def productos(request):
    return render(request, 'publica/productos.html')


def planton(request):
    return render(request, 'publica/productos.html')


def plantin(request):
    variable = 'xxxxxxyyyyy  zzzzzz'
    return render(request,'publica/plantin.html',
                  {'variable':variable})

def nuevo(request):
    if(request.method=='POST'):
        formulario = PlantaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantas_index')
    else:
        formulario =PlantaForm()
    return render(request,'publica/nuevo.html',{'form':formulario})

"""
    CRUD Plantas
"""
def plantas_index(request):
    #queryset
    plantas = Planta.objects.all()
    return render(request,'publica/plantas/index.html',{'plantas':plantas})

def plantas_nuevo(request):
    if(request.method=='POST'):
        formulario = CursoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('plantas_index')
    else:
        formulario = CursoForm()
    return render(request,'publica/cursos/nuevo.html',{'form':formulario})

def plantas_editar(request,id_planta):
    try:
        curso = Curso.objects.get(pk=id_planta)
    except Curso.DoesNotExist:
        return render(request,'publica/404_admin.html')

    if(request.method=='POST'):
        formulario = CursoForm(request.POST,request.FILES, instance=planta)
        if formulario.is_valid():
            formulario.save()
            return redirect('planta_index')
    else:
        formulario = PlantaForm(instance=planta)
    return render(request,'publica/plantas/editar.html',{'form':formulario})

