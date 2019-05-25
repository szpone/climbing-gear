from django.db import models

from users.models import Climber

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=128)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GearCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Gear(models.Model):
    gear_category = models.ForeignKey(GearCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    climber = models.ForeignKey(Climber, on_delete=models.CASCADE)

    def get_full_name(self):
        return f"{self.brand.name} {self.model.name} {self.gear_type.name}"


class Image(models.Model):
    image = models.ImageField()
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)


class Usage(models.Model):
    date_used = models.DateTimeField()
    location = models.CharField(max_length=256)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
