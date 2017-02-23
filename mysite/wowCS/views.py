from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Notebook,Note
from django.shortcuts import render,redirect
from django.utils.html import format_html
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .forms import UserForm
import pypandoc





class IndexView(generic.ListView):
    template_name = 'wowCS/index.html'
    context_object_name = 'all_notebook'
    def get_queryset(self):
        return Notebook.objects.all()


def catalogue(request,notebook_title):
    notebook = Notebook.objects.get(notebook_title=notebook_title)
    return render(request, 'wowCS/catalogue.html', {'notebook':notebook})

def show_all_notes(request):
    notes = Note.objects.all()
    return render(request,'wowCS/show_all_notes.html',{'all_notes':notes})

def detail(request,notebook_title,note_id):
    note = Note.objects.get(id=note_id)
    html = pypandoc.convert_file(note.note_content.url, 'html')
    return render(request, 'wowCS/detail.html', {'note': note,'note_content':html})

class NotebookCreate(CreateView):
    model = Notebook
    fields = ['notebook_title','genre','notebook_description']

class NoteCreate(CreateView):
    model = Note
    fields = ['notebook','note_title','note_content','is_favorite']

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

















