from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=256,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=4,
    )


class Purchase(models.Model):
    created = models.DateTimeField(
        auto_created=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )
    name = models.CharField(
        max_length=128
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )


class Favorites(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
