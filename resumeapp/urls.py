# resumeapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # We'll create this `home` view next
]
