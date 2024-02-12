from django import forms
from datetime import date

class ReviewForm(forms.Form):
    username = forms.CharField(max_length=100)    
    rating = forms.IntegerField(min_value=1, max_value=5)
    userreview = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
