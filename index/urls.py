from django.contrib import admin
from django.urls import path
from .views import index, contact, order

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("order/", order, name="order"),
]
