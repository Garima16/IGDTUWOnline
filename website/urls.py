from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books/$', views.home, name='home'),
    # url(r'^$',)
    url(r'^$', views.login_view, name='login'),
    url(r'^password_change/$', views.change_password, name='password_change'),
    url(r'^set_password_unusable/$', views.set_password_unusable, name='set_password_unusable'),
    # url(r'^logging_first_time/$', views.if_logging_for_first_time, name='if_logging_first_time')
]

