# forms.py
from django import forms
from .models import ProgrammingLanguage

class LanguageForm(forms.ModelForm):
    class Meta:
        model = ProgrammingLanguage
        fields = ['name', 'creator', 'release_year', 'paradigm', 'typical_use']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter the language name'}),
            'creator': forms.TextInput(attrs={'placeholder': 'Enter the creator of the language'}),
            'release_year': forms.NumberInput(attrs={'placeholder': 'Enter the release year'}),
            'paradigm': forms.TextInput(attrs={'placeholder': 'Enter the programming paradigm'}),
            'typical_use': forms.TextInput(attrs={'placeholder': 'Enter the typical use cases'}),
        }
