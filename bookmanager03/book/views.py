from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse('Good Good Study!')
def goods(request,cat_id,goods_id):
    print(cat_id,goods_id)
    return JsonResponse({'cat_id':cat_id,'goods_id':goods_id})
def shop(request,cate_id,goods_id):
    return JsonResponse({'cate_id':cate_id,'goods_id':goods_id})

#查询字符串
def get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')
def search(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('mum2')
    alist = request.GET.get('num1')
    print(num1)
    print(num2)
    print(alist)
    return HttpResponse('浩哥真帅!')