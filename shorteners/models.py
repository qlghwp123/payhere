from django.db import models


class Link(models.Model):
    origin = models.URLField(max_length=200)
    new = models.URLField(default="")
    expire = models.DateTimeField()