from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket


@login_required
def profile(request):
    ''' view for user profile'''

    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Данные успешно сохранены')
            form.save()
    else:
        form = UserProfileForm(instance=user)

    context = {
        'title':'GeekShop - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=user)
    }

    return render(request, 'authapp/profile.html', context)

def login(request):
    ''' view for user login'''

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'title':'GeekShop - Вход',
        'form': form
    }

    return render(request, 'authapp/login.html', context)

def logout(request):
    ''' view for user logout'''

    auth.logout(request)
    return render(request, 'mainapp/index.html')

def register(request):
    ''' view for user register'''

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегистрировались, можете войти на сайт используюя свой логин и пароль.')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()

    context = {
        'title':'GeekShop - Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context)
