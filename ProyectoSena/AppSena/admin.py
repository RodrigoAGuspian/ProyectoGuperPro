from django.contrib import admin
from .models import *

# Registramos los modelos al administrador
admin.site.register(Permiso)
admin.site.register(Persona)
admin.site.register(Permiso_persona)
admin.site.register(Rol)
admin.site.register(Rol_persona)
admin.site.register(Programa)
admin.site.register(Ficha)
admin.site.register(Persona_ficha)
