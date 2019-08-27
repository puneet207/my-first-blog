from django import forms
from .models import Board


class PostForm(forms.ModelForm):


    class Meta:
        model = Board
        fields = ('title', 'text',)