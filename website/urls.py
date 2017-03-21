from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='login'),
    url(r'^password_change/$', views.change_password, name='password_change'),
    url(r'^home_page/$', views.home_page, name='home_page')
]

