from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from product.models import Product


class UserDashboard(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'dashboard.html'
    context_object_name = 'my_products'

    def get_queryset(self):
        return (
            Product.objects.filter(created_by=self.request.user)
                .order_by('-created_at')
                )