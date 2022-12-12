from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('product/<int:pk>', views.product, name='product'),
    path('store/', views.store, name='store'),
]
