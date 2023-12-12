from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from crm_management_app.models import Employees
from crm_management_app.serializers.employee_serializer import EmployeeSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_api(request, id=0):
    # GET request to retrieve all employees
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    # POST request to add a new employee
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse({"error": "Failed to add"}, status=status.HTTP_400_BAD_REQUEST, safe=False)

    # PUT request to update an existing employee
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        try:
            employee = Employees.objects.get(
                EmployeeId=employee_data['EmployeeId'])
        except Employees.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)

        employees_serializer = EmployeeSerializer(
            employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse({"message": "Update Successfully"}, safe=False)
        return JsonResponse({"error": "Failed to update"}, status=status.HTTP_400_BAD_REQUEST, safe=False)

    # DELETE request to delete an existing employee
    elif request.method == 'DELETE':
        try:
            employee = Employees.objects.get(EmployeeId=id)
        except Employees.DoesNotExist:
            return JsonResponse({"error": "employee not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)

        employee.delete()
        return JsonResponse({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT, safe=False)
