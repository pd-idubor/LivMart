from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.contrib.auth.models import User


class Category(models.Model):
    """Defines the product category model"""
    title = models.CharField(max_length=50, unique=True, help_text='Enter product category name')

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'categories'
        constraints = [
            UniqueConstraint(
                Lower('title'),
                name='category_title_case_insensitive_unique',
                violation_error_message = "Category already exists (Match is case insensitive)"
                ),]

    def __str__(self):
        """Returns string representation of product title"""
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Product(models.Model):
    """"Product details model"""
    name = models.CharField(max_length=100, help_text="Enter product name")
    description = models.TextField(max_length=1000, help_text="Add a description of the product", null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    price = models.FloatField()
    stock_quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='products', null=True)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

