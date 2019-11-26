from django.contrib import admin
from django.urls import path, re_path, include
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('^$', mainapp.index, name='index'),

    re_path('^main/', include('mainapp.urls', namespace='main')),

    re_path('^auth/', include('authapp.urls', namespace='auth')),

    re_path('^basket/', include('basketapp.urls', namespace='basket')),

    re_path('^orders/', include('ordersapp.urls', namespace='orders')),

    re_path('^admin/', include('adminapp.urls', namespace='admin')),

    re_path(r'^auth/verify/google/oauth2/', include("social_django.urls", namespace="social")),

    # path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)