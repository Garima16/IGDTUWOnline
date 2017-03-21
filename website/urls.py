from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.home, name='home'),
    # url(r'^$',)
    url(r'^$', views.login_view, name='login'),
    url(r'^password_change/$', views.change_password, name='password_change'),
]

