from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Chore(models.Model):
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=250)
	def __str__(self):
		return self.name

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	email=models.EmailField(max_length=70)
	home_id=models.ForeignKey('Home',models.SET_NULL,blank=True,null=True)
	#M:M
	chores=models.ManyToManyField(Chore,through='Schedule')
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

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




