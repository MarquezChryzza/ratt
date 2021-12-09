from __future__ import absolute_import, unicode_literals
from uuid import uuid4
import speech_recognition
from convert import models
from django.shortcuts import render
import moviepy
from moviepy.editor import *
from act.models import Activity



def process_uploadedFile(audioData):

    audioData = None
    audioData = models.VideoFiles.objects.last()

    transcribe_audio(audioData)
    word_count(audioData)
    
def transcribe_audio(audioData):

    audio = audioData.audio
    audio_file = transcript = None

    recognizer = speech_recognition.Recognizer()

    with speech_recognition.AudioFile(audio) as ef:
        recognizer.adjust_for_ambient_noise(ef)
        audio_file = recognizer.record(ef)
        transcript = recognizer.recognize_google(audio_file)
        
    audioData.transcript = transcript
    audioData.save()

    return

def word_count(audioData):
    # wow = VideoFiles.objects.values('act')
    # print(wow)
    transcript = audioData.transcript
    material = list(Activity.objects.all().values_list('a_material', flat=True))
    print(material)
    for i in material:
        print(i)
    counts1 = dict()
    mtrDefault = i.split()

    for word in mtrDefault:
        if word in counts1:
            counts1[word] += 1
        else:
            counts1[word] = 1

    counts = dict()
    strDefault = transcript.split()

    for word in strDefault:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print(counts1)
    print(counts)
    #print(counts1)
    expected = len(mtrDefault)
    actual = len(strDefault)
    accuracy = (actual/expected) * 100
    print(accuracy, "%")
    audioData.accuracy = accuracy
    audioData.save()
    audioData.expected = expected
    audioData.save()
    audioData.actual = actual
    audioData.save()

    return counts1
    return counts