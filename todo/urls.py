from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
    path('',views.first, name='first'),
    path('choose', views.choose, name='choose'),
    path('delete/<str:pk>', views.delete, name='delete')
]