from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homeView(request):
    if request.method == "POST":
        if request.POST.get("formFor")=="signin":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                context ={}
                context['error']='KAUN HAY BE TU'
                return render(request,"login/login_page.html",context)

        elif request.POST.get("formFor")=="signup":
            # signup garchhau
            pass

    return render(request,'login/login_page.html',{})

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return HttpResponse("KAUN HAY BE TU")
        return HttpResponse('username :'+username+' password : '+password)

def logoutView(request):
    logout(request)
    return redirect("/")
