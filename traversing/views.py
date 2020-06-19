from django.shortcuts import render
from traversing.forms import EmployeeForm
from django.template.context_processors import csrf
# Create your views

def index(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)     #saving the instance

        if employee_form.is_valid():
            form = employee_form.save()
            return redirect('index')

    else:
        employee_form = EmployeeForm()
    args = {}
    args.update(csrf(request))
    args['employee_form'] = employee_form

    return render(request, "index.html", args)
