from django.shortcuts import render, redirect
from app.forms import usuarioForm
from app.models import usuario
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    #all = usuario.objects.all()
    search = request.GET.get('search')
    if search:
        data['db'] = usuario.objects.filter(nome__icontains=search)
    else:
        data['db'] = usuario.objects.all()
    """"
    pagination = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = pagination.get_page(pages)"""
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = usuarioForm()
    return render(request, 'form.html', data)

def create(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = usuario.objects.get(pk=pk)
    data['form'] = usuarioForm(instance=data['db'])
    return render(request, 'form.html', data)
"""
def update(request, pk):
    return render(request, 'index.html')
"""

def update(request, pk):
    data = {}
    data['db'] = usuario.objects.get(pk=pk)
    form = usuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = usuario.objects.get(pk=pk)
    db.delete()
    return redirect('home')


