# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from kapra.models import LettersTemplate

class LetterForm(forms.ModelForm):
    class Meta:
        model = LettersTemplate
        fields = [ 'letter_type', 'employee', 'letter_number', 'letter_date', 'letter_title', 'letter_body']


