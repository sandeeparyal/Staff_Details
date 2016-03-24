from django.contrib import admin
from django.utils import timezone
from kapra.models import Ministry, HeadSection, Section, Employee 

# Register your models here.

class HeadSectionInline(admin.TabularInline):
    model = HeadSection
    extra = 3

class MinistryAdmin(admin.ModelAdmin):
    fields = ['ministry_name', 'ministry_location']
    inlines = [HeadSectionInline]
    

admin.site.register(Ministry, MinistryAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    identity = (('emp_id', 'emp_gender'), ('emp_first_name', 'emp_middle_name', 'emp_last_name'))
    sewa = ('emp_sewa', 'emp_samuha', 'emp_upasamuha')
    status = (('emp_joined_date', 'emp_depart_date', 'emp_status'),)
    phone= ('emp_phone1','emp_phone2')
    fieldsets = [('Employee Identity', {'fields': identity}), 
                 ('Employee Position', {'fields': (sewa,  ('emp_class', 'designation', 'emp_type'))}),
                 ('Period',{'fields':status}),
                 ('Contact',{'fields':(phone,)}),
                 ('Section', {'fields':['section']})]

                
#admin.site.register(HeadSection)
admin.site.register(Section)
#admin.site.register(HeadSection, Section)
admin.site.register(Employee, EmployeeAdmin)

