from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Notebook,Note
from django.shortcuts import render


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
    return render(request, 'wowCS/detail.html', {'note': note})


class NotebookCreate(CreateView):
    model = Notebook
    fields = ['notebook_title','genre','notebook_description']


