from django.db import models
from django.core.validators import MinValueValidator

from tags.models import Taggable


class Car(Taggable):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(validators=[MinValueValidator(2010)])

    def __str__(self):
        return '{0} {1} {2}'.format(self.brand, self.model, self.year)