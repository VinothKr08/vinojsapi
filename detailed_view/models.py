from django.db import models
from django.contrib.postgres.fields import ArrayField


class DetailedView(models.Model):

    title = models.CharField(max_length=120)
    order_no = models.IntegerField()
    subtitle = models.CharField(max_length=120)
    description = ArrayField(models.CharField(max_length=200, blank=True))
    example = models.TextField(blank=True)
    output = models.TextField(blank=True)

    def __str__(self):
        return self.subtitle

