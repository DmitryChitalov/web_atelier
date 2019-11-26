from django.urls import path, re_path
import basketapp.views as basketapp

app_name='basketapp'

urlpatterns = [
    re_path('^index/$', basketapp.index, name='index'),
    re_path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),

    re_path(r'^add/(?P<pk>\d+)/(?P<value>\d+)/ajax/$', basketapp.basket_add_ajax),

    re_path(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),

]

