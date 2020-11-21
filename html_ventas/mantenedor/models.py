from django.db import models
#from .models import Registrado



# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    clave = models.CharField(max_length=10)

def __str__(self):
    return self.email






class Cafe(models.Model):
    codCafe = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Tamaño(models.Model):
    codTamaño = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    

class CafeTam(models.Model):
    tamaño = models.CharField(max_length=50)
    codTamaño = models.CharField(max_length=40)
    codCafe = models.OneToOneField(Cafe, on_delete=models.PROTECT)

    def __str__(self):
        return self.tamaño


class FormaPago(models.Model): #steve
    codFormaPago = models.IntegerField(null=False, primary_key=True)
    descripcion = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.descripcion


class Agregado(models.Model):
    codAgregados = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    papellido = models.CharField(max_length=20)
    sapellido = models.CharField(max_length=20)
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    

    def __str__(self):
        return self.rut
    #nombre + ' ' + self.papellido

class Region(models.Model):# steve
    cod_region = models.CharField(max_length=40)
    nombre = models.CharField(max_length= 30)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    cod_region= models.CharField(max_length=40)
    cod_comuna = models.CharField(max_length= 10, default="", primary_key=True)
    nombre = models.TextField(max_length= 30)

    def __str__(self):
        return self.nombre

class Sucursal(models.Model):
    cod_comuna = models.ForeignKey(Persona,on_delete=models.CASCADE,default=0)
    cod_sucursal = models.CharField(max_length=10)
    direccion = models.TextField(default=0)
    
    def __str__(self):
        return self.direccion

class Cargo(models.Model): #steve
    codCargo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    rut = models.AutoField(primary_key=True)  
    codCargo = models.CharField(max_length=200, null=False)
    sueldo = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.rut



class Pedido(models.Model):
    fechaPedido = models.DateField('Fecha de compra')
    descripcion = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200)
    codFormaPago = models.OneToOneField(FormaPago, on_delete=models.PROTECT)
    rut = models.OneToOneField(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return self.numPedido

class Postres(models.Model): #steve
    nombre = models.CharField(max_length=100, default='')
    precio = models.CharField(max_length=20, default='')
    stock = models.CharField(max_length=100, default='')
    img = models.ImageField(default='null',upload_to="fotosPostres")#upload_to='fotosImg'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'postres' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos

class Catalogos(models.Model): #steve
    nombre = models.CharField(max_length=100, default='')
    imgCatalogo = models.ImageField(default='null',upload_to="fotosPostres")#upload_to='fotosImg'
 
    class Meta:
         db_table = 'catalogo' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos



