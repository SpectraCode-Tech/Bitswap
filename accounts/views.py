from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists.")
            return redirect('signup')
        
        user = User.objects.create_user(
            username = username,
            email = email,
            password = password1
        )
        
        login(request, user)
        return redirect('dashboard')
    return render(request, 'accounts/Register.html')


def login_views(request):
    if request.method == 'POST':
        identifier = request.POST['username']
        password = request.POST['password']
        
        if '@' in identifier:
            try:
                user_obj = User.objects.get(email = identifier)
                username = user_obj.username
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect('login')
        else:
            username = identifier
            user = authenticate(request, username = username, password = password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid login details.")
               
    return render(request, 'accounts/Login.html')

def logout(request):
    logout(request)
    return redirect('home')