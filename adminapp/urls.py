from django.urls import path, re_path
import adminapp.views as adminapp

app_name='adminapp'

urlpatterns = [
    # re_path('^$', adminapp.index, name='index'),
    # re_path(r'^user/page/(?P<page>\d+)/$', adminapp.index, name='page'),
    re_path('^$', adminapp.UsersListView.as_view(), name='index'),
    re_path('^user/create/$', adminapp.user_create, name='user_create'),
    re_path('^user/update/(?P<pk>\d+)/$', adminapp.user_update, name='user_update'),
    re_path('^user/delete/(?P<pk>\d+)/$', adminapp.user_delete, name='user_delete'),
    re_path('^user/recover/(?P<pk>\d+)/$', adminapp.user_recover, name='user_recover'),

    re_path('^categories/$', adminapp.categories, name='categories'),
    # re_path('^category/create/$', adminapp.category_create, name='category_create'),
    re_path('^category/create/$', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    # re_path('^category/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    re_path('^category/update/(?P<pk>\d+)/$', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    # re_path('^category/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    re_path('^category/delete/(?P<pk>\d+)/$', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
    re_path('^category/recover/(?P<pk>\d+)/$', adminapp.category_recover, name='category_recover'),

    re_path('^products/(?P<category_pk>\d+)/$', adminapp.products, name='products'),
    re_path('^product/create/(?P<category_pk>\d+)/$', adminapp.product_create, name='product_create'),
    # re_path('^product/read/(?P<pk>\d+)/$', adminapp.product_read, name='product_read'),
    re_path('^product/read/(?P<pk>\d+)/$', adminapp.ProductDetailView.as_view(), name='product_read'),
    re_path('^product/update/(?P<pk>\d+)/$', adminapp.product_update, name='product_update'),
    re_path('^product/delete/(?P<pk>\d+)/$', adminapp.product_delete, name='product_delete'),
    re_path('^product/recover/(?P<pk>\d+)/$', adminapp.product_recover, name='product_recover'),
]

