from django.contrib import admin
from cart.models import the_cart,Order, ProductInOrder


admin.site.register(the_cart)


class ProductsInOrderInline(admin.TabularInline):
    model = ProductInOrder

    verbose_name = 'Order'
    verbose_name_plural = 'Orders'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('created',)
    list_display = ('customer', 'quantity', 'created', )

    inlines = (ProductsInOrderInline,)

    def quantity(self, obj):
        return ProductInOrder.objects.filter(order=obj).count()

    quantity.short_description = 'Quantity order'
