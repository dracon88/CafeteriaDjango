"""html_ventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from rest_framework import routers
#from django.views.generic import TemplateView
from mantenedor.views import PostresListado, PostreDetalle, PostreCrear, PostreActualizar, PostreEliminar \
    ,EmpleadoListado, EmpleadoDetalle, EmpleadoCrear, EmpleadoActualizar, EmpleadoEliminar, FormaPagoListado\
    ,FormaPagoListado, FormaPagoDetalle, FormaPagoCrear, FormaPagoActualizar, FormaPagoEliminar, FormaPagoListado\
    ,CargoListado, CargoDetalle, CargoCrear, CargoActualizar, CargoEliminar, CargoListado \
    ,RegionListado, RegionDetalle, RegionCrear, RegionActualizar, RegionEliminar, RegionListado \
    ,PersonaListado, PersonaDetalle, PersonaCrear, PersonaActualizar, PersonaEliminar, PersonaListado, persona_detalle, persona_lista, registro_usuario \
   
    


 
#from postres.views import PostresList
 
from django.conf import settings
from django.conf.urls.static import static 
from mantenedor import views
from django.contrib.auth.views import LoginView 
from django.urls import include
from rest_framework import routers
from django.contrib.auth import views as auth_views
from django.conf.urls import url

#router = routers.DefaultRouter()
#router.register(r'personas', PersonaViewSet)




 
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('postresInicio', views.postresInicio, name='postresInicio'),
    path('tortasInicio', views.tortasInicio, name='tortasInicio'),
    path('heladosInicio', views.heladosInicio, name='heladosInicio'),
    path('nosotrosInicio', views.nosotrosInicio, name='nosotrosInicio'),
    path('carrito', views.carrito, name='carrito'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('oauth/', include('social_django.urls', namespace='social')),
    #path('api/',include(router.urls)),    
    path('persona_get/', persona_lista),
    path('persona_get/<int:pk>', persona_detalle),
    
    
  
   

  
  path('reset_password/', 
       auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
       name="reset_password"),
  
  
  path('reset_password_sent/',
       auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_send.html"),
       name="password_reset_done"),
  
  path('reset/<uidb64>/<token>/', 
       auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
       name="password_reset_confirm"),
  
  
  path('reset_password_complete/', 
       auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
       name="password_reset_complete"),
    
    
    
    #path('cliente', views.cliente, name='cliente'),
    #path('pedido', views.pedido, name='pedido'),
    #path('usuario', views.usuario, name='usuario'),
    #path('inicio', views.volver, name='inicio'),
     #path('empleado', views.empleado, name='empleado'),
    
    path('admin/', admin.site.urls),
    path('index', PostresListado.as_view(template_name = "postres/indexFrm.html"), name='index'),
    path('postres/', login_required(PostresListado.as_view()), name='postres'),
    path('postres/detalle/<int:pk>', PostreDetalle.as_view(template_name = "postres/detallesFrm.html"), name='detalles'), 
    path('postres/crear', PostreCrear.as_view(template_name = "postres/crearFrm.html"), name='crear'),
    path('postres/editar/<int:pk>', PostreActualizar.as_view(template_name = "postres/actualizarFrm.html"), name='actualizar'),    
    path('postres/eliminar/<int:pk>', PostreEliminar.as_view(), name='eliminar'), 
    
    ############### PAGO#####################
    
    path('formaPago/', login_required(FormaPagoListado.as_view()), name='pago'),
    path('formaPago/', FormaPagoListado.as_view(template_name = "formaPago/indexFrm.html"), name='pago'),
    path('formaPago/detalle/<int:pk>', FormaPagoDetalle.as_view(template_name = "formaPago/detallesFrm.html"), name='detalles'), 
    path('formaPago/crear', FormaPagoCrear.as_view(template_name = "formaPago/crearFrm.html"), name='crear'),
    path('formaPago/editar/<int:pk>', FormaPagoActualizar.as_view(template_name = "formaPago/actualizarFrm.html"), name='actualizar'),    
    path('formaPago/eliminar/<int:pk>', FormaPagoEliminar.as_view(), name='eliminar'), 
    
    
    
    ############### Empleado #####################
 
    path('empleado/', login_required(EmpleadoListado.as_view()), name='empleado'),
    path('empleado/', EmpleadoListado.as_view(template_name = "empleado/indexFrm.html"), name='empleado'),
    path('empleado/detalle/<int:pk>', EmpleadoDetalle.as_view(template_name = "empleado/detallesFrm.html"), name='detalles'), 
    path('empleado/crear', EmpleadoCrear.as_view(template_name = "empleado/crearFrm.html"), name='crear'),
    path('empleado/editar/<int:pk>', EmpleadoActualizar.as_view(template_name = "empleado/actualizarFrm.html"), name='actualizar'),    
    path('empleado/eliminar/<int:pk>', EmpleadoEliminar.as_view(), name='eliminar'), 
    
    
    
    
    
    
    ############## CARGO ##############
    path('cargo/', login_required(CargoListado.as_view()), name='cargo'),
    path('cargo/', CargoListado.as_view(template_name = "cargo/indexFrm.html"), name='cargo'),
    path('cargo/detalle/<int:pk>', CargoDetalle.as_view(template_name = "cargo/detallesFrm.html"), name='detalles'), 
    path('cargo/crear', CargoCrear.as_view(template_name = "cargo/crearFrm.html"), name='crear'),
    path('cargo/editar/<int:pk>', CargoActualizar.as_view(template_name = "cargo/actualizarFrm.html"), name='actualizar'),    
    path('cargo/eliminar/<int:pk>', CargoEliminar.as_view(), name='eliminar'), 
    
    
    
    
    ################# REGION #################################
    path('region/', login_required(RegionListado.as_view()), name='region'),
    path('region/', RegionListado.as_view(template_name = "region/indexFrm.html"), name='region'),
    path('region/detalle/<int:pk>', RegionDetalle.as_view(template_name = "region/detallesFrm.html"), name='detalles'), 
    path('region/crear', RegionCrear.as_view(template_name = "region/crearFrm.html"), name='crear'),
    path('region/editar/<int:pk>', RegionActualizar.as_view(template_name = "region/actualizarFrm.html"), name='actualizar'),    
    path('region/eliminar/<int:pk>', RegionEliminar.as_view(), name='eliminar'),
    
    
    ################ PERSONA ################################
    #path('persona/', login_required(PersonaListado.as_view()), name='persona'),
    path('persona/', PersonaListado.as_view(template_name = "persona/indexFrm.html"), name='persona'),
    path('persona/detalle/<int:pk>', PersonaDetalle.as_view(template_name = "persona/detallesFrm.html"), name='detalles'), 
    path('persona/crear', PersonaCrear.as_view(template_name = "persona/crearFrm.html"), name='crear'),
    path('persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "persona/actualizarFrm.html"), name='actualizar'),    
    path('persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='eliminar'),
    
    
    
    
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)