from django.db import models
from django.contrib.auth.models import User

# MODELS
#======================PERMISO====================#
class Permiso(models.Model):
	motivos = (
		('Enfermedad', 'Enfermedad'),
		('Accidente', 'Accidente'),
		('Calamidad domestica', 'Calamidad domestica'),
		('Otro','Otro'),
		)
	motivo = models.CharField(max_length = 45,  choices=motivos)
	solicitoPermisoPor = models.CharField(max_length = 300, null = True, blank=True)
	permisoPorHora =  models.CharField(max_length = 45, null = True, blank=True)
	permisoPorDias = models.CharField(max_length = 45, null = True, blank=True)
	horaSalida = models.CharField(max_length = 45)
	fecha = models.DateField()

	def __str__(self):
		return self.horaSalida
#=================================================#


#======================PERSONA====================#
class Persona(models.Model):
	documentoIdentidad = models.CharField(max_length = 20, unique = True)
	nombres = models.CharField(max_length = 45)
	apellidos = models.CharField(max_length = 45)
	telefono = models.CharField(max_length = 10, null = True, blank = True)
	imgPerfil = models.ImageField(upload_to = 'img_perfil', null=True, blank=True)
	usuario = models.OneToOneField(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.nombres
#=================================================#

#==================PERSONA=PERMISO================#
class Permiso_persona(models.Model):
	est = (
			('En Espera', 'En Espera'),
			('Aprobado','Aprobado'),
			('Cancelado','Cancelado'), 
			('Rechazado','Rechazado'),
			('Finalizado','Finalizado'),
		)
	estado = models.CharField(max_length = 20,  choices=est)
	instructor = models.CharField(max_length = 100, null = True, blank=True)
	vigilante = models.CharField(max_length = 100, null = True, blank=True)
	permiso = models.ForeignKey(Permiso, on_delete = models.CASCADE)
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)

	def __str__(self):
		return self.persona.nombres+'_'+self.permiso.horaSalida+'_'+self.estado
#=================================================#

#=======================ROL=======================#
class Rol(models.Model):
	roles = (
			('APRENDIZ', 'APRENDIZ'),
			('INSTRUCTOR','INSTRUCTOR'),
			('ADMINISTRADOR','ADMINISTRADOR'), 
			('VIGILANTE','VIGILANTE'),
		)
	rol = models.CharField(max_length = 20, unique = True, choices=roles)

	def __str__ (self):
		return self.rol
#=================================================#

#====================ROL=PERSONA==================#
class Rol_persona(models.Model):
	rol = models.ForeignKey(Rol, on_delete = models.CASCADE)
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)

	def __str__(self):
		return self.persona.nombres+'_'+self.rol.rol
#=================================================#

#=====================PROGRAMA====================#
class Programa(models.Model):
	nombre = models.CharField(max_length = 100, unique = True)
	abreviacion = models.CharField(max_length = 30)

	def __str__(self):
		return self.nombre
#=================================================#

#======================FICHA======================#
class Ficha(models.Model):
	jornadas = (
		('Mañana', 'Mañana'),
		('Tarde', 'Tarde'),
		('Noche', 'Noche'),
		)
	numeroFicha = models.CharField(max_length = 20, unique = True)
	jornada = models.CharField(max_length = 20, choices = jornadas)
	ambiente = models.CharField(max_length = 50)
	lider = models.CharField(max_length = 100)
	fechaFinEtapaLectiva = models.DateField()
	programa = models.ForeignKey(Programa, on_delete = models.CASCADE)

	def __str__(self):
		return self.numeroFicha+' _ '+self.programa.nombre
#=================================================#

#===================PERSONA=FICHA=================#
class Persona_ficha(models.Model):
	persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
	ficha = models.ForeignKey(Ficha, on_delete = models.CASCADE)

	def __str__(self):
		return self.persona.nombres+'_'+self.ficha.numeroFicha
#=================================================# 