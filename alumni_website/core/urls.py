from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('directory/', views.alumni_directory, name='directory'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),  # Registration page
    path('news/', views.news_list, name='news'),
    path('jobs/', views.job_postings, name='job_postings'),
    path('jobs/<int:pk>/', views.job_details, name='job_details'),
    path('jobs/post/', views.post_job, name='post_job'),
    path('mentorship/', views.mentorship_requests, name='mentorship_requests'),    
    path('mentorship/request/', views.request_mentorship, name='request_mentorship'),
    
]
