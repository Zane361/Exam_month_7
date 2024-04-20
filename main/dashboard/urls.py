from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    # ----- AUTHENTICATION -----
    path('login/', views.log_in , name='login'),
    path('logout/', views.log_out , name='logout'),
    # ----- PROFILE -----
    path('profile-edit/', views.profile_edit, name='profile_edit'),
    # ----- STAFF -----
    path('staff-create/', views.staff_create , name='staff_create'),
    path('staff-list/', views.staff_list , name='staff_list'),
    path('staff-detail/<int:id>/', views.staff_detail , name='staff_detail'),
    path('staff-update/<int:id>/', views.staff_update , name='staff_update'),
    path('staff-delete/<int:id>/', views.staff_delete , name='staff_delete'),
    # ----- ATTENDANCE -----
    path('attendance-list/', views.attendance_list , name='attendance_list'),
]