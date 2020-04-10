from django.shortcuts import render, redirect

# Class-Based Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Profile, Chore
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


