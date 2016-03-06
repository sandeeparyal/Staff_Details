# -*- coding: utf-8 -*-

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
    GENDER_CHOICES = (
						('M','Male'),('F','Female'))
    EMPLOYEE_SEWA_CHOICES = (
                            ('prasashan', 'Nepal Prasashan'),
                            ('engineering', 'Nepal Engineering'),
                            ('bibidh', 'Nepal Bibidh'),('sikshya', 'Nepal Sikshya'),
                            ('anya', 'Anya')
                            )
    EMPLOYEE_SAMUHA_CHOICES = (
                            ('samanya_prasashan', 'Samanya Prasashan'),
                            ('civil_engineering', 'Civil'),
                            ('anya', 'Anya')
                            ) 
           
    EMPLOYEE_CLASS_CHOICES = (
                            ('bisistha', 'Bisistha'),
                            ('gazzetted_first_class', 'Gazzetted First'),
                            ('gazzetted_second_class', 'Gazzetted Second'),
                            ('gazzetted_third_class', 'Gazzetted Third'),
                            ('non_gazzetted_first_class', 'Non Gazzetted First'),
                            ('non_gazzetted_second_class', 'Non Gazzetted Second'),
                            ('non_gazzetted_third_class', 'Non Gazzetted Third'),
                            ('non_class', 'Shreni Bihin'),
                            ('anya', 'Anya'),
                            )

    section = models.ForeignKey(Section)
    emp_id = models.CharField(max_length=10, unique=True)
    emp_first_name = models.CharField(max_length=100)
    emp_middle_name = models.CharField(max_length=100, blank=True)
    emp_last_name = models.CharField(max_length=100)
    emp_gender = models.CharField(max_length=4, choices=GENDER_CHOICES)
    emp_sewa = models.CharField(max_length=100, choices=EMPLOYEE_SEWA_CHOICES) 
    emp_samuha = models.CharField(max_length=100, choices=EMPLOYEE_SAMUHA_CHOICES, blank=True)
    emp_upasamuha = models.CharField(max_length=100, blank=True)
    emp_class = models.CharField(max_length=50, choices=EMPLOYEE_CLASS_CHOICES, blank=True)
    designation = models.CharField(max_length=100) #Section-Officer, Nasu etc
    post = models.CharField(max_length=50, blank=True) #Special
    emp_joined_date = models.DateField('Employee Joined Date')
    emp_depart_date = models.DateField('Employee Departed Date', blank=True)
    emp_status = models.CharField(max_length=50, blank=True)
    emp_phone = models.CharField(max_length=12, blank=True)
    emp_type = models.CharField(max_length=4, choices=EMPLOYEE_TYPE_CHOICES)
    
    def __unicode__(self):
        return self.designation

    def employee_duration(self):
        return timezone.datetime.now()


