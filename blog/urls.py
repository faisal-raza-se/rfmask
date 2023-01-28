from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('my_blog/', views.my_blog, name='my_blog'),
    path('create_blog/', views.create_blog, name='create_blog'),
]
