# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo




