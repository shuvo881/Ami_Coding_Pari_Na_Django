from django.urls import path
from . import views

urlpatterns = [
    # ... other URLs
    path('search/', views.search_page, name='search_page'),
]
