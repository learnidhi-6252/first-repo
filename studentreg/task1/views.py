from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import reginfo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,"index.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'profile.html', {
        'user': request.user
    })

def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")

        User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        reginfo.objects.create(
            name=name,
            password=password,
            email=email
        )

        return redirect('login')

    return render(request, "register.html")

def adminlog(request):
    USERNAME = "admin"
    PASSWORD = "admin"

    if request.method == "POST":
        username = request.POST.get("username") 
        password = request.POST.get("password")

        if username == USERNAME and password == PASSWORD:
            request.session['user'] = username
            return redirect('/regview')
        else:
            return render(request, 'adminlog.html', {'error': 'Invalid credentials'})

    return render(request, 'adminlog.html')



def regview(request):
    all_infos = reginfo.objects.all()
    return render(request, 'regview.html', {'all_infos': all_infos})

def reg_detail(request, id):
    data = get_object_or_404(reginfo, id=id)
    return render(request, 'reg_detail.html', {'data': data})

def edit(request,id):
    info=reginfo.objects.get(id=id)
    return render(request,'edit.html',{'informations':info})

def updateinfo(request):
    if request.method=="POST":

        id=request.POST.get("id")
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")

        info=reginfo.objects.get(id=id)

        info.name = name
        info.password = password
        info.email = email
        info.save()

        return redirect ('/regview')
    

def deleteinfo(request,id):
    info = reginfo.objects.get(id=id)
    info.delete()
    return redirect('/regview')



