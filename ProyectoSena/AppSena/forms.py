from django import forms
from django.contrib.auth.models import User
from .models import *
from datetime import datetime, date

##----------------------------------------------------------------##
TOPIC_CHOICES = (
			('APRENDIZ', 'APRENDIZ'),
			('INSTRUCTOR','INSTRUCTOR'),
			('ADMINISTRADOR','ADMINISTRADOR'), 
			('VIGILANTE','VIGILANTE'),
)

class elegir_rol_aprendiz_form(forms.Form):
	rol = forms.ChoiceField(widget = forms.Select(), choices=TOPIC_CHOICES, initial='APRENDIZ', required=True, disabled = True)

class elegir_rol_instructor_form(forms.Form):
	rol = forms.ChoiceField(widget = forms.Select(), choices=TOPIC_CHOICES, initial='INSTRUCTOR', required=True, disabled = True)

class elegir_rol_admin_form(forms.Form):
	rol = forms.ChoiceField(widget = forms.Select(), choices=TOPIC_CHOICES, initial='ADMINISTRADOR', required=True, disabled = True)

class elegir_rol_vigilante_form(forms.Form):
	rol = forms.ChoiceField(widget = forms.Select(), choices=TOPIC_CHOICES, initial='VIGILANTE', required=True, disabled = True)
##---------------------------------------------------------------##

class agregar_programa_form(forms.ModelForm):
	class Meta:
		model = Programa
		fields = '__all__'

class login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())
	contraseña = forms.CharField(widget = forms.PasswordInput(render_value = True))
class agregar_rol_form(forms.ModelForm):
	class Meta:
		model= Rol 
		fields= '__all__'

class agregar_ficha_form(forms.ModelForm):
	class Meta:
		model = Ficha
		fields = '__all__'

		widgets={
			'fechaFinEtapaLectiva': forms.TextInput(attrs ={'placeholder': 'dd/MM/AAAA'})
		}

class agregar_persona_ficha_form(forms.ModelForm):
	class Meta:
		model = Persona_ficha
		fields = '__all__'

		labels={
			'persona':'aprendiz',
		}

##---------------------------------------------------------##
#        REGISTRAR VIGILANTE, APRENDIZ, INSTRUCTOR          #
class agregar_persona_form(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude=('usuario',)
#agregar user a APRENDEIZ, INSTRUCTOR y ADMIN
class agregar_user_form(forms.ModelForm):
	class Meta:
		model= User
		fields=['email']

		labels={
			'email':'Correo Electronico',
		}

		widgets = {
			'email': forms.TextInput(attrs ={'placeholder': 'alguien@misena.edu.co'})
		}

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if not 'misena.edu.co' in email:
			raise forms.ValidationError('Debes ingresar un correo misena. alguien@misena.edu.co')

		return email

class agregar_user_vigilante_form(forms.ModelForm): #agregar user a VIGILANTE
	class Meta:
		model= User
		fields=['email']

		labels={
			'email':'Correo Electronico',
		}

class editar_user_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email']

		labels={
			'email':'Correo Electronico',
		}
##-------------------------------------------------------------##

class elegir_ficha_form(forms.ModelForm):
	class Meta:
		model = Persona_ficha
		fields = ['ficha']
##-------------------------------------------------------------##
class cargar_excel_form(forms.Form):
	docfile = forms.FileField(label='Selecciona un archivo')
#============================================
	