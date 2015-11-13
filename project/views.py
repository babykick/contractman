from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponse
from .models import Project, Contract
from .forms import ContractForm, WorkOrderForm, ProjectForm
# Create your views here.
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
         

class ProjectFormView(FormView):
    template_name = "main/addProject.html"
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
    context_object_name = "projects"
    template_name = "main/projectlist.html"
    
class ProjectDetailView(DetailView):
    model = Project
   
   
class ContractFormView(FormView):
    template_name = "main/addcontract.html"
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
    template_name = "main/contractlist2.html"
    

class WorkOrderFormView(FormView):
    template_name = "main/addworkorder.html"
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
    template_name = "main/wordorderlist.html"
    

