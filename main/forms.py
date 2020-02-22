from django import forms
from .models import Review, Material, Department

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
