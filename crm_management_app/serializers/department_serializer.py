from rest_framework import serializers
from crm_management_app.models import Departments

# Serializer for Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ("DepartmentId", "DepartmentName")
