from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def home(request):
    return redirect('/shows')

def index(request):
    context = {
        "shows_list" : Shows.objects.all(),
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def add_show(request):
    errors=Shows.objects.validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')

    if request.method =="POST":
        Shows.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['date'], description=request.POST['desc'])
    return redirect('/')

def edit(request, id):
    context = {
        "show" : Shows.objects.get(id=id),
    }
    return render(request, 'edit_show.html', context)

def edit_show(request, id):
    errors=Shows.objects.validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/{id}/edit')

    if request.method == "POST":
        show = Shows.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.description = request.POST['desc']
        show.save()        
    return redirect('/')

def delete_show(request, id):
    Shows.objects.get(id=id).delete()
    return redirect('/')

def show_info(request, id):
    context = {
        "show" : Shows.objects.get(id=id),
    }
    return render(request, 'show_info.html', context)