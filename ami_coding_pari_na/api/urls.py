from django.urls import path

from . import views

urlpatterns = [
    # create url link for get_all_input_values views
    path('get_all_input_values/', views.get_all_input_values, name='get_all_input_values'),

]