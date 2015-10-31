from django.contrib import admin
from django.utils import timezone
from kapra.models import Ministry, HeadSection, Section, Employee, LettersTemplate; 

# Register your models here.

#class SectionInline(admin.TabularInline):
#    model = Section
#    extra = 2

class HeadSectionInline(admin.TabularInline):
    model = HeadSection
#    inlines = [SectionInline]
    extra = 3



class MinistryAdmin(admin.ModelAdmin):
    fields = ['ministry_name', 'ministry_location']
    inlines = [HeadSectionInline]
    

admin.site.register(Ministry, MinistryAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = [('Section', {'fields':['section']}),
                 ('Employee Name', {'fields': ['emp_id', 'emp_first_name', 'emp_middle_name', 'emp_last_name'], 'classes':['collapse']}), 
                 ('Employee Position', {'fields': ['designation', 'emp_joined_date', 'emp_depart_date', 'emp_status', 
                        'emp_phone', 'emp_type']})]

                
#admin.site.register(HeadSection)
admin.site.register(Section)
#admin.site.register(HeadSection, Section)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(LettersTemplate)


