#coding=utf-8
from django.forms import ModelForm
from .models import Project, Contract, WorkOrder



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('serial_number',
                  'name',
                  'intro',
                  'department'
                )
        

class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = ('serial_number',
                  'name',
                  'content',
                  'fundlimit',
                  'timeline',
                  'partA',
                  'partB')
        
        
class WorkOrderForm(ModelForm):
    class Meta:
        model = WorkOrder
        fields = ('serial_number',
                  'name',
                  'content',
                  'budget',
                  )