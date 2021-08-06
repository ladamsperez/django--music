from django import forms
from django.db.models.fields import CharField
from .models import Album

class OrderByForm(forms.Form):
    order = CharField(max_length=20)

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('artist', 'title', 'year')






        
        
    