from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    remaining_days = models.PositiveSmallIntegerField(default=0)
