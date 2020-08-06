from django.contrib import admin
from .models import Product, Category, Console, Manufacturer

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Console)
admin.site.register(Manufacturer)
