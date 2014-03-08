from django import forms
from django.forms import ModelForm
from apps.logi.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item


