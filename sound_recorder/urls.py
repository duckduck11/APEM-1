from django.urls import path
from . import views
from .views import upload_recording

urlpatterns = [
    path('', views.record, name='record'),
    path('recordings/', views.recordings_list, name='recordings_list'),
    path('recordings/delete/<int:pk>/', views.delete_recording, name='delete_recording'),
    path('upload/', upload_recording, name='upload_recording'),
]
