from django.urls import path

from Http.views import index,shop,phone

# 定义转换器,实现判断电话号码
from django.urls import register_converter


class MobileConverter:
    # 判断数据,正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题,讲数据给视图函数
    def to_python(self, value):
        return value


# 使用转换器,必须先注册
#phone转换器注册成功
register_converter(MobileConverter, 'phone')
urlpatterns = [
    path('index/',index),
    #对goods_id设置转换器,必须为整形
    path('<city_id>/<int:goods_id>/',shop),
    path('<phone:mobile>/',phone)

]