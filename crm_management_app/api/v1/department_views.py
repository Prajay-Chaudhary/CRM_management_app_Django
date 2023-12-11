from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from crm_management_app.models import Departments
from crm_management_app.serializers.department_serializer import DepartmentSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def department_api(request, id=0):
    # GET request to retrieve all departments
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    # POST request to add a new department
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse({"message": "Added Successfully"}, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse({"error": "Failed to add"}, status=status.HTTP_400_BAD_REQUEST, safe=False)

    # PUT request to update an existing department
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        try:
            department = Departments.objects.get(
                DepartmentId=department_data['DepartmentId'])
        except Departments.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)

        departments_serializer = DepartmentSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse({"message": "Update Successfully"}, safe=False)
        return JsonResponse({"error": "Failed to update"}, status=status.HTTP_400_BAD_REQUEST, safe=False)

    # DELETE request to delete an existing department
    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentId=id)
        except Departments.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=status.HTTP_404_NOT_FOUND, safe=False)

        department.delete()
        return JsonResponse({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT, safe=False)
