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
    path('group/<int:home_id>/chores',views.group_chores,name='group_chores'),
    path('group/<int:home_id>/chores/<int:chore_id>',views.group_chore_assoc,name='group_chore_assoc'),
    
    # HOUSEMATES
    path('group/members', views.members_index, name ='members_index'),
    path('group/member/new/', views.new_member, name ='new_member'),
   # path('group/member/<int:member_id>/', views.members_detail, name ='detail'),

    path('group/member/<int:profile_id>/<int:home_id>', views.members_detail, name ='member_detail'),
    path('group/member/<int:member_id/edit/', views.members_edit, name = 'members_edit'),
    path('group/member/<int:member_id/remove', views.members_remove, name ='members_remove'),
    path('group/member/assoc_chore/<int:profile_id>/<int:chore_id>',views.assoc_member_chore,name='assoc_member_chore'),




    # PROFILE
    path('profile/', views.profile_home, name='profile_home'),
    path('profile/view', views.profile_view, name='profile_view'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/<int:profile_id>/delete', views.profile_delete, name='profile_delete'),

    # CHORES
    path('chores/', views.chores_index, name = 'chores_index'),
    # path('chores/<int:chore_id>/update', views.chores_update, name ='chores_update'),
    # path('chores/<int:chore_id>/delete', views.chores_delete, name ='chores_delete'),
    # path('chores/index', views.ChoreList.as_view(), name = 'chores_index'),
    path('chores/<int:pk>/', views.ChoreDetail.as_view(), name = 'chores_detail'),
    path('chores/create/', views.ChoreCreate.as_view(), name ='chores_create'),
    path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name ='chores_update'),
    path('chores/<int:pk>/delete', views.ChoreDelete. as_view(), name ='chores_delete'),

    # PROFILE LOGIN URLs AUTOMATICALLY CREATED BY DJANGO
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete']
    
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/group', views.associate_group, name='associate_group'),
    path('accounts/signup/group/new', views.create_group, name='create_group'),

]