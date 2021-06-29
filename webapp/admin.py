from django.contrib import admin

from .models import Order, Customer, Item, ItemCategory, OrderItem

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(ItemCategory)