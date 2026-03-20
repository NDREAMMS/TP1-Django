from django.shortcuts import get_object_or_404, render

from .models import Category

# Create your views here.




def product_list(request) :
   return render(request, 'product_list.html')

def product_detail(request, id) :
   return render(request, 'product_detail.html', {"id":id})

def category_list(request):
 categories = Category.objects.all()
 return render(request, "products/category_list.html", {'categories': categories})

def category_detail(request, id):
 category = get_object_or_404(Category, id=pk)
 products = category.products.all() # Utilisation de related_name-'products'
 return render(request, 'products/category_detail.html', {'category': category, 'products': products})