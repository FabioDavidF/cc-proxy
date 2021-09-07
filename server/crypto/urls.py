
from django.urls import path
from . import views

urlpatterns = [
    path("eth", views.get_ethereum_price)
]
