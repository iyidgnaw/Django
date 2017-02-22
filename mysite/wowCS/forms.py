from django import forms
from django.contrib.auth.models import User
from .models import Notebook,Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['note_title','note_content']