
# Yeh Sb bhii Review Ka hai
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Choices for rating from 1 to 5
    user_name = forms.CharField(max_length=100)
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']