from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/password_change/$', views.password_change, name='password_change', kwargs={'next_page': '/'}),
    url(r'^accounts/password_change_done/$', views.password_change_done, name='password_change_done',
        kwargs={'next_page': '/'}),
    url(r'^accounts/password_reset/$', views.password_reset, name='password_reset'),
    url(r'^accounts/password_reset_done/$', views.password_reset_done, name='password_change_done',
        kwargs={'next_page': '/'}),
]



