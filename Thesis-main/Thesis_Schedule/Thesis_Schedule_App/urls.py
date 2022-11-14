from django.urls import path
from . import views
urlpatterns = {
    path('', views.login, name='login_page'),
    path('admin_landingpage/', views.adminlogin, name='admin_landingpage'),
    #path('Userinfo/', views.adminAddingUser, name='Userinfo'),

    # path('practice_only/', views.practice, name='practice_only')

}
