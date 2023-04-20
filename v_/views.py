from django.shortcuts import render, redirect,HttpResponse
import json

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

def autopull(request):
    if request.method=='GET':
        print('/n----------------------GET SOMETHING------------------------------/n')
        ans={"from":"get"}
        return HttpResponse(json.dumps(ans))
    else:

        # print(request.POST)
        # print(request.body)
        hookdata=request.body.decode('utf-8')
        data=json.loads(hookdata)
        print(data)
        print('/n----------------------收到webhook------------------------------/n')
        # print(request.POST.get('password'))
        ans={"from":"post"}
        return HttpResponse(json.dumps(ans))
    
    
