from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(Reparacion)

admin.site.register(Proveedor)

admin.site.register(Cliente)

admin.site.register(Repuesto)

admin.site.register(Avatar)

