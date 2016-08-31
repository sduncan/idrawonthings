from django.db import models


class Case(models.Model):
    title = models.CharField(max_length=100)