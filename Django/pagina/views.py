from django.shortcuts import render
from .models import Mesas,Silla
# Create your views here.
def principal(request):
    context={}

    return render(request,'pages/principal.html',context)

def nosotros(request):
    context={}
    return render(request,'pages/sobrenosotros.html',context)

def mesa(request):
    mesas=Mesas.objects.all()
    context={
        'mesas':mesas
    }
    return render(request,'pages/mesa.html',context)

def silla(request):
    context={}
    return render(request,'pages/sillas.html',context)

def inicio(request):
    context={}
    return render(request,'pages/iniciosesion.html',context)

def registro(request):
    context={}
    return render(request,'pages/registro.html',context)

def crud(request):
    mesas=Mesas.objects.all()
    sillas=Silla.objects.all()
    context={
        'mesas':mesas,
        'sillas':sillas
    }
    return render(request,'pages/CRUD.html',context)

def eliminar_me(request,pk):
    try:
        mesas=Mesas.objects.get(id_mesas=pk)
        mesas.delete()
        mesas=Mesas.objects.all()
        sillas=Silla.objects.all()
        context={
            'mesas':mesas,
            'sillas':sillas
        }
        return render(request,'pages/CRUD.html',context)
    except:
        mesas=Mesas.objects.all()
        context={
            'mesas':mesas,
            "mensaje":"Eliminado con exito"
        }
        return render(request,'pages/CRUD.html',context)
    
def eliminar_si(request,pk):
    try:
        sillas=Silla.objects.get(id_Sillas=pk)
        sillas.delete()
        sillas=Silla.objects.all()
        mesas=Mesas.objects.all()
        context={
            'sillas':sillas,
            'mesas':mesas
        }
        return render(request,'pages/CRUD.html',context)
    except:
        sillas=Silla.objects.all()
        context={
            'sillas':sillas,
            "mensaje":"Eliminado con exito"
        }
        return render(request,'pages/CRUD.html',context)
    
def agregar (request):
    if request.method !="post":
    
        context={
        }
        return render (request,'pages/agregar.html',context)
    else:
        nombre=request.POST.get("nombre")
        descripcion=request.POST.get("descripcion")
        precio=request.POST.get("precio")
        cantidad=request.POST.get("cantidad")
        imagen=request.POST.get("imagen")
        mesa=Mesas.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad,
            imagen=imagen
        )
        mesa.save()
        context={
            "mensaje":"Registro exitosos"
        }