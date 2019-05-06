from django.contrib import admin

from .models import Company, Usage, Gear, GearType, Image, ModelName

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(GearType)
class GearTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ("gear_type", "company", "model_name")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image",)


@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ("date_used", "location")


@admin.register(ModelName)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ("name", "company")
