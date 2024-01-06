from django.urls import path
from . import views
app_name='costumers'
urlpatterns = [
    path('', views.costumer_view, name="view")
]