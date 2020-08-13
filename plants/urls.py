from django.urls import path
from . import views
from .models import Plant

app_name = 'plants'
urlpatterns = [
    path('main/', views.index, name='index'),
    path('main/list/', views.plants_list, name='list'),
    path('main/check/', views.plants_check_today, name='check'),
    path('main/new_plant/', views.new_plant, name='new_plant'),
    path('main/list/<int:plant_id>/', views.plant, name='plant'),
    path('main/list/edit/<int:plant_id>/', views.edit, name='edit'),
    path('main/list/delete/<int:plant_id>/', views.delete, name='delete'),
    path('main/list/watering/<int:plant_id>/', views.watering, name='watering'),
    path('main/check/watering/<int:plant_id>/', views.today_watering, name='today_watering'),
    path('main/check/watering_all/', views.watering_all, name='watering_all'),
]