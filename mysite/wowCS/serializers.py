from rest_framework import serializers
from .models import Note,Notebook

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('note_title',)



class NoteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = ('notebook_title',)