from django.urls import path
from crm_management_app.api.v1 import department_views

urlpatterns = [
    path('departments', department_views.department_api, name='department_api'),
    path('department/<int:id>', department_views.department_api,
         name='department_api_detail')
]
