from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def index(request):
    context = {
        'firstcategory': Category.objects.get(category_name='2023/24 Season Kits'),
        'categories': Category.objects.exclude(category_name='2023/24 Season Kits'),
        'products' : Product.objects.all()
    }
    return render(request, 'home/index.html', context)


def get_cat_product(request, uid):
    context = {
        'catname': Category.objects.get(uid=uid),
        'catproducts': Product.objects.filter(category=uid)
    }
    return render(request, 'home/catproduct.html', context)