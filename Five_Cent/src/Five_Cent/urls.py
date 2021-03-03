from django.urls import path
from . import views

app_name = 'Five_Cent'

urlpatterns = [

    path('', views.productlist, name='product_list'),
    path('<slug:product_slug>', views.productdetail, name='product_detail'),

]
