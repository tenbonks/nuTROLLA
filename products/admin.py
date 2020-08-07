from django.contrib import admin
from .models import Product, Category, Console, Manufacturer

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'console',
        'price',
        'image',
        'stock',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'manufacturer',
        'friendly_name',
        'name',
    )


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Console, ConsoleAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
