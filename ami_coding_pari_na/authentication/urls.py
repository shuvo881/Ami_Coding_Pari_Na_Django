from django.urls import path
from . import views

urlpatterns = [
    # make a root url of login view
    path('', views.login_view, name='login'),
    # make registration views link
    path('register/', views.register_view, name='registration_view'),

]
