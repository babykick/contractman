from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from .models import Contract
from .forms import ContractForm
# Create your views here.

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
 
class ContractsListView(ListView):
    model = Contract
    context_object_name = "contracts"
    template_name = "contract/list.html"
    
