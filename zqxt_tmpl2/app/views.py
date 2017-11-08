from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    string = "不使用 u'something' 字符串难道就不能正常显示？"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'object':'Django', 'info':'这是自强学堂的 Django 项目练习题'}
    List = map(str, range(100))

    return render(request, 'home.html',
                  {'string': string,
                   'TutorialList':TutorialList, 'info_dict':info_dict,
                   'List':List})

def add(request, a=1, b=1):
    c = int(a) + int(b)
    return HttpResponse(str(c))