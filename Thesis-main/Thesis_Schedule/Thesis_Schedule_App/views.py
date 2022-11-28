from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user
from django.shortcuts import render, redirect
from .forms import ProfessorForm
from .models import Professor

# Create your views here.
from django.template import context


def adminlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'Thesis_Schedule_App/admin_landingpage.html')
        else:
            messages.error(request, "There Was an Error Logging In, Try Again...")
            return render(request, 'Registration/login_page.html')

    else:
        return render(request, 'Registration/login_page.html')


def facultyloading(request):
    return render(request, "Thesis_Schedule_App/facultyloading_page.html")


def classschedule(request):
    return render(request, "Thesis_Schedule_App/classscheduling_page.html")


def logout(request):
    return render(request, 'Registration/login_page.html')


def homePage(request):
    return render(request, 'Thesis_Schedule_App/homePage.html')


def AddProfessor(request):
    # if request.method == "POST":
    #     if request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get(''):
    #         saverecord=Professor()
    #         sa
    return render(request, 'Professor_view/AddProfessor.html')


def ProfessorList(request):
    showall=Professor.objects.all()
    return render(request, 'Professor_view/ProfessorList.html')


def Professor_Delete(request):
    return

#
# def adminAddingUser(request):
#     # q = request.GET.get('q')
#     return render(request, 'Thesis_Schedule_App/Userinfo.html')
#
#     #return render(request, 'Thesis_Schedule_App/admin_landingpage.html')
#
