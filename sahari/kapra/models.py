from django.db import models
from django.utils import timezone

# Create your models here.

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=200)
    ministry_location = models.CharField(max_length=200)

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
    section = models.ForeignKey(Section)
    emp_id = models.CharField(max_length=10)
    emp_first_name = models.CharField(max_length=50)
    emp_middle_name = models.CharField(max_length=50)
    emp_last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    emp_joined_date = models.DateTimeField('Employee Joined Date')
    emp_depart_date = models.DateTimeField('Employee Departed Date')
    emp_status = models.CharField(max_length=50)
    emp_phone = models.CharField(max_length=12)
    emp_type = models.CharField(max_length=4)
    
    def __unicode__(self):
        return self.designation

    def employee_duration(self):
        return timezone.datetime.now()


class LettersTemplate(models.Model):
    TITLE_CHOICES = (
                     ('Appointment', 'Niyukti'), ('Transfer', 'Saruwa'))
    employee = models.ForeignKey(Employee)
    letter_number = models.IntegerField(default=0)
    letter_type = models.IntegerField(default=0)
    letter_date = models.DateTimeField('date published')
    letter_title = models.CharField(max_length=200, choices=TITLE_CHOICES)
    letter_body = models.CharField(max_length=5000)
    
    def __unicode__(self):
        return self.letter_title
