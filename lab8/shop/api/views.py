from django.shortcuts import render
from .models import Product
from .models import Category
  
def index(request):
	return render(request, 'api/index.html')

def products(request):
	products = Product.objects.all()
	return render(request, 'api/products.html', {'products': products})

def categories(request):
	categories = Category.objects.all()
	return render(request, 'api/categories.html', {'categories': categories})

def oneproduct(request, id):
    oneproduct = Product.objects.order_by('id')[id-1:id]
    return render(request, 'api/oneproduct.html', {'oneproduct':oneproduct})

def onecategory(request, id):
    onecategory = Category.objects.order_by('id')[id-1:id]
    return render(request, 'api/onecategory.html', {'onecategory':onecategory})