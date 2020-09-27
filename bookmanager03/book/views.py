from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse('Good Good Study!')
def goods(request,cat_id,goods_id):
    print(cat_id,goods_id)
    return JsonResponse({'cat_id':cat_id,'goods_id':goods_id})
# def shop(request,cate_id,goods_id):
#     return JsonResponse({'cate_id':cate_id,'goods_id':goods_id})

#查询字符串
# def get(request):
#     a = request.GET.get('a')
#     b = request.GET.get('b')
#     alist = request.GET.getlist('a')
#     print(a)
#     print(b)
#     print(alist)
#     return HttpResponse('OK')
# def search(request):
#     num1 = request.GET.get('num1')
#     num2 = request.GET.get('mum2')
#     alist = request.GET.get('num1')
#     print(num1)
#     print(num2)
#     print(alist)
#     return HttpResponse('浩哥真帅!')

#请求from表单
def post(request):
    a = request.POST.get('a')
    print(a)
    return HttpResponse('ok')

#获取json数据
def post_json(request):
    #json数据不能通过request.POST获取数据
    body = request.body
    #返回二进制
    print(body)
    #转换成字符串
    body_str = body.decode()
    print(body_str,type(body_str))
    #讲json形式的字符串转换为Python的字典
    # 导入模块
    import json
    body_dict = json.loads(body_str)
    print(body_dict)
    #请求头
    #获取请求头中的端口信息
    print(request.META['SERVER_PORT'])
    return HttpResponse('json')

#获取请求方式,为GET方式
def method(request):
    print(request.method)
    return HttpResponse('method')

def response(request):
    info = {
        'name':'itcast',
        'password':123
    }
    friends = [
        {'name':1,"age":1},
        {'name':2,'age':2}
    ]
    #data 返回的响应数据一般是字典
    #safe=True表示这儿的data是字典类型
    #现在给了一个非字典类型,所以要改为False
    response = JsonResponse(data=friends,safe=False)
    # return response
    #重定向,返回一个网站
    return redirect('http://www.baidu.com')


#构造的响应状态吗为400
def res(request):
    # 响应头可以直接将HttpResponse对象当做字典进行响应头键值对的设置
    response = HttpResponse()
    response['itcast'] = 'python'
    return HttpResponse('itcast python',status=400)

def phone(request,mobile):
    print(mobile)
    return JsonResponse({'phone':mobile})


def set_cookie(request):
    #1.获取查询字符串数据
    username = request.GET.get('username')
    #2.服务器设置cookie信息
    #t通过响应对象.set_cookie 方法
    response = HttpResponse('set_cookie')
    #max_age 是一个秒数,从响应开始计数
    response.set_cookie('name',username,max_age=60)
    return response

def get_cookie(request):
    #获取cookie
    print(request.COOKIES)
    #request.COOKIES是字典数据
    name = request.COOKIES.get('name')
    return HttpResponse(name)

#session是保存在服务器端
def set_session(request):
    #模拟获取用户信息
    username = request.GET.get('username')
    #设置session信息
    #假如通过模型查询,查询到了用户信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session['user_id']
    username = request.session['username']
    content = '{},{}'.format(user_id,username)
    return HttpResponse(content)

#类视图
from django.views.generic import View

#类视图继承与View
#类视图中的方法是采用http小写的方式来区分不同的请求方式
class LoginView(View):

    def get(self,request):
        return HttpResponse('get方式')

    def post(self,request):
        return HttpResponse('post方式')

#类视图的多继承

#我的订单\个人中心页面,如果登录用户,可以访问,未登录,跳转到登录页面
from django.contrib.auth.mixins import LoginRequiredMixin

#LoginRequiredMixin 作用:判断只有登录用户才可以访问页面
class OrderView(LoginRequiredMixin,View):

    def get(selfs,request):
        return HttpResponse('Get 我的订单页面,这个页面必须登录')

    def post(self,request):
        return HttpResponse('POST 我的订单页面,这个页面必须登录')

############中间件###############
