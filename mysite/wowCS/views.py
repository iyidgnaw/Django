from django.views import generic
from django.urls import reverse
from .models import Notebook,Note,Favorite
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm,NoteBookForm,NoteForm
from .serializers import NoteSerializer,NoteBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import pypandoc
import re
from datetime import datetime



# index view
class IndexView(generic.ListView):

    template_name = 'wowCS/index.html'
    context_object_name = 'all_note'

    def get_queryset(self):
        return Note.objects.filter(ispublic=True)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if request.user.is_authenticated():
            context['islogin'] = True
        else:
            context['islogin'] = False
        return self.render_to_response(context)

# catalogue view for given notebook_title
class NoteBookView(generic.ListView):
    template_name = 'wowCS/catalogue.html'
    context_object_name = 'notebook'

    def get_queryset(self):
        notebook = Notebook.objects.get(notebook_title=self.kwargs.get('notebook_title'),user=self.request.user)
        # if the requested notebook doesn't belong to the current user, then return None
        if notebook.user==self.request.user:
            return notebook
        else:
            return None

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'wowCS/login.html')
        else:
            self.object_list = self.get_queryset()
            #if the get_queryset() returned None, then redirect to the wrong.html
            if not self.object_list:
                return render(request,'wowCS/wrong.html',{'error_message':"<h1>You can't see that notebook!</h1>"})
            context = self.get_context_data()
            return self.render_to_response(context)

# all notes view for listing all notes.
class AllNotebooksView(generic.ListView):
    template_name = 'wowCS/show_all_notebooks.html'
    context_object_name = 'all_notebooks'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'wowCS/login.html')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

    def get_queryset(self):
        return Notebook.objects.filter(user=self.request.user)

# all notes view for listing all notes.
class AllNotesView(generic.ListView):
    template_name = 'wowCS/show_all_notes.html'
    context_object_name = 'all_notes'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'wowCS/login.html')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

    def get_queryset(self):
        notes= []
        for notebook in Notebook.objects.filter(user=self.request.user):
            for note in notebook.note_set.all():
                notes.append(note.pk)
        return Note.objects.filter(pk__in=notes)

#detail view for the detail of a note
def detail(request,note_id):
    # if not request.user.is_authenticated():
    #     return render(request, 'wowCS/login.html')
    login_status = request.user.is_authenticated()
    note = Note.objects.get(id=note_id)
    if note.ispublic:
        html = pypandoc.convert_text(note.note_content, 'html', format='md')
        context = {'note': note, 'note_content': html, 'islogin': login_status}
        if login_status:
            if int(note_id) in [int(f.favorite_id) for f in Favorite.objects.filter(user=request.user)]:
                context['is_favorite'] = True
        return render(request, 'wowCS/detail.html',context )
    # show the private detail only if the requested note belongs to the current user
    if not login_status:
        return render(request, 'wowCS/wrong.html', {'islogin':False,'error_message': "<h1>You have to login before seeing this private note.</h1>"})
    if note.user==request.user:
        html = pypandoc.convert_text(note.note_content, 'html',format='md')
        return render(request, 'wowCS/detail.html', {'note': note,'note_content':html})
    else:
        return render(request, 'wowCS/wrong.html', {'islogin':True,'error_message': "<h1>You can't see that note!</h1>"})


