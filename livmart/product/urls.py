from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('search/', views.ProductListView.as_view(), name='search'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='detail'),
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete'),
]