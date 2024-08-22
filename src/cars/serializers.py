from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id',
                  'brand',
                  'model',
                  'fuel_type',
                  'transmission_type',
                  'year',
                  'mileage',
                  'price')
