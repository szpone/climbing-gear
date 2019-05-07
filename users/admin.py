from django.contrib import admin
from django.contrib.auth import get_user_model

Climber = get_user_model()

# Register your models here.


@admin.register(Climber)
class ClimberAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")
