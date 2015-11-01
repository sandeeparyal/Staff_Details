from django import forms
from django.forms import ModelForm
from kapra.models import LettersTemplate

class LetterForm(forms.ModelForm):
    class Meta:
        model = LettersTemplate
        fields = ['letter_type', 'letter_date', 'letter_title', 'letter_body']




'''class LetterForm(forms.Form):
    letter_number = forms.IntegerField(required=True)
    letter_number = forms.IntegerField(required=True)
    letter_type = forms.IntegerField(required=True)
    letter_date = forms.DateTimeField('date published')
    letter_title = forms.CharField(max_length=200)
    letter_body = forms.CharField(max_length=5000)'''
    
    
        

#class LettersTemplate(models.Model):
#    employee = models.ForeignKey(Employee)
#    letter_number = models.IntegerField(default=0)
#    letter_type = models.IntegerField(default=0)
#    letter_date = models.DateTimeField('date published')
#    letter_title = models.CharField(max_length=200)
#    letter_body = models.CharField(max_length=5000)
    
#    def __unicode__(self):
#        return self.letter_title
