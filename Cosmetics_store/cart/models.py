from django.db import models
from store.models import *
from django.contrib.auth.models import User


class the_cart(models.Model):
    object = None
    title = models.ForeignKey(cosmetics, on_delete=models.CASCADE, verbose_name='title')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='customer')
    quentity = models.FloatField(verbose_name = "Quantity", null = True)


class Order(models.Model):
    customer = models.ForeignKey(User, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Customer')
    porduct = models.ManyToManyField(cosmetics, verbose_name='Product', blank=True, through='ProductInOrder')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


    
class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order')
    product = models.ForeignKey(cosmetics, on_delete=models.PROTECT, verbose_name='Book', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity')

