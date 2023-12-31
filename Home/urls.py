from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('add/', views.blog_add, name = 'add'),
    path('myblogs', views.Myblogs, name = 'myblogs'),
    path('profile/', views.profile, name = 'profile')
]