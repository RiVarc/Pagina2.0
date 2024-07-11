from django.urls import path
from . import views

urlpatterns = [
   path('', views.principal, name='principal'), 
   path('sobrenosotros', views.nosotros, name='nosotros'),
   path('mesa', views.mesa, name='mesa'),
   path('sillas', views.silla, name='silla'),
   path('iniciosesion', views.inicio, name='inicio'),
   path('registro', views.registro, name='registro'),
   path('crud', views.crud, name='crud'),
   path('eliminar_me/<str:pk>', views.eliminar_me, name='eliminar_me'),
   path('eliminar_si/<str:pk>', views.eliminar_si, name='eliminar_si'),
   path('agregar', views.agregar, name='agregar'),
   path('compra', views.compra, name='compra'),
   path('finalizar', views.finalizar, name='finalizar'),
]
