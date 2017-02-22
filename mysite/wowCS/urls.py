from django.conf.urls import url

from . import views

app_name = 'wowCS'

urlpatterns = [

    url(r'^$',views.IndexView.as_view(),name = 'index'),

    url(r'notes/$',views.show_all_notes, name = 'show_all_notes'),

    url(r'^(?P<notebook_title>[a-zA-Z]+)/$',views.catalogue, name = 'catalogue'),

    url(r'^(?P<notebook_title>[a-zA-Z]+)/(?P<note_id>[0-9]+)/$',views.detail, name = 'detail'),

    url(r'notebook/add/$', views.NotebookCreate.as_view(), name='notebook-add'),


]