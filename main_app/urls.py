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
    path('profile/', views.profile_home, name='profile_home'), # temp for testing html
    path('login/', views.login, name='login'),

    # CHORES
    path('chores/', views.chores_index, name = 'chores_index'),
    # path('chores/<int:chore_id>/update', views.chores_update, name ='chores_update'),
    # path('chores/<int:chore_id>/delete', views.chores_delete, name ='chores_delete'),
    # path('chores/index', views.ChoreList.as_view(), name = 'chores_index'),
    path('chores/<int:pk>/', views.ChoreDetail.as_view(), name = 'chores_detail'),
    path('chores/create/', views.ChoreCreate.as_view(), name ='chores_create'),
    path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name ='chores_update'),
    path('chores/<int:pk>/delete', views.ChoreDelete. as_view(), name ='chores_delete'),

]