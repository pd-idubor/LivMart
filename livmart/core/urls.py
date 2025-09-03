from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import LoginForm


urlpatterns = [
        path('', views.index, name='index'),
        path('main', views.classIndex.as_view(), name='main'),
        path('signup', views.register, name='signup'),
        path('login', LoginView.as_view(authentication_form=LoginForm, template_name='login.html'), name='login')
        ]
