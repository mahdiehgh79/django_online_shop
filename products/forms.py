from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    model = Comment

    class Meta:
        model = Comment
        fields = ['body', 'stars', ]
