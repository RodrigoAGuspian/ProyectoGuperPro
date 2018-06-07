from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

# URLS
urlpatterns = [
#=======================INDEX=====================#
    path('', login_required(view_index), name = 'url_index'),
#=================================================#

#=======================FICHAS====================#
	path('lista_fichas/', login_required(view_lista_fichas), name = 'url_lista_fichas'),
	#AGREGAR FICHA
	path('agregar_ficha/', login_required(view_agregar_ficha), name = 'url_agregar_ficha'),

	path('agregar_persona_ficha/', login_required(view_agregar_persona_ficha), name = 'url_agregar_persona_ficha'),
	#EDITAR FICHA
	path('editar_ficha/<int:id_ficha>/', login_required(view_editar_ficha), name = 'url_editar_ficha'),
	#ELIMINAR FICHA
	path('eliminar_ficha/<int:id_ficha>/', login_required(view_eliminar_ficha), name = 'url_eliminar_ficha'),
#=================================================#

#======================PERMISOS===================#
	path('lista_permisos/', login_required(view_lista_permisos), name = 'url_lista_permisos'),
#=================================================#

#=================================================#

#======================PERSONAS===================#
	
	#AGREGAR ADMINISTRADOR
	path('agregar_admin/', login_required(view_agregar_administrador), name="url_agregar_admin"),
	
	#LISTA INSTRUCTORES
	path('lista_instructores/',login_required(view_lista_instructores), name='url_lista_instructores'),
	#AGREGAR INSTRUCTOR
	path('agregar_instructor/',login_required(view_agregar_instructor), name='url_agregar_instructor'),
	#Editar INSTRUCTOR
	path('editar_instructor/<int:id_instructor>/', login_required(view_editar_instructor), name='url_editar_instructor'),
	#eliminar INSTRUCTOR
	path('eliminar_instructor/<int:id_instructor>/', login_required(view_eliminar_instructor), name='url_eliminar_instructor'),

	#LISTA VIGILANTES
	path('lista_vigilantes/', login_required(view_lista_vigilantes), name= 'url_lista_vigilantes'),
	#AGREGAR VIGILANTE
	path('agregar_vigilante/',login_required(view_agregar_vigilante), name='url_agregar_vigilante'),
	#EDITAR VIGILANATE
	path('editar_vigilante/<int:id_vigilante>/', login_required(view_editar_vigilante), name= 'url_editar_vigilante'),
	#ELIMINAR VIGILANTE
	path('eliminar_vigilante/<int:id_vigilante>/', login_required(view_eliminar_vigilante), name= 'url_eliminar_vigilante'),

	#ListA aprendiCES
	path('lista_aprendices/', login_required(view_lista_aprendices), name='url_lista_aprendices'),
	#Agregar aprendiz
	path('agregar_aprendiz/', login_required(view_agregar_aprendiz), name = 'url_agregar_aprendiz'),
	#Editar Aprendiz
	path('editar_aprendiz/<int:id_aprendiz>/', login_required(view_editar_aprendiz), name='url_editar_aprendiz'),
	#eliminar Aprendiz
	path('eliminar_aprendiz/<int:id_aprendiz>/', login_required(view_eliminar_aprendiz), name='url_eliminar_aprendiz'),
	#Cargar Excel
	path('agregar_aprendiz_excel/', login_required(view_agregar_aprendiz_excel), name='url_agregar_aprendiz_excel'),
	#REGISTROS_EXCEL
	path('registros_excel/', login_required(cargar_excel), name = 'url_registros_excel'),
#=================================================#

#====================PROGRAMAS====================#
	path('lista_programas', login_required(view_lista_programas), name = 'url_lista_programas'),
	#AGREGAR PROGRAMA 
	path('agregar_programa/', login_required(view_agregar_programa), name='url_agregar_programa'),
	#EDITAR PROGRAMA 
	path('editar_programa/<int:id_programa>/', login_required(view_editar_programa), name='url_editar_programa'),
	#ELIMINAR PROGRAMA 
	path('eliminar_programa/<int:id_programa>/', login_required(view_eliminar_programa), name='url_eliminar_programa'),
#=================================================#

#=====================USUARIOS====================#
	path('usuario/index/', login_required(view_usuario), name = 'url_usuarios'),
#=================================================#

#=====================ROLES=======================#
	#Listar rol
	path('lista_roles', login_required(view_lista_roles), name = 'url_lista_roles'),
	#Agregar rol
	path('agregar_rol/',login_required(view_agregar_rol), name='url_agregar_rol'),
	#Agregar rol automaticamente
	path('agregar_rol_auto/<str:rol>/',login_required(view_agregar_rol_automatic), name='url_agregar_rol_auto'),
	#Editar rol
	path('editar_rol/<int:id_rol>/',login_required(view_editar_rol), name='url_editar_rol'),
	#Eliminar rol
	path('eliminar_rol/<int:id_rol>/',login_required(view_eliminar_rol), name='url_eliminar_rol'),
#=================================================#

#=====================LOGIN=======================#
	path('accounts/login/', view_login, name = 'url_login'),
	path('accounts/login_superuser/', view_login_superuser, name = 'url_login_superuser'),
	#LOGOUT
	path('logout/', login_required(view_logout), name = 'url_logout'),
#=================================================#

#================GENERAR=REPORTES==================#
	path('reporte_ficha/', reporte_ficha, name = 'url_reporte_ficha'),
	path('reporte_aprendiz/', reporte_aprendiz, name = 'url_reporte_aprendiz'),
#=================================================#

#=====================PERFIL======================#
	path('perfil/<int:id_persona>/', view_perfil, name = 'url_persona_perfil'),
#=================================================#
#===================VIEW=FICHA====================#
	path('view_ficha/<int:id_ficha>/', view_ficha, name = 'url_view_ficha'),
#=================================================#


#================================================================================================================================

#==================Peticiones de salida===========#
	path('peticiones_salida/', view_peticiones, name = 'url_peticiones'),
	path('ver_peticion/<int:id_pet>/', view_ver_peticion, name = 'url_ver_peticion'),
	path('aprobar_peticion/<int:id_pet>/', view_aprobar_peticion, name = 'url_aprobar_peticion'),
	path('rechazar_peticion/<int:id_pet>/', view_rechazar_peticion, name = 'url_rechazar_peticion'),
]
