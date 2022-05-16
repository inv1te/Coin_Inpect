from django.shortcuts import render, HttpResponse
from .models import *
from rest_framework import routers, serializers, viewsets

def CoinList(request):
    List_of_cryptos = ['BTC', 'ETH', 'BNB', 'USDC', 'XRP', 'SOL', 'BUSD', 'UST', ]
    BTC = Crypto_Curr.objects.get(symbol = "BTCUSD")
    context = {
        "list_cryptos": List_of_cryptos,
        "Currencies": {
            "BTC": BTC
        }
    }
    return render(request, 'profile.html', context= context)

def rest_api_update_data(request):
    if request.method == 'POST':
        print(request.POST.get('symbol'))
        return HttpResponse(request.POST.get('symbol'))
    else:
        return HttpResponse('Error! Send POST-method request!')