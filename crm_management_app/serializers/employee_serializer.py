from rest_framework import serializers
from crm_management_app.models import Employees

# Serializer for Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department',
                  'DateOfJoining', 'PhotoFileName')
