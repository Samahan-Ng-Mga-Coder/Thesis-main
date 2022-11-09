from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):
    return render(request, 'Thesis_Schedule_App/loginpage.html')


def adminlogin(request):
    # q = request.GET.get('q')

    return render(
        request, 'Thesis_Schedule_App/admin_landingpage.html')
def adminaddingUser(request):
    # q = request.GET.get('q')

    return render(
        request, 'Thesis_Schedule_App/Userinfo.html')