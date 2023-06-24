from django.db import models


class Products(models.Model):
    SITES = [
        ("https://mahsulot.com/order_api/", "mahsulot.com"),
        ("https://airshop.uz/order_api/", "airshop.uz"),
    ]

    photo = models.ImageField(upload_to="products/", default="products/default.jpg")
    name = models.CharField(max_length=255)
    stream = models.URLField()
    site = models.CharField(choices=SITES, max_length=255)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
