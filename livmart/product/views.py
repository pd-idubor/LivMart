from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Category, Product
from .forms import NewProductForm, EditProductForm



class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_list = Product.objects.filter(categories=self.get_object())
        context['product_list'] = product_list
        return context


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query', '')
        categories = Category.objects.all()
        category_id = self.request.GET.get('category', 0)
        context['categories'] = categories
        
        if query:
            context['query'] = query
            context['product_list'] = Product.objects.filter(name__icontains=query) | Product.objects.filter(description__icontains=query) 
        
        if category_id:
            context['product_list'] = Product.objects.filter(categories__id=category_id)
            
        return context
        
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.filter(categories__in=self.object.categories.all()).distinct().exclude(id=self.object.id)[:6]
        return context


    """def search_items(request):
        query = request.GET.get('query', '')
        category_id = request.GET.get('category', 0)
        categories = Category.objects.all()
        items = Item.objects.filter(available=True)

        if category_id:
            items = items.filter(category_id=category_id)

        if query:
            items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

        return render(request, 'search_items.html', {
            'items': items,
            'query': query,
            'categories': categories,
            'category_id': int(category_id)
        })"""

class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = NewProductForm
    template_name = 'product_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('product:detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = EditProductForm
    template_name = 'product_form.html'
    success_url = 'product:detail'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('product:detail', kwargs={'pk': self.object.pk})

    
    
class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('user:dashboard', args=[self.request.user])
