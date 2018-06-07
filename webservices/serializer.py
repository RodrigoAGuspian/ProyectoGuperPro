from rest_framework import serializers
from AppSena.models import *
from django.contrib.auth.models import User

#======================== USUARIO ===============================
class user_serializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('url','username','email','password')
#================================================================

#======================= PERSONA ================================
class persona_serializer(serializers.ModelSerializer):
	class Meta:
		model  = Persona
		fields = ('url','documentoIdentidad','nombres','apellidos','telefono','imgPerfil')
#=================================================================

#=================== ACTUALIZAR PERFIL ===========================
class actualizar_perfil_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Persona
		fields =('url','documentoIdentidad','nombres','apellidos','telefono','usuario')
#=================================================================

#======================== VER PERMISOS ===========================
class ver_permisos_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permiso_persona
		fields =('estado','instructor','vigilante','permiso_id','persona_id')
#=================================================================

#===================== SOLICITAR PERMISO ===========================
class solicitar_permiso_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permiso
		fields =('url','motivo','solicitoPermisoPor','permisoPorHora','permisoPorDias','horaSalida','fecha')
#=================================================================

#===================== APRENDIZ_PERMISO ===========================
class aprendiz_permiso_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Permiso_persona
		fields =('url','estado','instructor','vigilante','permiso','persona')
#=================================================================