from AppSena.models import *
from .serializer import *
from rest_framework import viewsets

#========================= USUARIO =============================
class user_viewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class =  user_serializer
#===============================================================

#========================= PERSONA =============================
class persona_viewset(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class =  persona_serializer
#===============================================================

#==================== MODIFICAR PERFIL =========================
class actualizar_perfil_viewset(viewsets.ModelViewSet):
	queryset = Persona.objects.all()
	serializer_class = actualizar_perfil_serializer
#===============================================================

#======================== VER PERMISOS =========================
class ver_permisos_viewset(viewsets.ModelViewSet):
	queryset = Permiso_persona.objects.all()
	serializer_class = ver_permisos_serializer
#===============================================================

#======================== SOLICITAR PERMISOS =========================
class solicitar_permiso_viewset(viewsets.ModelViewSet):
	queryset = Permiso.objects.all()
	serializer_class = solicitar_permiso_serializer
#===============================================================




#======================== APRENDIZ PERMISOS =========================
class aprendiz_permiso_viewset(viewsets.ModelViewSet):
	queryset = Permiso_persona.objects.all()
	serializer_class = aprendiz_permiso_serializer
#===============================================================