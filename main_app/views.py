from django.shortcuts import render, redirect
from .models import *
from  .forms  import *
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Class-Based Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


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

# def new_member(request):
# 	return render(request, 'group/invite.html')

def members_detail(request):
	return render(request, 'group/member/detail.html')

def members_edit(request):
	return render(request, 'group/member/edit.html')

def members_remove(request):
	return render(request, 'group/index.html')

# PROFILE

def profile_home(request):
	return render(request, 'profile/home.html')

def login(request):
	return render(request, 'registration/login.html')


# CHORES

def chores_index(request):
	chores = Chore.objects.all()
	return render(request, 'chores/index.html', {'chores': chores})

def new_chore(request):
	if request.method == 'POST':
		
		form = ChoreForm(request.POST)
		if form.is_valid():

			chore = form.save()
			print(chore.id)
			return redirect('detail', chore.id)
	else: 
		form = ChoreForm()
	context = {'form': form}
	return render(request, 'chores/chore_form.html', context)


def chores_update(request, chore_id):
	chore = Chore.objects.get(id =chore_id)

	if request.method == 'POST':
		form = ChoreForm(request.POST, instance = chore)
		if form.is_valid():
			chore = form.save()
			return redirect('detail', chore.id)
	else:
		form = ChoreForm(instance = chore)
		return render (request, 'chores/chore_form.html', {'form':form})

def chores_delete(request, chore_id):
	Chore.objects.get(id = chore_id).delete()
	return redirect('chores_index')

# class ChoreDetail(DetailView):
# 	model = Chore

# class ChoreUpdate(CreateView):
# 	model = Chore
# 	fields = ['name', 'description']

# class ChoreDelete(DeleteView):
# 	model = Chore
# 	success_url = '/chores/'

# class ChoreList(ListView):
# 	model = Chore

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
			#login(request,user)
			return redirect('home')
	else:
		error_message='Invalid sign up'
	form=UserCreationForm()
	profile_form=ProfileForm()
	context={'form':form,'p_form':profile_form,'error_message':error_message}
	return render(request,'profile/create.html',context)

def new_group(request):
	if request.method=='POST':
		form=HomeForm(request.POST)
		if form.is_valid():
			home=form.save(commit=False)
			home.manager=request.user.profile
			home.save()
			profile=request.user.profile
			profile.home_id=home
			profile.save()  #maybe have problem
			return redirect('group_index')#TODO:adjust group_index
	else:
		form=HomeForm()
	context={'form':form}
	return render(request,'group/create.html',context)

def group_invite(request):
	profiles=Profile.objects.filter(home_id=None)
	print(profiles)
	return render(request,'group/invite.html',{'profiles':profiles})

def group_invite_member(request,profile_id):
	profile=Profile.objects.get(id=profile_id)
	profile.home_id=request.user.profile.home_id
	profile.save()
	return  redirect('group_invite')

def group_index(request):
	profile=request.user.profile
	print(profile.home_id)
	if profile.home_id==None:
		home=None
		return render(request,'group/index.html',{'home':home})
	else:
		home=Home.objects.get(id=profile.home_id.id)
		return render(request,'group/index.html',{'home':home})

def  group_detail(request,home_id):
	if request.user.profile!=Home.objects.get(id=home_id).manager:
		#return redirect(request,'profile_home')
		return render(request,'profile/home.html')
	else:
		print('here')
		home=Home.objects.get(id=home_id)
		profiles=Profile.objects.filter(home_id=home_id)
		return render(request,'group/group_detail.html',{'home':home,'profiles':profiles})

def group_update(request,home_id):
	home=Home.objects.get(id=home_id)
	if(request.method=="POST"):
		form=HomeForm(request.POST,instance=home)
		if form.is_valid():
			home=form.save()
			return redirect('group_detail',home.id)
	else:
		form=HomeForm(instance=home)
	return render(request,'group/create.html',{'form':form})
