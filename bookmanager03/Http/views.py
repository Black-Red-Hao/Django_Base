from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


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

# #设置响应体
# def response(request):
#     #status设置状态码
#     # response = HttpResponse('response',status=200)
#     # #设置响应头
#     # response['name'] = 'itcast'
#
#
#     info = {
#         'name':'itcast',
#         'address':'shunyi'
#     }
#     friends = [
#         {
#             'name':'xiaoming',
#             'age':15
#         },
#         {
#             'name':'xiaozhang',
#             'age':13
#         }
#     ]
#     #data 返回的响应数据一般是字典类型
#     #JsonResponse可以把字典转换为json
#     #如果给的是非字典类型,需要修改safe,safe=True表示data是字典类型
#     response = JsonResponse(data=info)
#     response = JsonResponse(data=friends,safe=False)
#     return response
#
# #redirect重定向
# def red(request):
#     return redirect('http://www.baidu.com')


#状态保持
#设置Cookie,通过HttpResponse中的set_cookie方法来设置
def set_cookie(request):
    #1.获取查询字符串数据
    user=request.GET.get('user')
    pswd=request.GET.get('pswd')
    #2.服务器设置cookie信息
    response = HttpResponse('set_cookie')
    #HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
    response.set_cookie('name',user)
    #max_age设置秒数,从响应开始计数
    response.set_cookie('pwd',pswd,max_age=3600)
    #删除cookie
    # response.delete_cookie('name')
    return response

def get_cookie(request):
    #获取cookie
    print(request.COOKIES)
    #request>COOKIES为字典数据
    name = request.COOKIES.get('name')
    return HttpResponse(name)

#设置session
def set_session(request):
    #1.模拟用户信息
    user = request.GET.get('user')
    #2.设置session信息
    #假如通过模型查询,查到了用户信息
    user_id=1
    request.session['user_id']=user_id
    request.session['username']=user
    #设置有效期
    request.session.set_expiry(3600)
    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    user = request.session.get('username')
    content = '{},{}'.format(user_id,user)
    return HttpResponse(content)

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

##################HttpResponse对象########################

def response(request):
    # 设置响应状态
    # return HttpResponse('response',status=200)
    #设置相应头
    # response['name'] = 'haoge'
    # return response
    info = {
        'name':'itcast',
        'age':12
    }
    friends = [
        {
            "name":'小花',
            "age":12
        },
        {
          "name":'小米',
          "age":11
        }
    ]
    #JsonResponse可以吧字典转换为json
    #data返回数据响应一般是字典类型
    #safe=True表示data是字典数据
    #如果接受了一个非字典类型的数据,要将safe修改为false
    response = JsonResponse(data=info)
    response = JsonResponse(data=friends,safe=False)
    return response

#redirect重定向
def red(request):
    return HttpResponse('http://www.baidu.com')
