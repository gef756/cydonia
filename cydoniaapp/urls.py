from django.conf.urls import patterns, url
from cydoniaapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
