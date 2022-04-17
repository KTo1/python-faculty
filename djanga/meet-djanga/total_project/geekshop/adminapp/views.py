from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, UserAdminCategoryForm, UserAdminProductForm
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

from mainapp.models import ProductCategories, Products

def object_delete_by_id(object, id):
    _ = object.objects.get(id=id)
    _.is_active = False
    _.save()

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    ''' view for start page'''

    return render(request, 'adminapp/admin.html')

# region users

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    ''' view for user list'''

    context = {
        'title': 'Администраторский раздел - Пользователи',
        'users': User.objects.all()
    }

    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    ''' view for user create'''

    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminRegisterForm()

    context = {
        'title': 'Администраторский раздел - Создание пользователя',
        'form': form
    }

    return render(request, 'adminapp/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    ''' view for user update'''

    user_select = User.objects.get(id = id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно отредактирован.')
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=user_select)

    context = {
        'title': 'Администраторский раздел - Редактирование пользователя',
        'form': form,
        'user_select': user_select
    }

    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    ''' view for user delete'''

    object_delete_by_id(User, id)
    messages.success(request, 'Пользователь успешно удален.')
    return HttpResponseRedirect(reverse('adminapp:admin_users'))

#endregion

# region categories

@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    ''' view for category list'''

    context = {
        'title': 'Администраторский раздел - Категории',
        'categories': ProductCategories.objects.all()
    }

    return render(request, 'adminapp/admin-categories-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    ''' view for category create'''

    if request.method == 'POST':
        form = UserAdminCategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно создана.')
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
    else:
        form = UserAdminCategoryForm()

    context = {
        'title': 'Администраторский раздел - Создание категории',
        'form': form
    }

    return render(request, 'adminapp/admin-categories-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    ''' view for category update'''

    category_select = ProductCategories.objects.get(id = id)
    if request.method == 'POST':
        form = UserAdminCategoryForm(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно обновлена.')
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            print(form.errors)
    else:
        form = UserAdminCategoryForm(instance=category_select)

    context = {
        'title': 'Администраторский раздел - Редактирование категории',
        'form': form,
        'category_select': category_select
    }

    return render(request, 'adminapp/admin-categories-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    ''' view for category delete'''

    object_delete_by_id(ProductCategories, id)
    messages.success(request, 'Категория успешно удалена.')
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))

#endregion

# region products

@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    ''' view for product list'''

    context = {
        'title': 'Администраторский раздел - Продукты',
        'products': Products.objects.all()
    }

    return render(request, 'adminapp/admin-products-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    ''' view for product create'''

    if request.method == 'POST':
        form = UserAdminProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно создан.')
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = UserAdminProductForm()

    context = {
        'title': 'Администраторский раздел - Создание продукта',
        'form': form
    }

    return render(request, 'adminapp/admin-products-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    ''' view for product update'''

    product_select = Products.objects.get(id = id)
    if request.method == 'POST':
        form = UserAdminProductForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлен.')
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            print(form.errors)
    else:
        form = UserAdminProductForm(instance=product_select)

    context = {
        'title': 'Администраторский раздел - Редактирование продукта',
        'form': form,
        'product_select': product_select
    }

    return render(request, 'adminapp/admin-products-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    ''' view for product delete'''

    object_delete_by_id(Products, id)
    messages.success(request, 'Продукт успешно удален.')
    return HttpResponseRedirect(reverse('adminapp:admin_products'))

#endregion