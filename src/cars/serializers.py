from rest_framework import serializers

from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(
        max_length=63,
        help_text='Производитель авотомобиля',
        default='McLaren'
    )

    model = serializers.CharField(
        max_length=63,
        help_text='Модель авотомобиля',
        default='MP4/4'
    )

    year = serializers.IntegerField(
        help_text='Год выпуска',
        default=1988
    )

    mileage = serializers.IntegerField(
        help_text='Пробег в км',
        default=5000
    )
    price = serializers.IntegerField(
        help_text='Цена',
        default=4800000
    )

    class Meta:
        model = Car
        fields = ('id',
                  'brand',
                  'model',
                  'fuel_type',
                  'transmission',
                  'year',
                  'mileage',
                  'price')
