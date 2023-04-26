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
    elif request.method == 'PUT':
        if(request.GET.get('taskId') != None ):
            data = json.loads(request.body)
            employees = employee_manager.update_employee_task(id,data,request.GET.get('taskId'))
            return JsonResponse({'employees': employees}, safe=False)
        else:
            return JsonResponse({"error":"taskId Missing"},status=404)
    else:
        return JsonResponse({'status': 'method not foun'},status=404)
    

@csrf_exempt
def employee_task_list(request):
    if(request.GET.get('id') != None):
        if request.method == 'GET':
            employees = employee_manager.get_employees_tasks_by_id(request.GET.get('id'))
            return JsonResponse({'employees': employees}, safe=False)
        else:
            return JsonResponse({'status': 'method not foun'},status=404)
    else:
        if request.method == 'GET':
            employees = employee_manager.get_employees_tasks()
            return JsonResponse({'employees': employees}, safe=False)
        else:
            return JsonResponse({'status': 'method not foun'},status=404)


@csrf_exempt
def employee_upload_document(request,id):
    if request.method == 'POST':
        file = request.FILES['pdf']
        documentType = request.GET.get('type')
        document = file.read()

        # Save the PDF in the database
        pdf_id = employee_manager.save_employee_document(id,documentType,document)
        return JsonResponse({'pdf_id': pdf_id})
    else:
        return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def employees_list_doc(request):
    if request.method == 'GET':
        employees_doc = employee_manager.get_employees_doc()
        return JsonResponse({'employees_doc': employees_doc}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})



@csrf_exempt
def employee_list_docs(request,id):
    if request.method == 'GET':
        employees_doc = employee_manager.get_employee_doc(id)
        return JsonResponse({'employees_doc': employees_doc}, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'})



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