# functions and class for login/logout/register/profile
def log_in(request):
    if request.user.is_authenticated():
        return render(request, 'wowCS/index.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'wowCS/login.html', {'islogin':False,'error_message': 'Invalid login'})
    return render(request, 'wowCS/login.html')

def log_out(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'wowCS/login.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'wowCS/registration_form.html'

    # display a blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    # process form data
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # create an object from the form data but not saved.
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            # Generate a default empty notebook for user.
            defaultNB = Notebook()
            defaultNB.notebook_title = 'default'
            defaultNB.user = user
            defaultNB.genre = 'blank'
            defaultNB.notebook_description = 'Default Notebook.'
            defaultNB.save()

            # Generate a introduction note for new user.

            # returns User objects if credentials are correct
            user = authenticate(username = username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return redirect('wowCS:index')
                # request.user.username/profile...
        else:
            return render(request, self.template_name, {'form': form})

def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')
    return render(request,'wowCS/profile.html',{'user':request.user})


# create/update/delete/ notebook
def create_notebook(request):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')
    else:
        form = NoteBookForm(request.POST or None, request.FILES or None)
        if form.is_valid():

            notebook = form.save(commit=False)
            if not re.match('^[a-zA-Z0-9]+$',notebook.notebook_title):
                context = {"form": form,'error_message':"Illegal Notebook name!"}
                return render(request, 'wowCS/create_notebook.html', context)
            notebook.user = request.user
            try:
                notebook.save()
            except:
                context = {"form": form,'error_message':"Duplicate Notebook name!"}
                return render(request, 'wowCS/create_notebook.html', context)
            return HttpResponseRedirect(notebook.get_absolute_url())
        context = {
            "form": form,
        }
        return render(request, 'wowCS/create_notebook.html', context)

def update_notebook(request,notebook_title):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')

    instance = get_object_or_404(Notebook, notebook_title=notebook_title)
    form = NoteBookForm(request.POST or None, request.FILES or None, instance=instance)
    if instance.user!=request.user:
        return render(request, 'wowCS/wrong.html', {'error_message': "<h1>You can't update that notebook!</h1>"})
    # the form is valid when the method is POST and files exist.
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.notebook_title,
        "instance": instance,
        "form":form,
    }

    # for the get method
    return render(request, "wowCS/notebook_form.html", context)

def delete_notebook(request, notebook_title):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')

    instance = get_object_or_404(Notebook, notebook_title=notebook_title, user=request.user)
    if instance.user!=request.user:
        return render(request, 'wowCS/wrong.html', {'error_message': "<h1>You can't delete that notebook!</h1>"})
    instance.delete()
    return redirect("wowCS:index")

# create/update/delete/ note
def create_note(request):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')
    else:
        form = NoteForm(request.POST or None, request.FILES or None,user=request.user,)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            # html = pypandoc.convert_text(note.note_content,'html',format='md')
            return HttpResponseRedirect(note.get_absolute_url())
        context = {
            "form": form,
        }
        return render(request, 'wowCS/create_note.html', context)

def update_note(request,note_id):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')

    instance = get_object_or_404(Note, id=note_id)

    if instance.user!=request.user:
        return render(request, 'wowCS/wrong.html', {'error_message': "<h1>You can't change that note!</h1>"})


    form = NoteForm(request.POST or None, request.FILES or None, instance=instance)

    # the form is valid when the method is POST and files exist.
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.note_title,
        "instance": instance,
        "form":form,
    }

    # for the get method
    return render(request, "wowCS/note_form.html", context)

def delete_note(request, note_id):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')

    instance = get_object_or_404(Note, id=note_id, user=request.user)
    notebook = instance.notebook
    if instance.user!=request.user:
        return render(request, 'wowCS/wrong.html', {'error_message': "<h1>You can't delete that note!</h1>"})
    returning = HttpResponseRedirect(instance.get_absolute_url())
    instance.delete()
    return returning


def favorite(request,note_id):
    login_status = request.user.is_authenticated()
    if not login_status:
        return render(request, 'wowCS/wrong.html', {'islogin': False,
                                                    'error_message': "<h1>You have to login first.</h1>"})
    note = Note.objects.get(id=note_id)
    if note.ispublic:
        try:
            f = Favorite()
            f.user,f.favorite_id = request.user,note_id
            f.save()
            note.favorite_count += 1
            note.save()
            return redirect(reverse('wowCS:detail', kwargs={'note_id': note_id}))
        except:
            return redirect(reverse('wowCS:detail', kwargs={'note_id': note_id}))
    else:
        return render(request, 'wowCS/wrong.html', {'islogin': False,
                                                    'error_message': "<h1>Invalid request.</h1>"})

class FavoriteView(generic.ListView):
    template_name = 'wowCS/show_all_notes.html'
    context_object_name = 'all_notes'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'wowCS/login.html')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

    def get_queryset(self):
        notes = [f.favorite_id for f in Favorite.objects.filter(user=self.request.user)]
        return Note.objects.filter(pk__in=notes)



# restful API
class RecentNoteList(APIView):

    # List all notes
    def get(self,request):
        notes = Note.objects.filter(user=request.user)
        if len(notes)<=10:
            pass
        else:
            notes = notes[len(notes)-5:]
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)

class RecentNotebookList(APIView):

    # List all notebooks
    def get(self,request):
        notebooks = Notebook.objects.filter(user=request.user)
        if len(notebooks)<=10:
            pass
        else:
            notebooks = notebooks[len(notebooks)-5:]
        serializer = NoteBookSerializer(notebooks,many=True)
        return Response(serializer.data)


class Preview(APIView):
    def get(self, request, *args, **kwargs):
        note = Note.objects.get(id=self.kwargs.get('id'))
        if note.ispublic:
            pass
        else:
            if request.user.is_authenticated() and note.user==request.user:
                pass
            else:
                note = None
        serializer = NoteSerializer(note)
        return Response(serializer.data)

class Popular(APIView):
    def get(self, request):
        notes = Note.objects.filter(ispublic=True)
        notes = sorted(notes,key=lambda x:x.favorite_count,reverse=True)[:10]
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)