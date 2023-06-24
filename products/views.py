from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from Orders.models import Orders
from products.models import Products
from .forms import ProductOrderForm
import requests


class HomePage(View):

    def get(self, request, pk):
        form = ProductOrderForm()
        product = get_object_or_404(Products, id=pk)

        context = {
            "product": product,
            "form": form,
        }

        return render(request, "product.html", context=context)

    def post(self, request: HttpRequest, pk):
        data = request.POST
        form = ProductOrderForm(data=data)

        product = get_object_or_404(Products, id=pk)

        context = {
            "product": product,
            "form": form,
        }

        if not form.is_valid():
            messages.error(request, form.errors)
            return render(request, "product.html", context)
        name = form.data.get("name")
        phone = str(form.data.get("phone")).replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
        if len(phone) != 13:
            messages.error(request, "Telefon nomer nato'g'ri kiritildi")
            return render(request, "product.html", context)

        url = product.site

        payload = {
            "stream": product.stream,
            "phone": phone,
            "name": name,
        }
        headers = {"Content-Type": "application/json",
                   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                   }
        try:
            response = requests.post(url, json=payload, headers=headers).json()
            Orders.objects.create(name=name, phone=phone, product=product.name, stream=product.stream)
            if response['status'] == 200:
                return redirect(reverse("success"))
        except Exception as e:
            print(e)

        messages.error(request, "Serverda xatolik yuzaga keldi!!!")
        return render(request, "product.html", context)


class SuccessView(View):

    def get(self, request):
        return render(request, "success.html")
