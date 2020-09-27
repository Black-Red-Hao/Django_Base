from django.urls import path
from book.views import goods, index, post, post_json, \
    response, res, method, phone, set_cookie, get_cookie, \
    set_session, get_session, LoginView, OrderView

from django.urls.converters import register_converter
#1.定义转换器
class MobileConverter:
    #验证数据的关键是 : 正则
    regex = '1[3-9]\d{9}'
    #验证没有问题的数据给视图函数
    def to_python(self,value):
        return value
#必须先注册转换器
register_converter(MobileConverter,'phone')
urlpatterns = [
    path('index/',index),

    #<转换器名字:变量名>
    #转换器会对变量数据进行正则的验证
    path('<phone:mobile>/',phone),

    path('<int:cat_id>/<goods_id>/',goods),
    path('post/',post),
    path('json/',post_json),
    path('res/',response),
    path('abc/',res),
    path('method/',method),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('110.login/',LoginView.as_view()),
    path('order/',OrderView.as_view())
]