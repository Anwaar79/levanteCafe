from django.shortcuts import render, redirect
from .models import Order
from order.forms import OrderForm


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order.html', {'orders': orders})

def order_detail(request,  order_id):
  order = Order.objects.get( order_id=order_id)
  return render(request, 'order_detail.html', {'order': order})

def order_add(request): 
   form = OrderForm() 
   if request.method =='POST':
    form= OrderForm(request.POST)
    if form.is_valid():
     form.save()
     return redirect('orders:list')
   return render(request, 'order_add.html', {'form':form})



def order_update(request, order_id):
    order = Order.objects.get(order_id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:list')
    else:
        form = OrderForm(instance=order)
    
    context = {
        'form': form
    }
    
    return render(request, 'order_update.html', context)


def order_delete(request,  order_id):
 order = Order.objects.get(order_id=order_id)
 if request.method =='POST':
    order.delete()
    return redirect('orders:list')
 return render(request, 'order_delete.html')

