from django.urls import path
from backend import views

urlpatterns = [
    path('employees', views.employee_list,name='employee-list'),
    path('employee/<int:id>', views.employee_detail),
    path('employee/task/<int:id>', views.employee_task),
    path('employee/get/task/list', views.employee_task_list),
    path('employee/upload/doc/<int:id>', views.employee_upload_document),
    path('employees/get/document',views.employees_list_doc),
    path('employee/get/documents/<int:id>',views.employee_list_docs)
    
]
