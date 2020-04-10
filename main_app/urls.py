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

    # HOUSEMATES
    path('housemates/', views.housemates_index, name ='index'),
    path('housemates/new/', views.new_housemate, name ='new_housemate'),
    path('housemates/<int:housemate_id>/', views.housemates_detail, name ='detail'),
    path('housemates/<int:housemate_id/edit/', views.housemates_update, name = 'housemates_update'),
    path('housemates/<int:housemate_id/delete', views.housemates_delete, name ='housemates_delete'),

    # CHORES
    path('chores/', views.ChoreList.as_view(), name = 'chores_index'),
    path('chores/<int:pk>/', views.ChoreDetail.as_view(), name = 'chores_detail'),
    path('chores/create/', views.ChoreCreate.as_view(), name ='chores_create'),
    path('chores/<int:pk>/update', views.ChoreUpdate.as_view(), name ='chores_update')
    path('chores/<int:pk>/delete', views.ChoreDelete. as_view(), name ='chores_delete')


]