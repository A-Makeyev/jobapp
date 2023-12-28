from django.contrib import admin
from django.urls import path
from app import views # from app.views import job, job_list

urlpatterns = [
    path('', views.job_list, name='jobs_home'),
    path('job/<int:id>', views.job, name='job_details'),
    path('hello/', views.hello, name='hello')
]
