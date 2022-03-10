from ast import Param
from email.policy import default
from pickle import GET
from string import punctuation
from tkinter import OFF
import django
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    return HttpResponse('''"hello and welcome"<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">click here</a>''')

def mangala(request):
    djtext=request.GET.get('text',default)
    mangala=request.GET.get('mangala','off')
    punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    print(djtext)
    analayzed=''
    if mangala=='on':
        for char in djtext:
                if char not in punctuations:
                    analayzed = analayzed + char
        params= {'purpose':'removed puntuation','analysed_text':analayzed}
        
        return render(request,'analyse.html',params)
    else:
        return HttpResponse('Error')
