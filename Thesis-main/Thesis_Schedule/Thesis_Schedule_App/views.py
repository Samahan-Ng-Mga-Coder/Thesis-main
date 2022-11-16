from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login(request):

    return render(request, 'Registration/login_page.html')

def adminlogin(request):


    return render(request, 'Thesis_Schedule_App/admin_landingpage.html')


def adminAddingUser(request):
    # q = request.GET.get('q')
    return render(request, 'Thesis_Schedule_App/Userinfo.html')

    #return render(request, 'Thesis_Schedule_App/admin_landingpage.html')



