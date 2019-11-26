from django.urls import path, re_path
import authapp.views as authapp

app_name='authapp'

urlpatterns = [
    re_path('^login/$', authapp.user_login, name='login'),
    re_path('^logout/$', authapp.user_logout, name='logout'),
    re_path('^register/$', authapp.register, name='register'),
    # re_path('^edit/(\d+)/$', authapp.edit, name='edit'),
    re_path('^edit/$', authapp.edit, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', authapp.verify, name='verify'),
]

