from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.Email(max_length=70)
	home_id=models.ForeignKey(Home,models.SET_NULL,blank=Ture,null=Ture)
	#M:M
	chores=models.ManyToManyField(Chroe,through='Schedule')

class Schedule(models.Model):
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
	chroe=models.ForeignKey(Chore,on_delete=models.CASCADE)
	time=models.DurationField()


class Home(models.Model):
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	manager=models.ForeignKey(Profile,models.SET_NULL,blank=Ture,null=Ture)
	def __str__(self):
		return self.name

class Chore(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=100)