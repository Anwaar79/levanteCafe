from django.urls import path
from . import views

app_name='staff'

urlpatterns = [

    path('', views.staff_login, name="login"),
    path('Dashboard/<str:staff_name>/<int:staff_password>/', views.staff_view, name="view"),
    path('new_member/', views.staff_add, name="add"),
    path('update_user/<str:staff_name>/<int:staff_password>/', views.staff_update, name='update'),
    path('comment/',views.comments, name="comments"),
    path('Add_table/', views.table_add, name="table"),
    path('error/', views.staff_error, name="error"),

]