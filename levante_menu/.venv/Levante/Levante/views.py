from django.shortcuts import render, redirect
from menu.models import Item
from costumer.forms import ContactForm
from itertools import groupby
from operator import attrgetter


def home(request):
    menu = Item.objects.all()
    return render(request, 'hompage.html', {'menu':menu})

def about(request):
    return render(request, 'about.html')
    
def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)

    context = {'form': form}  # Add the form object to the context
    return render(request, 'contact.html', context)
  
def menu(request):
    menu_items = Item.objects.order_by('Food_Item_Type')
    grouped_items = groupby(menu_items, attrgetter('Food_Item_Type'))
    grouped_data = [(key, list(group)) for key, group in grouped_items]
    return render(request, 'costumer_menu.html', {'grouped_data': grouped_data})

