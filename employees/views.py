from django.db.models import Count
from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeListDetailView


class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Employee.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListDetailView
        return EmployeeSerializer


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Employee.objects.all()
    
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListDetailView
        return EmployeeSerializer


class EmployeeStatisticView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Employee.objects.all()

    def get(self, request):
        total_employees = self.queryset.count()
        total_by_gender = self.queryset.values("gender").annotate(count=Count("id"))
        employee_by_category = self.queryset.values("employee_category").annotate(
            count=Count("id")
        )
        employee_by_academic_level = self.queryset.values("academic_level").annotate(
            count=Count("id")
        )

        return response.Response(
            data={
                "total_employees": total_employees,
                "total_by_gender": total_by_gender,
                "employee_by_category": employee_by_category,
                "employee_by_academic_level": employee_by_academic_level,
            },
            status=status.HTTP_200_OK,
        )
