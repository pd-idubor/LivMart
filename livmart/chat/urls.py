from django.urls import path
from . import views


app_name = 'chat'

urlpatterns = [
    path('new/<int:product_pk>/', views.new_chat, name='new'),
    path('inbox', views.inbox, name='inbox'),
    path('<int:pk>/', views.message_detail, name='detail')

]