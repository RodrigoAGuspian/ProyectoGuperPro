from django.urls import path, include
from rest_framework import routers
from AppSena.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'user', user_viewset)
router.register(r'persona', persona_viewset)
router.register(r'actulizar_perfil', actualizar_perfil_viewset)
router.register(r'ver_permisos', ver_permisos_viewset)

router.register(r'solicitar_permiso', solicitar_permiso_viewset)
router.register(r'aprendiz_permiso', aprendiz_permiso_viewset)


urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
	path('rest-auth/', include('rest_auth.urls')),
	path('rest-auth/registration/', include('rest_auth.registration.urls')),
]