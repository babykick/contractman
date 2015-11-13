from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from .models import Project, Contract
from .forms import ContractForm, WorkOrderForm, ProjectForm
# Create your views here.



class ProjectFormView(FormView):
    template_name = "contract/addProject.html"
    form_class = ProjectForm
    
    def post(self, request, *args, **kwargs):
        print "in"
        form = self.get_form(self.form_class)
        if form.is_valid():
            item = form.save()
            return redirect("/list") #self.form_valid(form, **kwargs)
           
        else:
            return self.form_invalid(form, **kwargs)
 
 
class ProjectListView(ListView):
    model = Project
    context_object_name = "contracts"
    template_name = "contract/projectlist.html"
    


class ContractFormView(FormView):
    template_name = "contract/addcontract.html"
    form_class = ContractForm
    
    def post(self, request, *args, **kwargs):
        print "in"
        form = self.get_form(self.form_class)
        if form.is_valid():
            item = form.save()
            return redirect("/list") #self.form_valid(form, **kwargs)
           
        else:
            return self.form_invalid(form, **kwargs)
 


class ContractListView(ListView):
    model = Contract
    context_object_name = "contracts"
    template_name = "contract/contractlist2.html"
    

class WorkOrderFormView(FormView):
    template_name = "contract/addworkorder.html"
    form_class = WorkOrderForm
    
    def post(self, request, *args, **kwargs):
        print "in"
        form = self.get_form(self.form_class)
        if form.is_valid():
            item = form.save()
            return redirect("/contracts") 
        else:
            return self.form_invalid(form, **kwargs)
 
class WorkOrdersListView(ListView):
    model = Contract
    context_object_name = "workorders"
    template_name = "contract/wordorderlist.html"
    

