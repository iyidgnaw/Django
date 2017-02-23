from django import forms
from django.contrib.auth.models import User
from .models import Notebook,Note
from pagedown.widgets import PagedownWidget



class NoteBookForm(forms.ModelForm):
	
	class Meta:
		model = Notebook
		fields = ('notebook_title','genre','notebook_description')


class NoteForm(forms.ModelForm):
	note_content = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Note
		fields = ['notebook','note_title','note_content']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']