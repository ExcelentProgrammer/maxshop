from django.contrib import admin
from django.contrib.admin import ModelAdmin

from Orders.models import Orders


class OrdersView(ModelAdmin):
    list_display = ['name', "phone", "product", "stream"]


admin.site.register(Orders, OrdersView)
