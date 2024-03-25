from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse  # Add JsonResponse here
from .forms import RecordingForm
from .models import Recording
from django.views.decorators.csrf import csrf_exempt  # Only for testing purposes; handle CSRF properly in production


def record(request):
    if request.method == 'POST':
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recordings_list')
    else:
        form = RecordingForm()
    return render(request, 'sound_recorder/record.html', {'form': form})

def recordings_list(request):
    recordings = Recording.objects.all()
    return render(request, 'recorder/recordings_list.html', {'recordings': recordings})

def delete_recording(request, pk):
    if request.method == 'POST':
        recording = Recording.objects.get(pk=pk)
        os.remove(os.path.join(settings.MEDIA_ROOT, str(recording.audio_file)))
        recording.delete()
    return redirect('recordings_list')

def upload_recording(request):
    if request.method == 'POST':
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            recording = form.save()
            # Return a JSON response indicating success
            return JsonResponse({'message': 'Recording uploaded successfully', 'id': recording.id})
        else:
            # Return a JSON response indicating the form was invalid
            return JsonResponse({'error': 'Failed to upload recording due to form validation'}, status=400)
    else:
        # Only POST method is allowed for uploading
        return HttpResponse('Method not allowed', status=405)