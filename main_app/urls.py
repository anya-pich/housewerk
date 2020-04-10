from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),


    # General Pages
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),

    # GROUP
    path('group/', views.groups_index, name ='groups_index')
    
    # HOUSEMATES
    path('group/member', views.members_index, name ='index'),
    path('group/member/new/', views.new_member, name ='new_member'),
    path('group/member/<int:member_id>/', views.members_detail, name ='detail'),
    path('group/member/<int:member_id/edit/', views.members_edit, name = 'members_edit'),
    path('group/member/<int:member_id/remove', views.members_remove, name ='members_remove'),

    # CHORES
    path('chores/', views.ChoreList.as_view(), name = 'chore_index'),
    path('chores/<int:pk>/', views.ChoreDetail.as_view(), name = 'chores_detail'),
    path('chores/create/', views.ChoreCreate.as_view(), name ='chores_create'),
    path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name ='chores_update')
    path('chores/<int:pk>/remove', views.ChoreRemove. as_view(), name ='chores_remove')

]