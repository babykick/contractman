from django.contrib import admin
from .models import Department, Member



# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',
                    )
    
    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Member, MemberAdmin)