from django.urls import path
from home.views import index, get_cat_product

urlpatterns = [
    path('', index, name="index"),
    path('category/<str:uid>', get_cat_product, name="category_product")
]
