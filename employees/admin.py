from django.contrib import admin

from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "gender",
        "tax_number",
        "id_number",
        "academic_level",
        "employee_category",
        "place_of_work",
    )
    search_fields = ["id_number", "tax_number"]

    def __str__(self):
        return self.name
