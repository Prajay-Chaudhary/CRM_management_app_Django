from django.urls import path
from crm_management_app.api.v1 import department_views, employee_views

urlpatterns = [
    # Paths for department
    path('departments', department_views.department_api, name='department_api'),
    path('department/<int:id>', department_views.department_api,
         name='department_api_detail'),

    # Paths for employee
    path('employees', employee_views.employee_api, name='employee_api'),
    path('employee/<int:id>', employee_views.employee_api,
         name='employee_api_detail')
]
