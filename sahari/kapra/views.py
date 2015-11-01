from django.shortcuts import render
from django.core.urlresolvers import reverse
from kapra.models import Ministry, HeadSection, Section, Employee, LettersTemplate
from kapra.forms import LetterForm


# Create your views here.

def index(request):
    output = Ministry.objects.all()
    
    context = {'output':output}
    return render(request, 'kapra/index.html', context)

def headsection_listings(request, word):
    head_section_list = HeadSection.objects.all()
    head_section_name = [p.head_section_name for p in head_section_list if p.ministry.id == int(word)]
    no_of_employees = [str(p.no_of_employees) for p in head_section_list if p.ministry.id == int(word)]
    context = {'head_section_name':head_section_name, 'no_of_employees': no_of_employees}
    return render(request, 'kapra/headsection_list.html', context)

def section_listings(request, hsection):
    section_list = Section.objects.all()
#    import pdb; pdb.set_trace()
    section_name = [p.section_name for p in section_list if p.headsection.head_section_name == hsection]
    context = {'section_name':section_name, 'hsection':hsection}
    return render(request, 'kapra/section_list.html', context)

def employee_listings(request, hsection, section):
    #import pdb; pdb.set_trace()
    employee_list = Employee.objects.all()
    employee_id = [p.emp_id for p in employee_list if p.section.section_name == section]
    employee_name = [p.emp_first_name +' ' +  p.emp_last_name for p in employee_list if p.section.section_name == section]
    #    import pdb; pdb.set_trace()
    context = {'employee_name':employee_name, 'section':section, 'employee_id':employee_id}
    return render(request, 'kapra/employee_list.html', context)

def letters(request, employee_id):
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter_title = str(form.data['letter_title'])
            context = {'letter_title':letter_title}
            letter_contents = form.save()     
            return render(request, 'kapra/thanks.html', context)
        else:
            return render(request, 'kapra/letters.html')
    else:
        form = LetterForm()
        return render(request, 'kapra/contact.html', {'form' : form, })
'''letter_number = models.IntegerField(default=0)
    letter_type = models.IntegerField(default=0)
    letter_date = models.DateTimeField('date published')
    letter_title = models.CharField(max_length=200)
    letter_body = models.CharField(max_length=5000)
'''


