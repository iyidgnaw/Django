from django.conf.urls import url

from . import views

app_name = 'wowCS'

urlpatterns = [
    # main page of the root
    url(r'^$',views.IndexView.as_view(),name = 'index'),
    # /notes/
    url(r'notes/$',views.show_all_notes, name = 'show_all_notes'),
    # /Python/
    url(r'^(?P<notebook_title>[a-zA-Z]+)/$',views.catalogue, name = 'catalogue'),
    # /Python/1/
    url(r'^(?P<notebook_title>[a-zA-Z]+)/(?P<note_id>[0-9]+)/$',views.detail, name = 'detail'),
    # /add_notebook/
    url(r'add_notebook/$', views.NotebookCreate.as_view(), name='notebook-add'),
    # /Python/add/
    url(r'^(?P<notebook_title>[a-zA-Z]+)/add/$', views.NoteCreate.as_view(), name='note-add'),

]