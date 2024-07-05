from django.shortcuts import render

# Create your views here.
def principal(request):
    context={}
    hola=1
    return render(request,'pages/principal.html',context)

def nosotros(request):
    context={}
    return render(request,'pages/sobrenosotros.html',context)

def mesa(request):
    context={}
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