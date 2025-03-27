from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    line1 = '<h1 style = "text-align:center">主界面</h1>'
    line2 = '<a href = "play/">进入游戏界面</a>'
    line3 = '<img src = "http://gips3.baidu.com/it/u=764883555,2569275522&fm=3028&app=3028&f=JPEG&fmt=auto?w=960&h=1280"  width = 100%>'
    return HttpResponse(line1 + line2 + line3)


def play(request):
    line1 = '<h1>游戏界面</h1>'
    line2 = '<a href= "/">返回主界面</a>'
    line3 = '<img src = "http://gips2.baidu.com/it/u=2886475727,1716700323&fm=3028&app=3028&f=JPEG&fmt=auto?w=960&h=1280" width = 100%>'
    return HttpResponse(line1 + line2 + line3)
