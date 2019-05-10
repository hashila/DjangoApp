from django.shortcuts import render
from .models import product
from django.http import HttpResponse

def details(request):
    products = product.objects.all().order_by('title')
    return render(request,'products/details.html',{"products":products})

def fulldetails(request,slug):
    # return HttpResponse(slug[:-1])
    pro = product.objects.get(slug=slug)
    return render(request,'products/fulldetails.html',{"pro":pro})
