from django.contrib import admin

from units.models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "address")
    search_fields = ["name"]

    def __str__(self):
        return self.name
