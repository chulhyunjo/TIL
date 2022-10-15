from dataclasses import field
from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        exclude = ('user_id',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)