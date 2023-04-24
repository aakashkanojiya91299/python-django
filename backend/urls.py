from django.urls import path
from backend import views

urlpatterns = [
    path('employees/', views.employee_list),
]
