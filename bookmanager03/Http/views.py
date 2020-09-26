from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('o_o')

#获取路径值
def shop(request,city_id,goods_id,):
    print(city_id,goods_id)
    return HttpResponse('浩哥的店铺')

#获取电话号码
def phone(request,mobile):
    print(mobile)
    return JsonResponse({'phone':mobile})

#查询字符串,即网址中?后面的数据
def get(request):
    #get只能实现一键一值
    name = request.GET.get('name')
    id = request.GET.get('id')
    #getlist可以实现一键多值
    all_name = request.GET.getlist('name')
    print(name,id)
    print(all_name)
    return HttpResponse('get')

def post(request):
    #json不能通过request.POST获取数据
    data = request.POST
    print(data)
    return HttpResponse('ok')

def json(request):
    body = request.body
    #返回的数据位byte类型
    print(body)
    #转换成字符串
    body_str = body.decode()
    print(body_str)
    #将json形式的字符串转换为Python的字典
    #注意:json中书写的属性名称必须用双引号括起来
    """
    {
        "name":1,
        "age":1
    }
    """
    #导入json模块
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    return HttpResponse('json')