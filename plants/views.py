from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Plant
from .forms import PlantForm, EditForm
from datetime import date, timedelta
from django.db import IntegrityError


def check_plant_owner(owner, user):
    if owner != user:
        raise Http404


def index(request):
    """Front page"""
    return render(request, 'plants/index.html')


@login_required
def plants_list(request):
    plants = Plant.objects.filter(owner=request.user).order_by('name')
    context = {'plants': plants}
    return render(request, 'plants/list.html', context)


@login_required
def plant(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    check_plant_owner(plant.owner, request.user)

    context = {'plant': plant}
    return render(request, 'plants/plant.html', context)


@login_required
def plants_check_today(request):

    checks = get_plants_to_check(request)

    context = {'checks': checks}
    return render(request, 'plants/check.html', context)


@login_required
def new_plant(request):
    if request.method != 'POST':
        form = PlantForm()
    else:
        form = PlantForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                new_plant = form.save(commit=False)
                new_plant.owner = request.user
                new_plant.save()
                return redirect('plants:list')
            except IntegrityError:
                e = 'The name must be unique. Plant with this name already exists.'
                context = {'form': form, 'e': e}
                return render(request, 'plants/new_plant.html', context)

    context = {'form': form}
    return render(request, 'plants/new_plant.html', context)


@login_required
def edit(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    check_plant_owner(plant.owner, request.user)
    if request.method != 'POST':
        form = EditForm(instance=plant)
    else:
        form = EditForm(instance=plant, data=request.POST, files=request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('plants:plant', plant_id=plant.id)
            except IntegrityError:
                e = 'The name must be unique. Plant with this name already exists.'
                context = {'form': form, 'e': e}
                return render(request, 'plants/new_plant.html', context)

    context = {'plant': plant, 'form': form}
    return render(request, 'plants/edit.html', context)


@login_required
def delete(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    check_plant_owner(plant.owner, request.user)
    if request.method == 'POST':
        plant.delete()
        return redirect('plants:list')

    context = {'plant': plant}
    return render(request, 'plants/delete.html', context)


@login_required
def watering(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    check_plant_owner(plant.owner, request.user)
    if request.method == 'POST':
        plant.watering_date = date.today()
        plant.save()
        return redirect('plants:list')

    context = {'plant': plant, 'url_name': 'plants:list'}
    return render(request, 'plants/watering.html', context)


@login_required
def today_watering(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    check_plant_owner(plant.owner, request.user)
    if request.method == 'POST':
        plant.watering_date = date.today()
        plant.save()
        return redirect('plants:check')

    context = {'plant': plant, 'url_name': 'plants:check'}
    return render(request, 'plants/watering.html', context)


@login_required
def watering_all(request):
    plants = get_plants_to_check(request)

    if request.method == 'POST':
        for plant in plants:
            plant.watering_date = date.today()
            plant.save()
        return redirect('plants:check')

    context = {'plants': plants}
    return render(request, 'plants/watering_all.html', context)


def get_plants_to_check(request):
    today = date.today()
    if 4 <= today.month <= 9:
        regularly_list = Plant.objects.filter(owner=request.user).filter(watering_frequency='REG'). \
            filter(watering_date__lte=today - timedelta(days=3))
        infrequently_list = Plant.objects.filter(owner=request.user).filter(watering_frequency='INF'). \
            filter(watering_date__lte=today - timedelta(days=7))
    else:
        regularly_list = Plant.objects.filter(owner=request.user).filter(watering_frequency='REG'). \
            filter(watering_date__lte=today - timedelta(days=7))
        infrequently_list = Plant.objects.filter(owner=request.user).filter(watering_frequency='INF'). \
            filter(watering_date__lte=today - timedelta(days=15))
    plants = regularly_list.union(infrequently_list)
    return plants