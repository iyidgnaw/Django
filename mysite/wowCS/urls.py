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
    # /allnote/
    url(r'^allnote/$',views.AllNotesView.as_view(), name = 'show_all_notes'),
    # /allnote/
    url(r'^allnotebook/$', views.AllNotebooksView.as_view(), name='show_all_notebooks'),

    # /notebook/Python/
    url(r'^notebook/(?P<notebook_title>[a-zA-Z0-9]+)/$',views.NoteBookView.as_view(), name = 'catalogue'),
    # /note/1/
    url(r'^note/(?P<note_id>[0-9]+)/$',views.detail, name = 'detail'),


    # # /add_notebook/
    url(r'add/notebook/$', views.create_notebook, name='notebook-add'),
    # /update/notebook/Python/
    url(r'update/notebook/(?P<notebook_title>[a-zA-Z0-9]+)/$', views.update_notebook, name='notebook-update'),
    # /delete/notebook/Python/
    url(r'delete/notebook/(?P<notebook_title>[a-zA-Z0-9]+)/$', views.delete_notebook, name='notebook-delete'),

    # /Python/add/
    url(r'add/note/$', views.create_note, name='note-add'),
    # /update/note/1/
    url(r'update/note/(?P<note_id>[0-9]+)/$', views.update_note, name='note-update'),
    # /delete/note/1/
    url(r'delete/note/(?P<note_id>[0-9]+)/$', views.delete_note, name='note-delete'),

    # /favorite/1
    url(r'^favorite/(?P<note_id>[0-9]+)/$',views.favorite, name = 'add-favorite'),

    # /favorite/all
    url(r'^favorite/all/$',views.FavoriteView.as_view(), name = 'allfavorite'),

    # /see/1
    # public profile page for user 1.
    url(r'^see/(?P<user_id>[0-9]+)/$',views.UserView.as_view(), name = 'see'),

    url(r'^search/$', views.SearchView.as_view(), name='search'),

    # api

    # method : get
    url(r'^api/10recentnotes/$', views.RecentNoteList.as_view(), name='10recentnotes'),
    # method : get
    url(r'^api/10recentnotebooks/$',views.RecentNotebookList.as_view(),name='10recentnotebooks'),

    url(r'^api/10popular/$',views.Popular.as_view(),name='popular'),

    url(r'^api/preview/(?P<id>[0-9]+)/$',views.Preview.as_view(),name='preview'),

    url(r'^api/usercatagory/$',views.UserCatagory.as_view(),name="usercatagory"),

    url(r'^api/notesin/(?P<notebook_title>[a-zA-Z0-9]+)/$', views.NotebookCatagory.as_view(), name="notesin"),

]