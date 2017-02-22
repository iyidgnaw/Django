from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Notebook,Note
from django.shortcuts import render,get_object_or_404
from django.utils.html import format_html
import markdown

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
    filename = './'+note.note_content.name
    file = open(filename,'r')
    text = file.read()
    html = markdown.markdown(text)
    html = format_html(html)
    # html = format_html('<p>Hello</p>')
    return render(request, 'wowCS/detail.html', {'note': note,'note_content':html})

class NotebookCreate(CreateView):
    model = Notebook
    fields = ['notebook_title','genre','notebook_description']

class NoteCreate(CreateView):
    model = Note
    fields = ['notebook','note_title','note_content','is_favorite']



