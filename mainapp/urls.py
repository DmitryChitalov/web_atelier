"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
import mainapp.views as mainapp

app_name='mainapp'

urlpatterns = [
    re_path('^$', mainapp.catalog, name='index'),

    re_path(r'^category/(?P<category_pk>\d+)/$', mainapp.catalog, name='category'),
    re_path(r'^category/page/(?P<page>\d+)/$', mainapp.catalog, name='page'),

    re_path(r'^product/(?P<product_pk>\d+)/$', mainapp.product, name='product'),

    re_path('^contact/$', mainapp.contact, name='contact'),

]

