from django.urls import path

from employees.views import (
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
    EmployeeStatisticView,
)

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view(), name="employees_list"),
    path(
        "employee/<int:pk>/",
        EmployeeRetrieveUpdateDestroyView.as_view(),
        name="employee-detail-view",
    ),
    path(
        "employees/statistic/",
        EmployeeStatisticView.as_view(),
        name="employee_statistic",
    ),
]
