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