from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse  # Add JsonResponse here
from .forms import RecordingForm
from .models import Recording
from django.views.decorators.csrf import csrf_exempt  # Only for testing purposes; handle CSRF properly in production
from django.views.decorators.http import require_POST
from .forms import RecordingRenameForm


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
    return render(request, 'sound_recorder/recordings_list.html', {'recordings': recordings})

def delete_recording(request, recording_id):
    recording = get_object_or_404(Recording, id=recording_id)
    recording.delete()
    return redirect('recordings_list')  # Replace 'recordings_list' with the name of your URL pattern for the recording list

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
    
def rename_recording(request, recording_id):
    recording = get_object_or_404(Recording, id=recording_id)
    if request.method == 'POST':
        form = RecordingRenameForm(request.POST, instance=recording)
        if form.is_valid():
            form.save()
            return redirect('recordings_list')  # Adjust as necessary to redirect to your recordings list page
    else:
        form = RecordingRenameForm(instance=recording)
    return render(request, 'rename_recording.html', {'form': form, 'recording_id': recording_id})

def edit_recording_view(request, recording_id):
    recording = get_object_or_404(Recording, id=recording_id)
    # Make sure you use the correct app name in the template path
    return render(request, 'sound_recorder/edit_recording.html', {'recording': recording})