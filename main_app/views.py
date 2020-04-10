from django.shortcuts import render, redirect
from .models import *
from  .forms  import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Class-Based Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Housemate, Chore
# Import forms after they're created


# Create your views here.
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def chores_index(request):
	chores = Chore.objects.all()
	return render(request, 'chores/index.html', {'chores': chores})

# def chores_detail(request, chore_id):
# 	chore = Chore.objects.get(id = chore_id)

# 	return render(request, )

def new_member(request):
	error_message=''
	if  request.method=='POST':
		form=UserCreationForm(request.POST)
		profile_form=ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			login(request,user)
			return redirect('home')
		else:
			error_message='Invalid sign up'
		form=UserCreationForm()
		profile_form=ProfileForm()
		context={'form':form,'p_form':profile_form,'error_message':error_message}
		return render(request,'profile/create.html',context)

