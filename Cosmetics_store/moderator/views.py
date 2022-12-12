from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.views.generic import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


from store.models import *
from .forms import EditForm, EditNewsForm
from news.models import news
from cart.models import Order,ProductInOrder


def moderator_main(request):

    comments = comment_cosmetics.objects.all()
    user = User.objects.all()

    context = {
        'comments':comments,
        'user':user,
        }

    return render(request,"moderator/moderator_main.html",context = context)

def moderator_cosmetics(request):

    cosmetic = cosmetics.objects.all()


    context = {
        'cosmetic':cosmetic,
        }

    return render(request,"moderator/moderator_cosmetics.html",context = context)

def delete_user(request):
    path = request.GET.get('next')

    user_search = User.objects.get(id = request.GET.get('user_id'))
    user_search.delete()


    return redirect(path)

def add_menejer(request,pk):
    profile_user = User.objects.get(id = pk)
    profile_user.is_staff = True
    profile_user.save()

    return redirect('moderator:moderator_main')

def delete_menejer(request,pk):

    profile_user = User.objects.get(id = pk)
    profile_user.is_staff = False
    profile_user.save()

    return redirect('moderator:moderator_main')

class edit_cosmetics(UpdateView):
    model = cosmetics
    template_name = 'moderator/edit_cosmetics_cart.html'

    form_class = EditForm

class create_cosmetics(CreateView ):
    model = cosmetics
    template_name = 'moderator/edit_cosmetics_cart.html'

    form_class = EditForm
def delete_cosmetics(request,pk):

    b = cosmetics.objects.filter(pk = pk)
    path = request.path
    b.delete()

    return redirect('moderator:moderator_cosmetics')

def moderator_news(request):

    search_news = news.objects.all()

    context ={
        "news":search_news,

        }

    return render(request,"moderator/moderator_news.html",context = context)

class edit_news(UpdateView):
    model = news
    template_name = 'moderator/edit_news_cart.html'

    form_class = EditNewsForm

class create_news(CreateView ):
    model = news
    template_name = 'moderator/edit_news_cart.html'

    form_class = EditNewsForm

def delete_news(request,pk):

    b = news.objects.filter(pk = pk)
    path = request.path
    b.delete()

    return redirect('moderator:moderator_news')

def manager_main(request):
    orders =  reversed(Order.objects.all())
    product = ProductInOrder.objects.all()

    context = {
        'orders':orders,
        'product':product,
        }
    return render(request,'manager/index.html',context = context)




    


