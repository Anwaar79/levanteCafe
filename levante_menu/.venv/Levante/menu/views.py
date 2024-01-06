from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse
from .forms import MenuForm
from itertools import groupby
from operator import attrgetter


def menu_list(request):
    menu_items = Item.objects.order_by('Food_Item_Type')
    grouped_items = groupby(menu_items, attrgetter('Food_Item_Type'))
    grouped_data = [(key, list(group)) for key, group in grouped_items]
    return render(request, 'menu.html', {'grouped_data': grouped_data})

def menu_add(request):
  form= MenuForm()
  if request.method  == 'POST':
    form= MenuForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('menu:list')
    else:
        print(form.errors)
  return render(request, 'menu_add.html', {'form': form})


def menu_update(request,  item_id):
   menu= Item.objects.get(item_id =item_id)
   form= MenuForm(instance= menu)
   if request.method  == 'POST':
    form= MenuForm(request.POST, request.FILES, instance=menu)
    if form.is_valid():
      form.save()
      return redirect('menu:list')
   else:
        print(form.errors)
   return render(request, 'menu_update.html', {'menu': menu, 'form': form})


def menu_delete(request,  item_id):
   menu= Item.objects.get(item_id =item_id)
   if request.method  == 'POST':
     menu.delete()
     return redirect('menu:list')
   return render(request, 'menu_delete.html')

