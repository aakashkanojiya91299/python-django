from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .managers import EmployeeManager

employee_manager = EmployeeManager()

@csrf_exempt
def employee_list(request):
    if request.method == 'GET':
        employees = employee_manager.get_employees()
        return JsonResponse({'employees': employees}, safe=False)
    elif request.method == 'POST':
        data = request.POST.dict()
        employee_manager.create_employee(data)
        return JsonResponse({'status': 'Employee created successfully'})

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