from django.shortcuts import render
from .models import VideoFiles
from .forms import VideoForm
import moviepy
from moviepy.editor import *
import speech_recognition as sr
from convert import tasks
from convert import models
from django.http import HttpResponseRedirect
from act .models import Activity
from django.contrib import messages
from account.models import Account, Student



def showvideo(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            get_classrooms = request.user.classroom
            stud  = models.Account.objects.filter(classroom = get_classrooms)
            samples = models.VideoFiles.objects.filter(clss = get_classrooms)
        


    context= {
               'samples': samples,
               'stud': stud
            }
    
    return render(request, '../templates/videos.html', context)

def savevideo(request):
    activity = Activity.objects.all()
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        
        get_a_number = form.cleaned_data['activity_number']

        
        if request.user.is_authenticated: 
            get_classroom = request.user.classroom
            instance = form.save(commit=False)
            messages.success(request, 'Your video was uploaded successfully!')
            instance.student = request.user
            instance.act = Activity.objects.get(clss =get_classroom,a_number =get_a_number)
            instance.clss = request.user.classroom
            instance.save()

            lastvideo= models.VideoFiles.objects.last()
                

            video= lastvideo.video
            print(video.name)

            video = video.path
            audio = video
            print(video)

            clip = moviepy.editor.VideoFileClip(audio)

            clip.audio.write_audiofile("media/convert.wav")
        
            audio = "convert.wav"

            audioData = models.VideoFiles.objects.all().update(audio=audio)
            
            tasks.process_uploadedFile(audioData)        
    
            
         
    context= {
            'form': form,
            'activity':activity
    }
    
    return render(request, '../templates/s_class.html', context)


    

