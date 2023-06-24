from django import forms


class ProductOrderForm(forms.Form):
    name = forms.CharField(max_length=255, label="Ismingiz")
    phone = forms.CharField(max_length=255, label="Telefon nomeringiz")
