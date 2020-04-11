from django.forms import ModelForm
from .models import *

class ChoreForm(ModelForm):
	class Meta:
		model = Chore
		fields = ('name', 'description')

class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields=['email']
		