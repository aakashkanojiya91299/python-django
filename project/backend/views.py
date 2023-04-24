from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .managers import EmployeeManager
import json

employee_manager = EmployeeManager()

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        employees = employee_manager.get_employees()
        return JsonResponse({'employees': employees}, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        employee_manager.create_employee(data)
        return JsonResponse({'status': 'Employee created successfully'})
    else:
        return JsonResponse({'status': 'method not foun'},status=404)
 

@csrf_exempt
def employee_task(request,id):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee_tasks = employee_manager.create_employee_task(id,data)
        return JsonResponse({'status': 'Task created successfully'})
    else:
        return JsonResponse({'status': 'method not foun'},status=404)


@csrf_exempt
def employee_task_list(request):
    if request.method == 'GET':
        employees = employee_manager.get_employees_tasks()
        return JsonResponse({'employees': employees}, safe=False)
    else:
        return JsonResponse({'status': 'method not foun'},status=404)


@csrf_exempt
def employee_detail(request, id):
    if request.method == 'GET':
        employee = employee_manager.get_employee(id)
        return JsonResponse({'employee': employee}, safe=False)
    elif request.method == 'PUT':
        data = request.PUT.dict()
        employee_manager.update_employee(id, data)
        return JsonResponse({'status': 'Employee updated successfully'})
    elif request.method == 'DELETE':
        employee_manager.delete_employee(id)
        return JsonResponse({'status': 'Employee deleted successfully'})
    else:
        return JsonResponse({'status': 'method not foun'},status=404)