from django.contrib import admin
from .models import Order,Cart,Product

# Register your models here.
admin.site.register(Order);
admin.site.register(Cart);
admin.site.register(Product);
