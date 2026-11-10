from django.contrib import admin

from .models import Box, Order, OrderItem, Product


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ("reference", "created_at")


admin.site.register(Product)
admin.site.register(Box)
