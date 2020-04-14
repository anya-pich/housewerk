from django.contrib import admin
from .models import Chore, Profile, Home, Schedule

# Register your models here.
admin.site.register(Chore)
admin.site.register(Profile)
admin.site.register(Home)
admin.site.register(Schedule)