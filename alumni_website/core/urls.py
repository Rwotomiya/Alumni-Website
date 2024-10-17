from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('directory/', views.alumni_directory, name='directory'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),  # Registration page
    path('news/', views.news_list, name='news'),
]
