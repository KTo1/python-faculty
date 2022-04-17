import json
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.views.generic import DetailView
# Create your views here.
from mainapp.models import ProductCategories, Products


def index(request):
    ''' view for index'''

    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)

def products(request, category_id=None, page_id=1):
    ''' view for products'''

    if category_id:
        products = Products.objects.filter(category_id=category_id, is_active=True)
    else:
        products = Products.objects.filter(is_active=True)

    paginator = Paginator(products, per_page=2)

    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'title':'GeekShop - Каталог',
               'products': products_paginator,
               'categories': ProductCategories.objects.filter(is_active=True),
               }

    return render(request, 'mainapp/products.html', context)


class ProductDetail(DetailView):
    model = Products
    template_name ='mainapp/detail.html'