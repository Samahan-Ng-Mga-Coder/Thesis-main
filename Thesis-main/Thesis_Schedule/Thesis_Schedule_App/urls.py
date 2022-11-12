from django.urls import path
from . import views
urlpatterns = (
    path('', views.login, name='login_page'),
    path('admin_landingpage/', views.adminlogin, name='admin_landingpage'),
    path('user_info/', views.adminAddingUser, name='user_info')

)
