from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('staff-list/', views.staff_list, name='staff_list'),
    path('attendance-create/', views.attendance_create, name='attendance_create'),
]