from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=63, blank=False)
    model = models.CharField(max_length=127, blank=False)

    class FuelTypeChoices(models.TextChoices):
        PETROL = 'бензин'
        DIESEL = 'дизель'
        ELECTRIC = 'электричество'
        HYBRID = 'гибрид'

    fuel_type = models.CharField(max_length=31,
                                 choices=FuelTypeChoices,
                                 blank=False)

    class TransmissionChoices(models.TextChoices):
        MANUAL = 'механическая'
        AUTO = 'автоматическая'
        CVT = 'вариатор'
        SEMI_AUTO = 'робот'

    transmission = models.CharField(max_length=31,
                                    choices=TransmissionChoices,
                                    blank=False)

    year = models.PositiveIntegerField(blank=False)
    mileage = models.PositiveIntegerField(blank=False)
    price = models.PositiveIntegerField(blank=False)

    class Meta:
        ordering = ('-id',)
        unique_together = ('brand', 'model')