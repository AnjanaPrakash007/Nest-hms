from django.urls import path
from . import views

urlpatterns = [
    path('register/admin/', views.admin_registration, name='admin_registration'),
    path('register/student/', views.student_registration, name='student_registration'),
    # path('login/', views.login_view, name='login_view'),
    # path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    # path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
]
