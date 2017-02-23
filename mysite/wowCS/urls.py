from django.conf.urls import url
from . import views

app_name = 'wowCS'

urlpatterns = [
    # main page of the root
    url(r'^$',views.IndexView.as_view(),name = 'index'),
    # login
    url(r'^login/$',views.log_in,name = 'login'),
    # logout
    url(r'^logout/$', views.log_out, name='logout'),
    # register
    url(r'^register/$',views.UserFormView.as_view(),name = 'register'),
    # profile
    url(r'^profile/$',views.profile,name = 'profile'),
    # /notes/
    url(r'^note/all/$',views.AllNotesView.as_view(), name = 'show_all_notes'),
    # /Python/
    url(r'^notebook/(?P<notebook_title>[a-zA-Z]+)/$',views.NoteBookView.as_view(), name = 'catalogue'),
    # /Python/1/
    url(r'^note/(?P<note_id>[0-9]+)/$',views.detail, name = 'detail'),






    # # /add_notebook/
    url(r'add/notebook/$', views.create_notebook, name='notebook-add'),
    # /update/notebook/Python/
    url(r'update/notebook/(?P<notebook_title>[a-zA-Z]+)/$', views.update_notebook, name='notebook-update'),
    #
    # /Python/add/
    url(r'add/note/$', views.create_note, name='note-add'),
    # /update/note/1/
    url(r'update/note/(?P<note_id>[0-9]+)/$', views.update_note, name='note-update'),

    # api

    # method : get
    url(r'^api/5recentnotes/$', views.RecentNoteList.as_view(), name='5recentnotes'),
    # method : get
    url(r'^api/5recentnotebooks/$',views.RecentNotebookList.as_view(),name='5recentnotebooks'),

]