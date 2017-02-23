from django.views import generic
from django.views.generic.edit import CreateView
from .models import Notebook,Note
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from .serializers import NoteSerializer,NoteBookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
import pypandoc





class IndexView(generic.ListView):

    template_name = 'wowCS/index.html'
    context_object_name = 'all_notebook'

    def get_queryset(self):
        return Notebook.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request, 'wowCS/login.html')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

class NoteBookView(generic.ListView):
    template_name = 'wowCS/catalogue.html'
    context_object_name = 'notebook'

    def get_queryset(self):
        notebook = Notebook.objects.get(notebook_title=self.kwargs.get('notebook_title'))
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

def detail(request,note_id):
    if not request.user.is_authenticated():
        return render(request, 'wowCS/login.html')

    note = Note.objects.get(id=note_id)
    # show the detail only if the requested note belongs to the current user
    if note.user==request.user:
        html = pypandoc.convert_file(note.note_content.url, 'html')
        return render(request, 'wowCS/detail.html', {'note': note,'note_content':html})
    else:
        return render(request, 'wowCS/wrong.html', {'error_message': "<h1>You can't see that note!</h1>"})

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
            return render(request, 'wowCS/login.html', {'error_message': 'Invalid login'})
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

            # returns User objects if credentials are correct
            user = authenticate(username = username,password=password)
            if user is not None and user.is_active:
                login(request,user)
                return redirect('wowCS:index')
                # request.user.username/profile...
        else:
            return render(request, self.template_name, {'form': form})

class RecentNoteList(APIView):

    # List all notes
    def get(self,request):
        notes = Note.objects.all()
        if len(notes)<=5:
            pass
        else:
            notes = notes[len(notes)-5:]
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data)

class RecentNotebookList(APIView):

    # List all notebooks
    def get(self,request):
        notebooks = Notebook.objects.all()
        if len(notebooks)<=5:
            pass
        else:
            notebooks = notebooks[len(notebooks)-5:]
        serializer = NoteBookSerializer(notebooks,many=True)
        return Response(serializer.data)














