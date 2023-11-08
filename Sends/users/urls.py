from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.Home, name='Home'),
    path('login/', LoginView.as_view(), name='login'),
]
