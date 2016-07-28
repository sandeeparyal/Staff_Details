# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=200, verbose_name='मन्त्रालयको नाम')
    ministry_location = models.CharField(max_length=200, blank=True, verbose_name='ठेगाना')

    def __unicode__(self):
        return self.ministry_name


class HeadSection(models.Model):
    ministry = models.ForeignKey(Ministry, verbose_name='मन्त्रालय')
    head_section_name = models.CharField(max_length=150, verbose_name='महाशाखाको नाम')
    no_of_employees = models.IntegerField(default=0, verbose_name='कर्मचारी स‌ङ्ख्या')

    def __unicode__(self):
        return self.head_section_name


class Section(models.Model):
    headsection = models.ForeignKey(HeadSection, verbose_name='महाशाखा')
    section_name = models.CharField(max_length=150, verbose_name='शाखाको नाम')
    no_of_employees = models.IntegerField(default=0, verbose_name='कर्मचारी स‌ङ्ख्या')

    def __unicode__(self):
        return self.section_name


class Employee(models.Model):
    EMPLOYEE_TYPE_CHOICES = (
                             ('perm', 'स्थायी'), ('temp', 'करार'))
    GENDER_CHOICES = (
						('M','पुरुष'),('F','महिला'))
    EMPLOYEE_SEWA_CHOICES = (
                            ('1', 'नेपाल प्रशासन'),
                            ('2', 'न्याय'),
                            ('3', 'लेखा' ),
                            ('4', 'नेपाल ईन्जिनियरिङ्ग' ),
                            ('5', 'विविध' ),
                            ('6', 'शिक्षा' ),
                            ('7', 'अन्य'),
        )
    EMPLOYEE_SAMUHA_CHOICES = (
                            ('1', 'सामान्य प्रशासन'),
                            ('2', 'कानून'),
                            ('3','सिभिल'),
                            ('4','अन्य'),
             ) 
           
    EMPLOYEE_CLASS_CHOICES = (
                            ('1', 'विशिष्ट'),
                            ('2', 'रा.प.प्रथम'),
                            ('3', 'रा.प.द्वितिय'),
                            ('4', 'रा.प.तृतिय'),
                            ('5', 'रा.प.अनं.प्रथम'),
                            ('6', 'रा.प.अनं.द्धितिय'),
                            ('7', 'रा.प.अनं.तृतिय'),
                            ('8', 'श्रेणी विहिन'),
                            ('9', 'अन्य'),
         )
    DESIGNATION_CHOICES = (
                            ('1', 'सचिव'),
                            ('2', 'सहसचिव'),
                            ('3','सु इ'),
                            ('4', 'उपसचिव'),
                            ('5', 'वरीष्ठ समाजशास्त्री'),
                            ('6', 'सि डि इ'),
                            ('7', 'शाखा अधिकृत'),                
                            ('8','इन्जिनियर'),                
                            ('9', 'नायव सुब्बा'),
                            ('10', 'कम्प्युटर अपरेटर'),
                            ('11', 'पुस्तकालय सहायक'),
                            ('12', 'खरिदार'),
                            ('13','हलुका सवारी चालक'),
                            ('14','कार्यालय सहयाेगी'),
                            ('15', 'अन्य'),
         )
    STATUS_CHOICES = (
                            ('1', 'कार्यरत'),
                            ('2', 'काज'),
			    ('3', 'बिदा'),
			    ('4', 'निलम्बन'),
         )
    section = models.ForeignKey(Section, verbose_name='शाखा')
    emp_id = models.CharField(max_length=10, unique=True, verbose_name='कर्मचारी स‌ङ्केत न‌')
    emp_title = models.CharField(max_length=100, default='श्री', verbose_name='Title')
    emp_first_name = models.CharField(max_length=100, verbose_name='नाम')
    emp_middle_name = models.CharField(max_length=100, blank=True, verbose_name='बीचको नाम')
    emp_last_name = models.CharField(max_length=100, verbose_name='थर')
    emp_gender = models.CharField(max_length=4, choices=GENDER_CHOICES, verbose_name='लिङ्ग')
    emp_sewa = models.CharField(max_length=100, choices=EMPLOYEE_SEWA_CHOICES, verbose_name='सेवा') 
    emp_samuha = models.CharField(max_length=100, choices=EMPLOYEE_SAMUHA_CHOICES, blank=True, verbose_name='समूह')
    emp_upasamuha = models.CharField(max_length=100, blank=True, verbose_name='उपसमूह')
    emp_class = models.CharField(max_length=50, choices=EMPLOYEE_CLASS_CHOICES, blank=True, verbose_name='श्रेणी')
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES, verbose_name='पद') #Section-Officer, Nasu etc
    post = models.CharField(max_length=50, blank=True) #Special
    emp_joined_date = models.DateField(verbose_name='हाजिरी मिति')
    emp_depart_date = models.DateField(blank=True, verbose_name='रमाना मिति')
    emp_status = models.CharField(max_length=50, blank=True, choices=STATUS_CHOICES, default=1, verbose_name='कार्यरत अवस्था')
    emp_phone1 = models.CharField(max_length=12, blank=True, verbose_name='फोन१')
    emp_phone2 = models.CharField(max_length=12, blank=True, verbose_name='फोन२')
    emp_address = models.CharField(max_length=12, blank=True, verbose_name='ठेगाना')
    emp_type = models.CharField(max_length=4, choices=EMPLOYEE_TYPE_CHOICES, verbose_name='दरबन्दीको किसिम')
    
    def __unicode__(self):
        return (self.emp_id + " " + self.emp_first_name +' '+ self.emp_last_name)

    def employee_duration(self):
	if (not self.emp_depart_date):
            date_difference = datetime.now() - self.emp_joined_date
	else:
	    date_difference = self.emp_depart_date - self.emp_joined_date
	if date_difference.days < 0:
	    return "Invalid"            
	else:
	    return date_difference.days


