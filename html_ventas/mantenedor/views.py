from django.shortcuts import render,redirect
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
from .models import Postres
from .models import Empleado
from .models import FormaPago
from .models import Cargo
from .models import Region
from .models import Persona
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms 
from mantenedor import views

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import  RegisterForm
from .models import Registrado
from django.contrib.auth import login, authenticate

## rest_framework #####
from rest_framework import viewsets
from .serializers import PersonaSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse








# Create your views here
def inicio(request):
    return render(request,"inicio/inicioFr.html",{})

def postresInicio(request):
    models = Postres.objects.all()
    return render(request,"inicio/postresFr.html",{'postres':models})

def tortasInicio(request):
    return render(request,"inicio/tortasFr.html",{})

def heladosInicio(request):
    return render(request,"inicio/heladosFr.html",{})

def nosotrosInicio(request):
    return render(request,"inicio/nosotrosFr.html",{})



def stock(request):
    return render(request,"inicio/stockFr.html",{})

def carrito(request):
    return render(request,"inicio/carritoFrm.html",{})

def registros(request):
    form = RegForm()
    context = {
        "el_form" : form,
    }
    return render(request,"registration/registro.html",context)

############ registro formulario####################

#def registro(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form.cleaned_data["email"]
        abc2 = form.cleaned_data["nombre"]
        clave = form.cleaned_data["clave"]
        obj = Registrado.objects.create(email=abc,nombre=abc2,clave=clave)
        
    
    context = {
        "form": form,
    }
    return render(request, "inicio/registrate.html", context)



def registro_usuario(request):
    data = {
        'form':RegisterForm()
    }
    
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario y redirige al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, F"Bienvenid@ a nuestra cafeteria {username}")
            login(request, user)
            return redirect(to='/')
        else:
            for msg in forms.error_messages:
                messages.error(request, forms.error_messages[msg])
    return render(request, 'inicio/registrate.html',data)






class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro.html"
    from_class = UserCreationForm
   


            
        



############ Empleado###############
class EmpleadoListado(ListView): 
    model = Empleado # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('empleado') # Redireccionamos a la vista principal 'leer'
    
class EmpleadoCrear(SuccessMessageMixin, CreateView): 
    model = Empleado # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Empleado # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('empleado') # Redireccionamos a la vista principal 'leer'

class EmpleadoDetalle(DetailView): 
    model = Empleado # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('empleado') # Redireccionamos a la vista principal 'leer'
    
    
class EmpleadoActualizar(SuccessMessageMixin, UpdateView): 
    model = Empleado # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Empleado # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('empleado') # Redireccionamos a la vista principal 'leer'
    
    
    
class EmpleadoEliminar(SuccessMessageMixin, DeleteView): 
    model = FormaPago 
    form = FormaPago
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('empleado') # Redireccionamos a la vista principal 'leer'


################ POSTRES ####################

class PostresListado(ListView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('index') # Redireccionamos a la vista principal 'leer'

class PostreCrear(SuccessMessageMixin, CreateView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('index') # Redireccionamos a la vista principal 'leer'

class PostreDetalle(DetailView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('index') # Redireccionamos a la vista principal 'leer'
    
    
class PostreActualizar(SuccessMessageMixin, UpdateView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('index') # Redireccionamos a la vista principal 'leer'
    
    
    
class PostreEliminar(SuccessMessageMixin, DeleteView): 
    model = Postres 
    form = Postres
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('index') # Redireccionamos a la vista principal 'leer'




############## FOrma PAgo###########

class FormaPagoListado(ListView): 
    model = FormaPago # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('pago') # Redireccionamos a la vista principal 'leer'
    
class FormaPagoCrear(SuccessMessageMixin, CreateView): 
    model = FormaPago # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = FormaPago # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Pago Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('pago') # Redireccionamos a la vista principal 'leer'

class FormaPagoDetalle(DetailView): 
    model = FormaPago # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('pago') # Redireccionamos a la vista principal 'leer'
    
    
class FormaPagoActualizar(SuccessMessageMixin, UpdateView): 
    model = FormaPago # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = FormaPago # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Pago Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('pago') # Redireccionamos a la vista principal 'leer'
    
    
    
class FormaPagoEliminar(SuccessMessageMixin, DeleteView): 
    model = FormaPago 
    form = FormaPago
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Pago Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('pago') # Redireccionamos a la vista principal 'leer'
    
    
    
    
###################### CARGO #####################
class CargoListado(ListView): 
    model = Cargo # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('cargo') # Redireccionamos a la vista principal 'leer'

class CargoCrear(SuccessMessageMixin, CreateView): 
    model = Cargo # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Cargo # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cargo Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('cargo') # Redireccionamos a la vista principal 'leer'

class CargoDetalle(DetailView): 
    model = Cargo # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('cargo') # Redireccionamos a la vista principal 'leer'
    
    
class CargoActualizar(SuccessMessageMixin, UpdateView): 
    model = Cargo # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Cargo # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Cargo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('cargo') # Redireccionamos a la vista principal 'leer'
    
    
    
class CargoEliminar(SuccessMessageMixin, DeleteView): 
    model = Cargo 
    form = Cargo
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Cargo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('cargo') # Redireccionamos a la vista principal 'leer'
    
    
    
################### Region ####################
class RegionListado(ListView): 
    model = Region # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('region') # Redireccionamos a la vista principal 'leer'

class RegionCrear(SuccessMessageMixin, CreateView): 
    model = Region # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Region # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'region Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('region') # Redireccionamos a la vista principal 'leer'

class RegionDetalle(DetailView): 
    model = Region # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('region') # Redireccionamos a la vista principal 'leer'
    
    
class RegionActualizar(SuccessMessageMixin, UpdateView): 
    model = Region # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Region # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'region Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('region') # Redireccionamos a la vista principal 'leer'
    
    
    
class RegionEliminar(SuccessMessageMixin, DeleteView): 
    model = Region 
    form = Region
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'region Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('region') # Redireccionamos a la vista principal 'leer'
    
    
    
########### PERSONA ##################

class PersonaListado(ListView): 
    model = Persona # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('persona') # Redireccionamos a la vista principal 'leer'

class PersonaCrear(SuccessMessageMixin, CreateView): 
    model = Persona # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Persona # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'persona Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('persona') # Redireccionamos a la vista principal 'leer'

class PersonaDetalle(DetailView): 
    model = Persona # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    def get_success_url(self):        
        return reverse('persona') # Redireccionamos a la vista principal 'leer'
    
    
class PersonaActualizar(SuccessMessageMixin, UpdateView): 
    model = Persona # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Persona # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('persona') # Redireccionamos a la vista principal 'leer'
    
    
    
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
    model = Persona 
    form = Persona
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'region Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('persona') # Redireccionamos a la vista principal 'leer'
    
    
    
    

    
##### Persona en Api 

  
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        
        
        
@csrf_exempt
def persona_lista(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        persona = Persona.objects.all()
        serializer = PersonaSerializer(persona, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        persona = PersonaSerializer(data=data)
        if persona.is_valid():
            persona.save()
            return JSONResponse(persona.data, status=201)
        return JSONResponse(persona.errors, status=400)


@csrf_exempt
def persona_detalle(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        persona = PersonaSerializer(persona)
        return JSONResponse(persona.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        persona = PersonaSerializer(persona, data=data)
        if persona.is_valid():
            persona.save()
            return JSONResponse(persona.data)
        return JSONResponse(persona.errors, status=400)

    elif request.method == 'DELETE':
        persona.delete()
        return HttpResponse(status=204)

