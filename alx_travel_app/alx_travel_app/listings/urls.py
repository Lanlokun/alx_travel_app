from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings_api, name='listings_api'),
]