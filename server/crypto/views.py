from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def get_ethereum_price(request):
    response = requests.get("https://www.mercadobitcoin.net/api/ETH/ticker")
    price = float(json.loads(response.content)["ticker"]["last"])
    formatted_price = f"{price:.2f}"
    return HttpResponse(formatted_price)
