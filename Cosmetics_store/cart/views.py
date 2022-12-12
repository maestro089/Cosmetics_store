from django.shortcuts import render, redirect
from django.contrib import messages

from .models import the_cart,Order,ProductInOrder
from store.models import *


def view_cart(request):

    price = 0
    
    cart = the_cart.objects.filter(customer = request.user)
    

    for cart in cart:
        price_all = cosmetics.objects.get(title = cart.title)
        price = price + price_all.price * cart.quentity


    context = {
        'cart': the_cart.objects.filter(customer = request.user),
        'price':price,
        }
    return render(request,'cart/cart_view.html',context = context)



def add_cart(request):
    path = request.GET.get('next')
    
    if request.method == 'POST':
        if request.POST.get('quentity'):
                the_cart.objects.create(title = cosmetics.objects.get(id = request.GET.get('ad_id')),
                                        customer = request.user, 
                                        quentity = request.POST.get('quentity')
                                        )
    return redirect(path)

def delete_cart(request):
    path = request.GET.get('next')
    
    if request.method == 'POST':
        id = request.GET.get('cart_id')
        find = the_cart.objects.get(id = id)
        find.delete()
    return redirect(path)


def place_order(request):

    cart = the_cart.objects.filter(customer = request.user)
    if(len(cart)>0):
        order = Order.objects.create(customer=request.user)

        for cart in cart:
            product = cosmetics.objects.get(pk=cart.title.pk)
            quantity = cart.quentity
            ProductInOrder.objects.create(order=order, product=cart.title, quantity=quantity)
            cart.delete()
        messages.success(request, 'Заказ оформлен')
        return render(request,'cart/cart_view.html') 
    return render(request,'cart/cart_view.html')

def order(request):
    orders =  Order.objects.filter(customer = request.user)
    
    context = {
        'orders':Order.objects.filter(customer = request.user),
        'product':ProductInOrder.objects.all(),
        }
    return render(request,'Order.html',context = context)

