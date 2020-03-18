from django import forms
from .models import Review, Material, Department, Message

class MaterialSearchForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('level', 'faculty', 'department')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.none()

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


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Email'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={    
        'placeholder' : 'Subject of your Message'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder' : 'Your Message'
    }))

    class Meta:
        model = Message
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]