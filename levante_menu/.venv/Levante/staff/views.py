from django.shortcuts import render, redirect
from .models import User
from .forms import StaffLoginForm, StaffUpdateForm
from django.shortcuts import get_object_or_404
from costumer.models import Contact
from table.forms import TableForm


def staff_login(request):
    form = StaffLoginForm() 
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            staff_name = form.data['staff_name']
            staff_password= form.data['staff_password']
            return redirect('staff:view', staff_name=staff_name, staff_password=staff_password)
    
    return render(request, 'login.html', {'form': form})

def staff_error(request):
    return render(request, 'error.html')
           

def staff_view(request, staff_name, staff_password):
    user = User.objects.get(staff_name=staff_name, staff_password=staff_password)
    context = {
        'user': user
    }
    return render(request, 'staff.html', context)


def staff_add(request):
    form = StaffLoginForm()
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            form.save()
            staff_name = form.cleaned_data['staff_name']  
            staff_password = form.cleaned_data['staff_password']  
            return redirect('staff:view', staff_name=staff_name, staff_password=staff_password)
    return render(request, 'staff_add.html', {'form': form})


def staff_update(request, staff_name, staff_password):
    user = get_object_or_404(User, staff_name=staff_name, staff_password=staff_password)
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('staff:view', staff_name=staff_name, staff_password=staff_password)
    else:
        form = StaffUpdateForm(instance=user)
    
    context = {
        'form': form
    }
    
    return render(request, 'staff_update.html', context)

def comments(request):
    comments = Contact.objects.all()
    return render(request, 'costumer_comments.html', {'comments': comments})

def table_add(request):
  form= TableForm()
  if request.method  == 'POST':
    form= TableForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('staff:login')
    else:
        print(form.errors)
  return render(request, 'add_table.html', {'form': form})