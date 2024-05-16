# urls.py
from django.urls import path
from .views import index , null_view , index2 , home

urlpatterns = [
    path('',home,name="home"),
    path('property/',index, name='property'),
    path('property_list/',index2, name='property_list'),
    path('null/',null_view,name="null"),
]
