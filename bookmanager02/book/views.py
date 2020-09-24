from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#添加数据
# def create_book(request):
#     from book.models import BookInfo,PeopleInfo
    #方法一:创建模型类对象,执行对象的save()方法保存
    # book = BookInfo(
    #     name='java入门',
    #     pub_date='2020-1-1'
    # )
    # book.save()
    #方法二:通过模型类.objects.create()直接保存
    # BookInfo.objects.create(
    #     name='c语言入门',
    #     pub_date='1991-2-1'
    # )
    #
    # return HttpResponse('create')


#修改数据
# def update_book(request):
#     from book.models import BookInfo, PeopleInfo
#     #方法一:修改模型类对象的属性,然后执行save()方法
#     # book = BookInfo.objects.get(name='c语言入门')
#     # book.name = '汉语言入门'
#     # book.save()
#
#     #方法二:使用模型.objects.filter().update()直接修改,会返回受影响的行数
#     BookInfo.objects.filter(name='java入门').update(name='英语入门')


#删除数据



def del_book(request):
    from book.models import BookInfo,PeopleInfo
    #方法一:模型类对象.delete
    # book = BookInfo.objects.get(name='汉语言入门')
    # book.delete()

    #方法二:模型类.objects.filter.delete()
    BookInfo.objects.filter(name='英语入门').delete()
