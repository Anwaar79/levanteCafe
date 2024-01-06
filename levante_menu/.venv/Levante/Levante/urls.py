from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('menu/', include('menu.urls')),
    path('staff/', include('staff.urls')),
    path('orders/', include('order.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('costumer_menu/', views.menu, name='menu'),
    path('costumer/', include('costumer.urls')),
] 
