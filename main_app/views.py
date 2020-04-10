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

# GROUP

def group_index(request):
  return render(request, 'group/index.html')

# HOUSEMATES

def members_index(request):
  return render(request, 'group/index.html')

def new_member(request):
	return render(request, 'group/invite.html')

def members_detail(request):
	return render(request, 'group/member/detail.html')

def members_edit(request):
	return render(request, 'group/member/edit.html')

def members_remove(request):
	return render(request, 'group/index.html')

# def (request):
# 	return render(request, '.html')

# def (request):
# 	return render(request, '.html')


# CHORES

# def chores_index(request):
# 	chores = Chore.objects.all()
# 	return render(request, 'chores/index.html', {'chores': chores})

# def chores_detail(request):
# 	return render(request, 'chores/detail.html')

# def chores_create(request):
# 	return render(request, 'chores/add.html')

# def chores_update(request):
# 	return render(request, 'chores/edit.html')

# def chores_remove(request):
# 	return render(request, 'chores/index.html')

# def chores_detail(request, chore_id):
# 	chore = Chore.objects.get(id = chore_id)

# 	return render(request, )


