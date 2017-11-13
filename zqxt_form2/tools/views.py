from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# 引入创建的表单类
from .forms import AddForm


def index(request):
    if request.method == 'POST': # 通过判断是否是 'POST' 方式，确定是否提交表单
        form = AddForm(request.POST) # form 包含提交的数据

        if form.is_valid():    # 由 Django 判断数据是否合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
   
    else:    # 如果不是提交而是正常访问
        form = AddForm()
    return render(request,'index.html',{'form':form})
