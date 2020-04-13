from django.urls import path
from . import views

urlpatterns = [
    # General Pages
    path('', views.home, name ='home'),
    path('about/', views.about, name ='about'),

    # GROUP
    path('group/', views.group_index, name ='group_index'),
    path('group/new',views.new_group,name='new_group'),
    path('group/invite',views.group_invite,name='group_invite'),
    path('group/invite/<int:profile_id>',views.group_invite_member,name='group_invite_member'),
    path('group/detail/<int:home_id>',views.group_detail,name='group_detail'),
    path('group/<int:home_id>/edit',views.group_update,name='group_update'),
    
    # HOUSEMATES
    path('group/members', views.members_index, name ='members_index'),
    path('group/member/new/', views.new_member, name ='new_member'),
    path('group/member/<int:member_id>/', views.members_detail, name ='detail'),
    path('group/member/<int:member_id/edit/', views.members_edit, name = 'members_edit'),
    path('group/member/<int:member_id/remove', views.members_remove, name ='members_remove'),

    # PROFILE
    path('profile/<int:profile_id>/', views.profile_home, name='profile_home'),
    path('login/', views.login, name='login'),
    path('profile/<int:profile_id>/view', views.profile_view, name='profile_view'),
    path('profile/<int:profile_id>/edit', views.profile_edit, name='profile_edit'),
    path('profile/<int:profile_id>/delete', views.profile_delete, name='profile_delete'),

    # CHORES
    path('chores/', views.chores_index, name = 'chores_index'),
    # path('chores/', views.ChoreList.as_view(), name = 'chores_index'),
    # path('chores/<int:pk>/', views.ChoreDetail.as_view(), name = 'chores_detail'),
    # path('chores/create/', views.ChoreCreate.as_view(), name ='chores_create'),
    # path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name ='chores_update'),
    # path('chores/<int:pk>/remove', views.ChoreRemove. as_view(), name ='chores_remove'),

]