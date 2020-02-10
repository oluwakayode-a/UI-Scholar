from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Write Your Review'
        }
    ))

    class Meta:
        model = Review
        fields = ('review',)
