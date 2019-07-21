from django.urls import path, re_path
from django.views.decorators.cache import cache_page

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    re_path(r'^category/(?P<pk>\d+)/$', cache_page(3600)(mainapp.products)),
    re_path(r'^category/(?P<pk>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$', cache_page(3600)(mainapp.products_ajax)),
    path('product/<int:pk>/', mainapp.product, name='product'),
    path('category/<int:pk>/', mainapp.products, name='category'),
]
