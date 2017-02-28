from rest_framework import serializers
from .models import Note,Notebook

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('note_title','id','user','note_content','favorite_count','date')



class NoteBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = ('notebook_title','id')
