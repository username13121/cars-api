import re

import django_filters

from cars.models import Car


class CarFilter(django_filters.FilterSet):
    brand = django_filters.BaseInFilter(method='filter_words')
    model = django_filters.BaseInFilter(method='filter_words')

    fuel_type = django_filters.MultipleChoiceFilter(choices=Car.FuelTypeChoices.choices)
    transmission = django_filters.ChoiceFilter(choices=Car.TransmissionChoices.choices)

    min_year = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='year', lookup_expr='lte')

    min_mileage = django_filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    max_mileage = django_filters.NumberFilter(field_name='mileage', lookup_expr='lte')

    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    @staticmethod
    def filter_words(queryset, name, value):
        """
        Фильтр по отдельным словам, не регистрозависимый. Использовать только с BaseInFilter()

        Почему не __iexact? Нужен поиск по словам, чтобы можно было найти "Mercedes-benz" по слову "mercedes"
        Почему не __icontains? Коллизии, если бы появился автопроизводитель "Yota", поиск выдал бы еще и "Toyota"
        """

        if value is None:
            return queryset

        # Escape нужен для удаления спец символов
        value = (re.escape(val) for val in value)

        # "\b" для поиска отдельного слова. "?:" чтобы не хранить группу в памяти
        regex_pattern = rf'\b(?:{'|'.join(value)})\b'

        return queryset.filter(**{
            f'{name}__iregex': regex_pattern
        })

    class Meta:
        model = Car
        fields = ('brand',
                  'model',
                  'min_year',
                  'year',
                  'max_year',
                  'min_mileage',
                  'max_mileage',
                  'min_price',
                  'max_price',
                  'fuel_type',
                  'transmission')
