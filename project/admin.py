from django.contrib import admin
from .models import Project
from company.models import Department


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('serial_number',
                    'name',
                    )
    #fields = ('')
    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Department, DepartmentAdmin)