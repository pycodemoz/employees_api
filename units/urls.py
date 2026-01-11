from django.urls import path

from units.views import (
    UnitListCreateView,
    UnitRetrieveUpdateDestroyView,
    UnitStatisticView,
)

urlpatterns = [
    path("units/", UnitListCreateView.as_view(), name="units_list"),
    path(
        "units/<int:pk>/",
        UnitRetrieveUpdateDestroyView.as_view(),
        name="unit-detail-view",
    ),
    path("units/statistic/", UnitStatisticView.as_view(), name="unit-statistic-view"),
]
