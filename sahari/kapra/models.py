from django.db import models
from django.utils import timezone

# Create your models here.

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=200)
    ministry_location = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.ministry_name


class HeadSection(models.Model):
    ministry = models.ForeignKey(Ministry)
    head_section_name = models.CharField(max_length=150)
    no_of_employees = models.IntegerField(default=0)

    def __unicode__(self):
        return self.head_section_name


class Section(models.Model):
    headsection = models.ForeignKey(HeadSection)
    section_name = models.CharField(max_length=150)
    no_of_employees = models.IntegerField(default=0)

    def __unicode__(self):
        return self.section_name


class Employee(models.Model):
    EMPLOYEE_TYPE_CHOICES = (
                             ('perm', 'Permanent'), ('temp', 'Temporary'))
    section = models.ForeignKey(Section)
    emp_id = models.CharField(max_length=10, unique=True)
    emp_first_name = models.CharField(max_length=50)
    emp_middle_name = models.CharField(max_length=50, blank=True)
    emp_last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    emp_joined_date = models.DateField('Employee Joined Date')
    emp_depart_date = models.DateField('Employee Departed Date', blank=True)
    emp_status = models.CharField(max_length=50, blank=True)
    emp_phone = models.CharField(max_length=12, blank=True)
    emp_type = models.CharField(max_length=4, choices=EMPLOYEE_TYPE_CHOICES)
    
    def __unicode__(self):
        return self.designation

    def employee_duration(self):
        return timezone.datetime.now()


class LettersTemplate(models.Model):
    TITLE_CHOICES = (
                     ('appointment', 'Niyukti'), ('transfer', 'Saruwa'))
    LETTER_TYPES_CHOICES = (
                            ('ni', 'Niyukti'), ('padas', 'Padasthapan'), ('trans', 'Transfer'))
    employee = models.ForeignKey(Employee)
    letter_number = models.IntegerField(default=0)
    letter_type = models.CharField(max_length=200, choices=LETTER_TYPES_CHOICES)
    letter_date = models.DateField('date published')
    letter_title = models.CharField(max_length=200, choices=TITLE_CHOICES)
    letter_body = models.CharField(max_length=5000)
    
    def __unicode__(self):
        return self.letter_title
