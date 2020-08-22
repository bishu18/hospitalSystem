"""hospitalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    # path('showthis/', showthis, name='showthis'),
    path('contact/', contact, name='contact'),
    path('login_staff/', login_staff, name='login_staff'),
    path('login_admin/', login_admin, name='login_admin'),
    path('login_doctor/', login_doctor, name='login_doctor'),
    path('staff_home/', staff_home, name='staff_home'),
    path('admin_home/', admin_home, name='admin_home'),
    path('patient_graph/', patient_graph, name='patient_graph'),
    path('doctor_view/', doctor_view, name='doctor_view'),
    path('doctor_add/', doctor_add, name='doctor_add'),
    path('doctor_delete(?D<int:did>)/', doctor_delete, name='doctor_delete'),
    path('branch_view/', branch_view, name='branch_view'),
    path('branch_add/', branch_add, name='branch_add'),
    path('branch_delete(?D<int:bid>)/', branch_delete, name='branch_delete'),
    path('staff_view/', staff_view, name='staff_view'),
    path('staff_add/', staff_add, name='staff_add'),
    path('staff_delete(?D<int:sid>)/', staff_delete, name='staff_delete'),
    path('patient_add/', patient_add, name='patient_add'),
    path('patient_view/', patient_view, name='patient_view'),
    path('patient_delete(?D<int:pid>)/', patient_delete, name='patient_delete'),
    path('logout_admin/', Logout_admin, name='logout_admin'),
    path('logout_doctor/', Logout_doctor, name='logout_doctor'),
    path('logout_staff/', Logout_staff, name='logout_staff'),
    path('profile/', profile, name='profile'),
    path('', index, name='index'),
    path('patient_list/', patient_list, name='patient_list'),
]
