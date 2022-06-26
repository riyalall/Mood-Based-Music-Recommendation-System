from django.shortcuts import render, HttpResponse
from transformers import pipeline
emotion = pipeline('sentiment-analysis',model='arpanghoshal/EmoRoBERTa')
import random
import speech_recognition as sr
from playsound import playsound
import pygame
from pygame import mixer
from tkinter import *
import os

# global mood

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def mymood(request):
    return render(request, 'mymood.html')

def mainpage(request):
    data = request.POST.get('name')
    print(data)
    l=["How have you been feeling this week?","What happened over your weekend","Is there anything bothering you",
    "How do you feel about yourself?","Describe yourself in a sentence"]
    context={'variable':random.choice(l)}
    # print(type(context_dict)) 
    return render(request, 'mainpage.html',context)

def mycode(request):
    data = request.POST.get('name')
    emotion_labels = emotion(data)
    print(emotion_labels[0]['label'])
    print(data)
    # global mood
    # print('hey' +mood)
    mood = emotion_labels[0]['label']
    context={'variable':mood}
    # print(context)
    # print("joker")
    if context=="":
         print("start")
    #      playsound('D:\\song Recommender\\MoodRecognizer\static\\neutral\\Kuch Baatein Payal Dev 128 Kbps.mp3')
    #      print("stop")
    return render(request,'mymood.html',context)

def mycode1(request):
    data = request.POST.get('name')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("hi Speaking")
        audio=r.listen(source)

        try:
            text=r.recogize_google(audio)
            emotion_labels = emotion(text)
            print(emotion_labels[0]['label'])
            context={'variable':text}
    
        except:
            print("sry speak again")
    print("Hi preeti")
    return HttpResponse("helo")
    # return render(request,'mymood.html',context)
    

def music(request):
    def playsong():
        currentsong=playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        songstatus.set("Playing")
        mixer.music.play()

    def pausesong():
        songstatus.set("Paused")
        mixer.music.pause()

    def stopsong():
        songstatus.set("Stopped")
        mixer.music.stop()

    def resumesong():
        songstatus.set("Resuming")
        mixer.music.unpause()    

    root=Tk()
    root.title('Music player project')

    mixer.init()
    songstatus=StringVar()
    songstatus.set("choosing")

#playlist---------------

    playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
    playlist.grid(columnspan=5)

    # global mood

    # print('Riya: '+mood)

    # if mood in os.listdir('D:\Projects\Major\Mood-Recognizer-master\MoodRecognizer\static'):
    #     os.chdir(r'"D:\Projects\Major\Mood-Recognizer-master\MoodRecognizer\static\" + mood')
    # else:
    #     os.chdir(r'D:\Projects\Major\Mood-Recognizer-master\MoodRecognizer\static\joy')
    os.chdir(r'D:\Projects\Major\Mood-Recognizer-master\MoodRecognizer\static\joy')
    songs=os.listdir()
    for s in songs:
        playlist.insert(END,s)

    playbtn=Button(root,text="play",command=playsong)
    playbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    playbtn.grid(row=1,column=0)

    pausebtn=Button(root,text="Pause",command=pausesong)
    pausebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    pausebtn.grid(row=1,column=1)

    stopbtn=Button(root,text="Stop",command=stopsong)
    stopbtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    stopbtn.grid(row=1,column=2)

    Resumebtn=Button(root,text="Resume",command=resumesong)
    Resumebtn.config(font=('arial',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
    Resumebtn.grid(row=1,column=3)

    mainloop()

    return render(request, 'music.html')



