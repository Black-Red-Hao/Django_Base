from django.shortcuts import render

# Create your views here.
#导入HttpResponse模块
from django.http import HttpResponse

#定义试图函数
def index(request):
    # return HttpResponse('OK!')
    #准备上下文:定义在字典中(测试数据)
    context = {'h2':'天天向上'}

    #将上下文交给模板中进行处理,处理后视图响应给客户端
    return render(request,'Book/index.html',context)