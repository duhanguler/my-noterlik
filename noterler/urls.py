from django.urls import path
from . import views

urlpatterns = [
    path('', views.noter_list, name='noter_list'),
]