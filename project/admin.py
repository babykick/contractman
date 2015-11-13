from django.contrib import admin
from .models import Project



# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('serial_number',
                    'name',
                    )
    #fields = ('')
    
admin.site.register(Project, ProjectAdmin)