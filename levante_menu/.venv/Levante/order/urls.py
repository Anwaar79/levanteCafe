from django.urls import path
from . import views

app_name='orders'

urlpatterns = [
    path('', views.order_list, name="list"),
    path('order_detail/<int:order_id>/', views.order_detail, name="order_detail"),
    path('order_add/', views.order_add, name="add"),
    path('order_delete/<int:order_id>/', views.order_delete),
    path('order_update/<int:order_id>/', views.order_update)

]