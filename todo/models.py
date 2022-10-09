from django.db import models

# Create your models here.

# class inheritance =
# our item class can do everything the Django built-in models can do


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Overriding the default Item display to use the item name
    def __str__(self):
        return self.name
