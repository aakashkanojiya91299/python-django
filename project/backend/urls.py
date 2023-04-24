from django.urls import path
from backend import views

urlpatterns = [
    path('employees', views.employee_list,name='employee-list'),
    path('employee/task/<int:id>', views.employee_task),
    path('employee/get/task/list', views.employee_task_list)

]
