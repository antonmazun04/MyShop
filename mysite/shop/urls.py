from django.urls import path
from django.conf.urls import include
from . import views


app_name='shop'
urlpatterns=[

    path('category/<str:slug>/', views.product_list, name='product_list'),
    path('products/<str:id>/<str:slug>/', views.product_detail, name='product_detail'),
]
