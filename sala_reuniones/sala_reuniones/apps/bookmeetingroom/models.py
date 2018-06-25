# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from sala_reuniones.apps.supply.models import Supply
from sala_reuniones.apps.meetingroom.models import MeetingRoom

# Create your models here.

class BookMeetingRoom(models.Model):

    date = models.DateField(auto_now=True,)

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    amount_of_people = models.IntegerField(blank=True,)

    supplies = models.ManyToManyField(Supply)

    meetingroom = models.ForeignKey(
        MeetingRoom,
        related_name='meetingroom_bookmr',
    )


