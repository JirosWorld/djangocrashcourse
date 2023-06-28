from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name='details'),
]

#   If you notice path() instead of url(), know that this is a change in Django 2.0.  Do not include the r'^$' but make it just path() function with single quotes for the index view.