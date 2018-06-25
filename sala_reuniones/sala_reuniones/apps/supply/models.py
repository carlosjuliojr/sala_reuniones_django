# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Supply(models.Model):

    nameSupply = models.CharField( 
        max_length=50,
         blank=False,
        )

    def __str__(self):
        return self.nameSupply


