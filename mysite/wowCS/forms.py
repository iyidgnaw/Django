from django import forms
from django.contrib.auth.models import User
from .models import Notebook,Note
from pagedown.widgets import PagedownWidget



class NoteBookForm(forms.ModelForm):
	

	class Meta:
		model = Notebook
		fields = ('notebook_title','notebook_description')


class NoteForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
			user = kwargs.pop('user', None)
			super(NoteForm, self).__init__(*args, **kwargs)
			if user:
				self.fields['notebook'].queryset = Notebook.objects.filter(user = user)

	note_content = forms.CharField(widget=PagedownWidget())
	class Meta:
		model = Note
		fields = ['notebook','note_title','note_content','ispublic']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']