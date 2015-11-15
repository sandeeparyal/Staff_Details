# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic

from kapra.models import Ministry, HeadSection, Section, Employee, LettersTemplate
from kapra.forms import LetterForm


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'kapra/index.html'
    context_object_name = 'output'

    def get_queryset(self):
        return Ministry.objects.all()

def headsection_listings(request, word): #here word has in it the id from the ministry name
    head_section_list = HeadSection.objects.all()
    head_section_name = [p.head_section_name for p in head_section_list if p.ministry.id == int(word)]
    no_of_employees = [str(p.no_of_employees) for p in head_section_list if p.ministry.id == int(word)]
    context = {'head_section_name':head_section_name, 'no_of_employees': no_of_employees}
    return render(request, 'kapra/headsection_list.html', context)

def section_listings(request, hsection):
    section_list = Section.objects.all()
    section_name = [p.section_name for p in section_list if p.headsection.head_section_name == hsection]
    context = {'section_name':section_name, 'hsection':hsection}
    return render(request, 'kapra/section_list.html', context)

def employee_listings(request, hsection, section):
    employee_list = Employee.objects.all()
    employee_id = [p.emp_id for p in employee_list if p.section.section_name == section]
    employee_name = [p.emp_first_name +' ' +  p.emp_last_name for p in employee_list if p.section.section_name == section]
    context = {'employee_name':employee_name, 'section':section, 'employee_id':employee_id}
    return render(request, 'kapra/employee_list.html', context)

def letters(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter_contents = form.save()
            generate_letter(form)
            form.save()     
            return render(request, 'kapra/thanks.html')
        else:
            return render(request, 'kapra/letters.html')
    else:
        form = LetterForm()
        return render(request, 'kapra/contact.html', {'form' : form, })

def generate_letter(form):
    f = (open("file1.txt","w"))
    f.write(form.data['letter_number'].encode('utf-8'))
    f.write('\n'+form.data['letter_date'].encode('utf-8'))
    f.write('\n'+form.data['letter_title'].encode('utf-8'))
    f.write('\n'+form.data['letter_body'].encode('utf-8'))
    f.write('\n'+form.data['letter_date'].encode('utf-8'))
    f.close()
    pass

