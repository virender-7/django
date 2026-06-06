from django import forms
from posts import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = ['title','body','slug','banner']

