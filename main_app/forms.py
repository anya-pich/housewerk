import django import forms 
from .model import Chore, Housemate

class ChoreForm(forms.ModelForm):
	class Meta:
		model = Chore
		fields = ('name', 'description')
