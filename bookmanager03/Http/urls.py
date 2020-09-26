from django.urls import path, register_converter

# from Http.views import index, shop, phone, post, json, get, method
#
# # 定义转换器,实现判断电话号码
# from django.urls import register_converter
#
#
# class MobileConverter:
#     # 判断数据,正则
#     regex = '1[3-9]\d{9}'
#
#     # 验证没有问题,讲数据给视图函数
#     def to_python(self, value):
#         return value
#
#
# # 使用转换器,必须先注册
# #phone转换器注册成功
# register_converter(MobileConverter, 'phone')
# urlpatterns = [
#     path('index/',index),
#     #对goods_id设置转换器,必须为整形
#     path('<city_id>/<int:goods_id>/',shop),
#     path('<phone:mobile>/',phone),
#     path('post/',post),
#     path('json/',json),
#     path('get/',get),
#     path('method/',method),
#
#
# ]

#####################################################
from Http.views import home, get, post, json, shop, method, response, red


#定义转换器
class MobileConverter:
    #判断数据,使用正则
    regex = '1[3-9]\d{9}'
    #验证没问题,将数据给视图函数
    def to_python(self,value):
        return value

#使用转换器,必须先注册
register_converter(MobileConverter,'phone')
urlpatterns = [
    # path('<city_id>/<home_id>/',home),
    path('get/',get),
    path('post/',post),
    path('json/',json),
    path('<good_money>/<phone:mobile>/',shop),
    path('method/',method),
    path('response/',response),
    path('red/',red),
]