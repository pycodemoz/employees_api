from rest_framework import generics, response, status, views
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultPermission
from units.models import Unit
from units.serializers import UnitSerializer


class UnitListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitStatisticView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Unit.objects.all()

    def get(self, request):
        total_units = self.queryset.count()

        return response.Response(
            data={
                "total_units": total_units,
            },
            status=status.HTTP_200_OK,
        )
