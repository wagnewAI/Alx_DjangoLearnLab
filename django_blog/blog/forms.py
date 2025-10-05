from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

# Form for creating/editing posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),  # <-- TagWidget correctly applied
        }

# Form for adding/editing comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }

