from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('<str:pk>/dashboard', views.UserDashboard.as_view(), name='dashboard')
]