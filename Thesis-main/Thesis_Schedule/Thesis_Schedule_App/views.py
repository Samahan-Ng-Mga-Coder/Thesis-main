
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user
from django.shortcuts import render, redirect



# Create your views here.

<<<<<<< Updated upstream
# def login(request):
#
#     if request.method == "POST":
#         #request method
#         username = request.POST['username']
#         password = request.POST['password']
#         #check user request to authenticate
#         user = authenticate(request, username=username, password=password)
#
#         #conditional statement
#         if user is not None:
#             login(request, user)
#             return redirect(request, 'admin_landingpage')
#         else:
#             messages.error(request, "There Was an Error Logging In, Try Again...")
#             return render(request, 'Registration/login_page.html')
#
#     else:
#         return render(request, 'Registration/login_page.html')


=======
>>>>>>> Stashed changes
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

#
# def adminAddingUser(request):
#     # q = request.GET.get('q')
#     return render(request, 'Thesis_Schedule_App/Userinfo.html')
#
#     #return render(request, 'Thesis_Schedule_App/admin_landingpage.html')
#
