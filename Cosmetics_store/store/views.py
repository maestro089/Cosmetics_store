from django.shortcuts import render, redirect
from .models import *
from news.models import *

def index(request):
    context = {
        'cosmetic':cosmetics.objects.all().order_by("-id")[0:4],
        'news':news.objects.all().order_by("-id")[0:4],
        }
    return render(request,'store/index.html',context = context)

def product(request,pk):

    if request.method == "POST":

            comment_cosmetics.objects.create(author = request.user,text = request.POST.get('Text'),cosmetics=cosmetics.objects.get(pk = pk))
            return redirect(request.path)
    context = {
        "cosmetic":cosmetics.objects.filter(pk = pk),
        "comment":comment_cosmetics.objects.filter(cosmetics = cosmetics.objects.get(pk = pk)),
        }
    return render(request,'store/product.html',context = context)

def store(request):

    context = {
        'cosmetic':cosmetics.objects.all(),
        }
    return render(request,'store/store.html',context = context)


##