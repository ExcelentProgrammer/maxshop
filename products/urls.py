from django.urls import path

from products.views import HomePage, SuccessView

urlpatterns = [
    path("product/<int:pk>/", HomePage.as_view(), name="product"),
    path("success/", SuccessView.as_view(), name="success")
]
