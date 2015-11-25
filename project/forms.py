#coding=utf-8
from django.forms import ModelForm
from .models import Project, Contract, WorkOrder



class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('serial_number',
                  'name',
                  'intro',
                  'pm',
                  'budget',
                  'material_cost',
                  'construction_cost',
                  'supervision_cost',
                  'coordination_cost',
                  'other_cost',
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