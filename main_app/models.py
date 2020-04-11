from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chore(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=100)

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField(max_length=70)
	home_id=models.ForeignKey('Home',models.SET_NULL,blank=True,null=True)
	#M:M
	chores=models.ManyToManyField(Chore,through='Schedule')

class Home(models.Model):
	name=models.CharField(max_length=50)
	address=models.CharField(max_length=100)
	manager=models.ForeignKey(Profile,models.SET_NULL,blank=True,null=True)
	#M:M
	chores=models.ManyToManyField(Chore)
	def __str__(self):
		return self.name


class Schedule(models.Model):
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
	chroe=models.ForeignKey(Chore,on_delete=models.CASCADE)
	time=models.DurationField()
	Mark=models.BooleanField(default=False)




