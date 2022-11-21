from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.adminlogin, name='login_page'),
    path('admin_landingpage', views.adminlogin, name='admin_landingpage'),
    path('facultyloading', views.facultyloading, name='facultyloading'),
    path('classschedule', views.classschedule, name='classschedule'),
    path('homePage', views.homePage, name='homePage'),

    #path('Userinfo/', views.adminAddingUser, name='Userinfo'),

    # path('practice_only/', views.practice, name='practice_only')

]
