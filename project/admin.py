from django.contrib import admin
from .models import Project, Contract



# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ('serial_number',
                    'name',
                    )
    #fields = ('')
    
class ContractAdmin(admin.ModelAdmin):
    model = Contract
    list_display = ('serial_number',
                 'name',)

    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contract, ContractAdmin)
