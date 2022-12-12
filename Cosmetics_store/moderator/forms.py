from store.models import *
from django.forms import ModelForm
from django import forms
from news.models import news


class EditForm(forms.Form,ModelForm):

    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название'}))
    price = forms.IntegerField(label="Цена", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Цена'}))
    description = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))


    class Meta:
        model = cosmetics
        fields = ['photo','title',  'description', 'price','type','Manufacturer']

class EditNewsForm(forms.Form,ModelForm):

    title = forms.CharField(label="Название", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Название'}))
    text = forms.CharField(label="Описание", widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))


    class Meta:
        model = news
        fields = ['photo','title', 'text']



        
