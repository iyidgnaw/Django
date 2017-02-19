from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.poll, name='poll'),
    url(r'^main/$', views.main),
]