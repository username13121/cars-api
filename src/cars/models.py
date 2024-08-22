from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=63, blank=False)
    model = models.CharField(max_length=127, blank=False)

    class FuelType(models.TextChoices):
        PETROL = 'бензин'
        DIESEL = 'дизель'
        ELECTRIC = 'электричество'
        HYBRID = 'гибрид'

    fuel_type = models.CharField(max_length=31,
                                 choices=FuelType,
                                 blank=False)

    class TransmissionType(models.TextChoices):
        MANUAL = 'механическая'
        AUTO = 'автоматическая'
        CVT = 'вариатор'
        SEMI_AUTO = 'робот'

    transmission_type = models.CharField(max_length=31,
                                         choices=TransmissionType,
                                         blank=False)

    year = models.IntegerField(blank=False)
    mileage = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)

    class Meta:
        ordering = ('-id',)