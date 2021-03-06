# -*- coding: utf-8 -*-
import os

import csv
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from kapra.models import Ministry, HeadSection, Section, Employee



# Create your views here.

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class IndexView(LoggedInMixin, generic.ListView):
    template_name = 'kapra/index.html'
    context_object_name = 'output'
    
    def get_queryset(self):
        return Ministry.objects.all()


@login_required
def headsection_listings(request, ministry_id): #here word has in it the id from the ministry name
    head_section_list = HeadSection.objects.filter(ministry__id=int(ministry_id))
    context = {'head_section_list':head_section_list, 'ministry_id':ministry_id}
    return render(request, 'kapra/headsection_list.html', context)

@login_required
def section_listings(request, ministry_id, head_section_id):
    section_list = Section.objects.filter(headsection__id=int(head_section_id))
    context = {'section_list':section_list, 'head_section_id':head_section_id, 'ministry_id':ministry_id }
    return render(request, 'kapra/section_list.html', context)

@login_required
def employee_listings(request, ministry_id, head_section_id, section_id):
    employee = Employee.objects.filter(section__id=int(section_id)).order_by('emp_sewa', 'emp_class','designation')
    duration = [x.employee_duration() for x in employee]
    employee_list = zip(employee, duration)
    
    context = {'employee_list':employee_list}
    return render(request, 'kapra/employee_list.html', context)

@login_required
def search_by_id(request):
    try:    
        employee = Employee.objects.get(emp_id=request.POST['search_id'])
        context = {"employee": employee}
    except:
        employee = "No employee found"
        context = {"employee": employee}
    return render(request, 'kapra/search_by_id_result.html', context)

@login_required
def generate_pdf(request, ministry_id, head_section_id, section_id):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="employee.txt"'
    writer = csv.writer(response)
    employee_list = Employee.objects.filter(section__id=int(section_id)).order_by('emp_sewa')
    writer.writerow(["नाम"+'\t' + "पद"])
    for x in employee_list:
        writer.writerow([str(x.emp_first_name.encode('utf-8'))+' ' + str(x.emp_last_name.encode('utf-8'))+'\t' + str(x.designation.encode('utf-8'))+'\t'])
    return response


