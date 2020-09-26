from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse('o_o')
#
# #获取路径值
# def shop(request,city_id,goods_id,):
#     print(city_id,goods_id)
#     return HttpResponse('浩哥的店铺')
#
# #获取电话号码
# def phone(request,mobile):
#     print(mobile)
#     return JsonResponse({'phone':mobile})
#
# #查询字符串,即网址中?后面的数据
# def get(request):
#     #get只能实现一键一值
#     name = request.GET.get('name')
#     id = request.GET.get('id')
#     #getlist可以实现一键多值
#     all_name = request.GET.getlist('name')
#     print(name,id)
#     print(all_name)
#     return HttpResponse('get')
#
# def post(request):
#     #json不能通过request.POST获取数据
#     data = request.POST
#     print(data)
#     return HttpResponse('ok')
#
# def json(request):
#     body = request.body
#     #返回的数据位byte类型
#     print(body)
#     #转换成字符串
#     body_str = body.decode()
#     print(body_str)
#     #将json形式的字符串转换为Python的字典
#     #注意:json中书写的属性名称必须用双引号括起来
#     """
#     {
#         "name":1,
#         "age":1
#     }
#     """
#     #导入json模块
#     import json
#     body_dict = json.loads(body_str)
#     print(body_dict)
#     # 请求头
#     print(request.META)
#     print(request.META['SERVER_PORT'])
#     return HttpResponse('json')
#
# #查询请求方式
# def method(request):
#     print(request.method)
#     return HttpResponse('method')

####################get请求和post请求############################
#路径请求
def home(request,city_id,home_id):
    print(city_id,home_id)
    return JsonResponse({'city_id':city_id,'home_id':home_id})

#添加转换器
def shop(request,good_money,mobile):
    print(good_money,mobile)
    return HttpResponse('浩哥的店铺')

#字符串查询
def get(request):
    #get方式实现一键一值
    name = request.GET.get('name')
    age = request.GET.get('age')
    print(name, age)
    #gitlist方式实现一键多值
    all_name = request.GET.getlist('name')
    print(all_name)
    return HttpResponse('get')

#post字符串查询
def post(request):
    # get方式实现一键一值
    name = request.POST.get('name')
    age = request.POST.get('age')
    print(name, age)
    # gitlist方式实现一键多值
    all_name = request.POST.getlist('name')
    print(all_name)
    return HttpResponse('post')

#表单查询
"""
    {
        "name":1,
        "age":1
    }
"""
def json(request):
    #json数据不能用response.POST获取数据
    body = request.body
    #获取到的是byte类型
    print(body)
    #转换为字符串类型
    body_str = body.decode()
    print(body_str)
    #json形式的字符串转换为Python的字典
    #导入json模块
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    #请求头
    print(request.META)
    print(request.META['SERVER_PORT'])
    return HttpResponse('json')

#查询请求方式
def method(request):
    print(request.method)
    return HttpResponse('method')
