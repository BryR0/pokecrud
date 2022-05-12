from django import forms
from .models import Api

"""
class ApiCreateForm(forms.ModelForm):
    class Meta:
        model=Api
        name=forms.CharField()
        image=forms.ImageField()
"""

class ApiCreateForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()