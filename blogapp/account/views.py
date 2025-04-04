from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {"error": "incorrect username or password"})
                   
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {
                    "error":"Bu Username Kullanılıyor",
                    "username":username,
                    "email":email,
                    "firstname":firstname,
                    "lastname":lastname})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {
                        "error":"Bu Email Kullanılıyor",
                        "username":username,
                        "email":email,
                        "firstname":firstname,
                        "lastname":lastname})
                else:
                    user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password)
                    user.save()
                    return redirect("login")
        else:
            return render(request, "account/register.html",{"error":"parolalar eşleşmiyor",                    "username":username,
            "email":email,
            "firstname":firstname,
            "lastname":lastname})
        
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homework_list')  # veya 'home'
        else:
            return render(request, 'account/login.html', {'error': 'Geçersiz kullanıcı bilgileri'})
    return render(request, 'account/login.html')