from django.shortcuts import render
from django.http import HttpResponse
from .models import menu
from django.core import serializers
# Create your views here.


def index(request):
    pizzas = menu.objects.all().order_by('prix')
    return render(request, 'pizza/index.html',{'pizzas': pizzas})


def main(request):
    return render(request, 'pizza/main.html')

def api(request):
    pizzas = menu.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)