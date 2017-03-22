"""Blog Forms."""

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Form for Creating Another Post."""

    class Meta:
        model = Post
        fields = ('title', 'text',)
