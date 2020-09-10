from django.urls import path
from blogs import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('about/', views.about, name='blogs-about'),
]