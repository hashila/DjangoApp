from django.http import HttpResponse
from django.shortcuts import render
from products.models import product

def about(request):
    return render(request,'about.html')

def homePage(request):
    products = product.objects.all().order_by('title')
    prd = products[0]
    products = products[1:]
    return render(request,'homepage.html',{"products":products,"fst":prd})
