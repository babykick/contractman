from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponse
from .models import Project, Contract
from company.models import Department
from .forms import ContractForm, WorkOrderForm, ProjectForm
# Create your views here.
from django.views.generic import View


class IndexView(ListView):
    context_object_name = "departments"
    template_name = "index.html"
    model = Department



class ProjectFormView(FormView):
    template_name = "main/addProject.html"
    form_class = ProjectForm
    
    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            item = form.save()
            return redirect("/projects") #self.form_valid(form, **kwargs)
           
        else:
            return self.form_invalid(form, **kwargs)
 
 
class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "main/projectlist.html"
    
    def get_queryset(self):
        dept_pk = self.request.GET.get('dept')
        if dept_pk:
            #dept = get_object_or_404(Department, dept_pk)
            return Project.objects.filter(department=dept_pk)
        else:
            return Project.objects.all()
    
    
class ProjectDetailView(DetailView):
    model = Project
   
   
class ContractFormView(FormView):
    template_name = "main/addcontract.html"
    form_class = ContractForm
   
    def form_valid(self, form):
        print self.kwargs
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        print project
        if project:
            form.instance.project = project
            form.save()
            return super(ContractFormView, self).form_valid(form)
        
    
    def get_success_url(self):
        return "/project/{0}".format(self.kwargs['pk'])
        
        # form = self.get_form(self.form_class)
        # if form.is_valid():
        #     item = form.save()
        #     return redirect("/project/{0}".format(self.kwargs['pk'])) #self.form_valid(form, **kwargs)
        #    
        # else:
        #     return self.form_invalid(form, **kwargs)
 


class ContractListView(ListView):
    model = Contract
    context_object_name = "contracts"
    template_name = "main/contractlist.html"
    
    #def get_queryset(self):
        #publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
        #return Contract.objects.filter(project=self.kwargs['pk'])

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
    

