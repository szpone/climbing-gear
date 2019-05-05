from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128)


class ModelName(models.Model):
    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class GearType(models.Model):
    name = models.CharField(max_length=64)


class DateTimeLocation(models.Model):
    date_used = models.DateTimeField()
    location = models.CharField(max_length=256)


class Image(models.Model):
    image = models.ImageField()


class Gear(models.Model):
    gear_type = models.ForeignKey(GearType, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model_name = models.ForeignKey(ModelName, on_delete=models.CASCADE)
    used = models.ManyToManyField(DateTimeLocation)
    image = models.ManyToManyField(Image, blank=True)

