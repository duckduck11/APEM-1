from django.urls import path
from . import views
from .views import upload_recording
from .views import delete_recording
from .views import rename_recording
from .views import edit_recording_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.record, name='record'),
    path('recordings/', views.recordings_list, name='recordings_list'),
    path('recordings/delete/<int:pk>/', views.delete_recording, name='delete_recording'),
    path('upload/', upload_recording, name='upload_recording'),
    path('delete/<int:recording_id>/', delete_recording, name='delete_recording'),
    path('rename/<int:recording_id>/', rename_recording, name='rename_recording'),
    path('edit/<int:recording_id>/', edit_recording_view, name='edit_recording'),
    path('record-camera/', views.record_camera, name='record_camera'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
