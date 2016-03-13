# -*- coding: utf-8 -*-
import os

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

from kapra.models import Ministry, HeadSection, Section, Employee



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'kapra/index.html'
    context_object_name = 'output'

    def get_queryset(self):
        return Ministry.objects.all()

def headsection_listings(request, ministry_id): #here word has in it the id from the ministry name
    head_section_list = HeadSection.objects.filter(ministry__id=int(ministry_id))
    context = {'head_section_list':head_section_list}
    return render(request, 'kapra/headsection_list.html', context)

def section_listings(request, headsection_id):
    section_list = Section.objects.filter(headsection__id=headsection_id)
    context = {'section_list':section_list, 'headsection_id':headsection_id }
    return render(request, 'kapra/section_list.html', context)

def employee_listings(request, headsection_id, section_id):
    employee_list = Employee.objects.filter(section__id=section)
    employee_id = [p.emp_id for p in employee_list if p.section.section_name == section]
    employee_name = [p.emp_first_name +' ' +  p.emp_last_name for p in employee_list if p.section.section_name == section]
    context = {'employee_name':employee_name, 'section':section, 'employee_id':employee_id}
    return render(request, 'kapra/employee_list.html', context)


