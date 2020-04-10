from django.forms import ModelForm
from .model import *

class ChoreForm(forms.ModelForm):
	class Meta:
		model = Chore
		fields = ('name', 'description')

class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields=['email']
		