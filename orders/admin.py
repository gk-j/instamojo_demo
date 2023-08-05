from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'product', 'is_paid', 'instamojo_response', 'created_at', 'updated_at')

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.select_related('user', 'product')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_image', 'product_price', 'created_at', 'updated_at')


    # def __str__(self):
    #     return self.product_name

admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)