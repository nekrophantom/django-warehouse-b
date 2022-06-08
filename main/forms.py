from socket import fromshare
from django import forms
from .models import categoryWarehouse

class categoryWarehouseForm(forms.ModelForm):

    class Meta:
        model = categoryWarehouse
        fields = '__all__'
