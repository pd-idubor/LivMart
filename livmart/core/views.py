from django.shortcuts import render, redirect
from django.views import View
from product.models import Category, Product
from .forms import RegistrationForm


def index(request):
    products = Product.objects.filter(is_available=True)[:8]
    categories = Category.objects.all()
    return render(request, 'index.html', context={
        'products': products,
        'categories': categories,
    })

class classIndex(View):
    def get(self, req):
        return render(req, 'main.html')
    
def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})
