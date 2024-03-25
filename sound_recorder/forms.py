from django import forms
from .models import Recording
from django.shortcuts import get_object_or_404, redirect

class RecordingForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ['name', 'audio_file']

class RecordingDeleteForm(forms.Form):
    recording_id = forms.IntegerField(widget=forms.HiddenInput())

def delete_recording(request, recording_id):
    recording = get_object_or_404(Recording, id=recording_id)
    if request.method == 'POST':
        recording.delete()
        return redirect('recordings_list')  # Redirect to the recordings list page
    return redirect('recordings_list')

class RecordingRenameForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ['name']