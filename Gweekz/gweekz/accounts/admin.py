from django.contrib import admin
from .models import Customer, Order, OrderItem, Product, Tag, Game

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Game)

