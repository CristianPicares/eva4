from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse

from empleados.models import Employee

# Create your views here.
def employeeView(request):
    emp = {
        'id' : 123,
        'name' : 'Cristian',
        'email' : 'cristian@neworg.cl',
        'salary' : '500000'
    }
    empleados = Employee.objects.all()

    data = {'employees' : list(empleados.values('name','salary'))}
    return JsonResponse(data)