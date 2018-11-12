from django import forms

from .models import Client, Hairdo, AdditionalService, Bill


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class HairdoForm(forms.ModelForm):
    class Meta:
        model = Hairdo
        fields = '__all__'


class AdditionalSetviceForm(forms.ModelForm):
    class Meta:
        model = AdditionalService
        fields = '__all__'

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
