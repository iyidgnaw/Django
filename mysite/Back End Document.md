# Back End Document 

### URL

首页请求

```python
url(r'^$',views.IndexView.as_view(),name = 'index'),
```

登入/登出/注册请求

```python
url(r'^login/$',views.log_in,name = 'login'),
```
```python
url(r'^logout/$', views.log_out, name='logout'),
```
```python
url(r'^register/$',views.UserFormView.as_view(),name = 'register'),
```
查看用户信息

```python
url(r'^profile/$',views.profile,name = 'profile'),
```
显示当前用户所有笔记

```python
url(r'^allnote/$',views.AllNotesView.as_view(), name = 'show_all_notes'),
```
显示当前用户所有笔记本

```python
url(r'^allnotebook/$', views.AllNotebooksView.as_view(), name='show_all_notebooks'),
```
显示某笔记本目录

```python
url(r'^notebook/(?P<notebook_title>[a-zA-Z0-9]+)/$',views.NoteBookView.as_view(), name = 'catalogue'),
```
显示某条笔记内容

```python
url(r'^note/(?P<note_id>[0-9]+)/$',views.detail, name = 'detail'),
```

添加/修改/删除笔记本

```python
url(r'add/notebook/$', views.create_notebook, name='notebook-add'),
```
```python
url(r'update/notebook/(?P<notebook_title>[a-zA-Z]+)/$', views.update_notebook, name='notebook-update'), 
```
```python
url(r'delete/notebook/(?P<notebook_title>[a-zA-Z]+)/$', views.delete_notebook, name='notebook-delete'), 
```
添加/修改/删除笔记

```python
url(r'add/note/$', views.create_note, name='note-add'),
```
```python
url(r'update/note/(?P<note_id>[0-9]+)/$', views.update_note, name='note-update'),
```
```python
url(r'delete/note/(?P<note_id>[0-9]+)/$', views.delete_note, name='note-delete'),
```

# api

最近添加的五条笔记

```python
url(r'^api/5recentnotes/$', views.RecentNoteList.as_view(), name='5recentnotes'),
```
最近添加的五个笔记本

```python
url(r'^api/5recentnotebooks/$',views.RecentNotebookList.as_view(),name='5recentnotebooks'),
```
