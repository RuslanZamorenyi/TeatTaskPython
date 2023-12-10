from django.contrib import admin

# Register your models here.
from .models import CostsModel


@admin.register(CostsModel)
class RestaurantAdmin(admin.ModelAdmin):
    pass