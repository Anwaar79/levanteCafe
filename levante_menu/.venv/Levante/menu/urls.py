from django.urls import path
from . import views

app_name= 'menu'

urlpatterns = [
    path('', views.menu_list, name="list"),
    path('add_item/', views.menu_add, name= "add"),
    path('delete_item/<int:item_id>/', views.menu_delete, name= "delete"),
    path('update_item/<int:item_id>/', views.menu_update, name= "update")
]
