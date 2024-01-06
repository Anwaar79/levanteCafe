from django.shortcuts import render, redirect

# Create your views here.
def costumer_view(request):
    return redirect('home')
    return render(request, 'costumer.html')




