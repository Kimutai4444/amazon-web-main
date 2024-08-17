from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'base/index.html') 

def products(request):
    return render(request, 'base/products.html')

def services(request):
    return render(request,'base/services.html')
def ourstory(request):
    return render(request,'base/ourstory.html')
def contact(request):
    return render(request,'base/contact.html')