from django import forms
from django.forms import ModelForm
from kapra.models import LettersTemplate

class LetterForm(forms.ModelForm):
    class Meta:
        model = LettersTemplate
        fields = ['employee', 'letter_number', 'letter_type', 'letter_date', 'letter_title', 'letter_body']


