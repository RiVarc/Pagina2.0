from django.db import models

# Create your models here.

class Mesas(models.Model):
    id_mesas=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    descripcion=models.TextField(null=False,blank=False)
    precio=models.IntegerField(null=False,blank=False)
    cantidad=models.IntegerField(null=False,blank=False)
    imagen=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return(
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )
    

class Silla(models.Model):
    id_Sillas=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=False,blank=False)
    descripcion=models.TextField(null=False,blank=False)
    precio=models.IntegerField(null=False,blank=False)
    cantidad=models.IntegerField(null=False,blank=False)
    imagen=models.CharField(max_length=100,null=False,blank=False)
    def __str__(self):
        return(
            str(self.nombre)
            + ", precio: "
            + str(self.precio)
        )