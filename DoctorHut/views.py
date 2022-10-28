from django.shortcuts import HttpResponse,render

def Home(request):
    return render(request, "Home.html")

def clinic_login(request):
    return render(request,'clinic_login.html')