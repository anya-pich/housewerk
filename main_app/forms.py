from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class ChoreForm(ModelForm):
	class Meta:
		model = Chore
		fields = ('name', 'description')

class ProfileForm(ModelForm):
	class Meta:
		model=Profile
		fields=['email']

class HomeForm(ModelForm):
	class Meta:
		model=Home
		fields=['name','address']

class GroupIdForm(forms.Form):
	group_id = forms.IntegerField(help_text="Enter group code here - just numbers please.")

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
