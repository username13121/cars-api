from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from cars.filters import CarFilter
from cars.models import Car
from cars.serializers import CarSerializer
from src.permissions import ReadOnlyOrIsAdmin


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = CarFilter

    permission_classes = (ReadOnlyOrIsAdmin,)
