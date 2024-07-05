from django.urls import path
from . import views

urlpatterns = [
   path('', views.principal, name='principal'), 
   path('sobrenosotros', views.nosotros, name='nosotros'),
   path('mesa', views.mesa, name='mesa'),
   path('sillas', views.silla, name='silla'),
   path('iniciosesion', views.inicio, name='inicio'),
   path('registro', views.registro, name='registro'),
]
