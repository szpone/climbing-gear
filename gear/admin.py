from django.contrib import admin

from .models import Brand, Gear, GearCategory, Image, Model, Usage

# Register your models here.


@admin.register(Brand)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(GearCategory)
class GearTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ("gear_type", "brand", "model")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ("date_used", "location")


@admin.register(Model)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")
