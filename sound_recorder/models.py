from django.db import models
from django.utils import timezone

def recording_file_path(instance, filename):
    # Extract the file extension from the original file name
    ext = filename.split('.')[-1]

    # Generate a unique file name using the current date and time
    filename = f"{timezone.now():%Y-%m-%d-%H-%M-%S}-{instance.name}.{ext}"

    # Return the path under which the file will be saved
    return f'recordings/{filename}'

class Recording(models.Model):
    name = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to=recording_file_path)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
