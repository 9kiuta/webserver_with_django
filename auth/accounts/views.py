from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']  # (1점)
        password = request.POST['password']  # (1점)

        user = authenticate(request, username=username, password=password)  # (총 2점: 각 1점)

        if user is not None:
            login(request, user)  # (1점)
            return redirect('home')  # (1점)
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
            return render(request, 'accounts/login.html')  # (1점)
    else:
        return render(request, 'accounts/login.html')

@login_required
def home_view(request):
    return render(request, 'accounts/home.html', {'user': request.user})

def logout_view(request):
    logout(request)  # (1점)
    return redirect('login')
