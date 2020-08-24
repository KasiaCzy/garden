from django.urls import path
from . import views

app_name = 'plants'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.plants_list, name='list'),
    path('check/', views.plants_check_today, name='check'),
    path('new_plant/', views.new_plant, name='new_plant'),
    path('list/<int:plant_id>/', views.plant, name='plant'),
    path('edit/<int:plant_id>/', views.edit, name='edit'),
    path('delete/<int:plant_id>/', views.delete, name='delete'),
    path('list/watering/<int:plant_id>/', views.watering, name='watering'),
    path('check/watering/<int:plant_id>/', views.today_watering, name='today_watering'),
    path('check/watering_all/', views.watering_all, name='watering_all'),
]