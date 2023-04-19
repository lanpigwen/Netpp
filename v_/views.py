from django.shortcuts import render, redirect

#以下两行的作用是让结果唯一：
from langdetect import DetectorFactory
DetectorFactory.seed = 0

def bg(request):
    return render(request, 'bg.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def more(request):
    return render(request, 'more.html', locals())

def vrHouse(request):
    return render(request, 'room.html',locals())