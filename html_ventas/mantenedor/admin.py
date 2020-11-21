from django.contrib import admin

#from .models import Registrado

from .models import Registrado
from .forms import RegModelForm

# Register your models here.
class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp","clave"]
    form = RegModelForm
    #list_display_link = ["nombre"]
    list:filter = ["timestamp"]
    list_editable = ["nombre"]
    list_fields = ["email","nombre","clave"]
    class Meta:
        model = Registrado

admin.site.register(Registrado)

