from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Write Your Comment'
        }
    ))

    class Meta:
        model = Comment
        fields = ('body',)


