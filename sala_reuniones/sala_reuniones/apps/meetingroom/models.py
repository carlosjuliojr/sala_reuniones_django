# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from sala_reuniones.apps.state.models import State
from sala_reuniones.apps.supply.models import Supply

# Create your models here.

class MeetingRoom(models.Model):

    name = models.CharField(
        max_length=100,
        blank = False,
    )

    address = models.CharField(
        max_length=150,
        blank=False,
    )

    capacity = models.ImageField()

    availability_schedule = models.DateTimeField()

    state = models.ForeignKey(
        State,
        related_name='state_meetingroom',
    )

    supplies = models.ManyToManyField(Supply)

    def __str__(self):
        return self.name

    # esto va en Supplie
    # supplies = models.ManyToManyField(
    #     Supplie,
    #     related_name='supplies_meetingroom',
    # )

