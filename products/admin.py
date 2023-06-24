from django.conf import settings
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.template.defaultfilters import safe
from django.urls import reverse

from products.models import Products


class ProductView(ModelAdmin):
    list_display = ['name', "product", "stream", "price", "site", "description"]

    def product(self, obj):
        domain = settings.SITE_URL
        url = safe("<a href='{domain}{url}' >{domain}{url}</a>".format(domain=domain,
                                                                       url=reverse('product', kwargs={'pk': obj.id})))
        return url

    product.allow_tags = True
    product.short_description = "Maxsulot"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


admin.site.register(Products, ProductView)
