from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class ModelName(models.Model):
    name = models.CharField(max_length=128)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GearType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Gear(models.Model):
    gear_type = models.ForeignKey(GearType, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    model_name = models.ForeignKey(ModelName, on_delete=models.CASCADE)

    def __str__(self):
        return self.gear_type.name


class Image(models.Model):
    image = models.ImageField()
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)


class Usage(models.Model):
    date_used = models.DateTimeField()
    location = models.CharField(max_length=256)
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
