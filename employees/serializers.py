from datetime import date
from rest_framework import serializers
from units.serializers import UnitSerializer
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

    
class EmployeeListDetailView(serializers.ModelSerializer):
    place_of_work = UnitSerializer()
    length_service = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Employee
        fields = ['id', 'name', 'birthday', 'gender', 'academic_level', 'course', 'id_number', 'tax_number', 'employee_category', 'entry_date', 'place_of_work', 'length_service']
        
    def get_length_service(self, obj):
        if not obj.entry_date:
            return None

        today = date.today()
        years = today.year - obj.entry_date.year

        # Se ainda não completou o ano atual
        if (today.month, today.day) < (obj.entry_date.month, obj.entry_date.day):
           years -= 1

        return years
