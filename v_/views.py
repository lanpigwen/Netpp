from django.shortcuts import render, redirect,HttpResponse
import json
import os

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

def feature(request):
    return render(request, 'feature.html',locals())

def market(request):
    return render(request, 'market.html',locals())

def overview(request):
    return render(request, 'overview.html',locals())