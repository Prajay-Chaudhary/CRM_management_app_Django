from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from crm_management_app.models import Departments
from crm_management_app.serializers import DepartmentSerializer


@csrf_exempt
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
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    # PUT request to update an existing department
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        try:
            department = Departments.objects.get(
                DepartmentId=department_data['DepartmentId'])
        except Departments.DoesNotExist:
            return JsonResponse("Department not found", status=404)

        departments_serializer = DepartmentSerializer(
            department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    # DELETE request to delete an existing department
    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentId=id)
        except Departments.DoesNotExist:
            return JsonResponse("Department not found", status=404)

        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
