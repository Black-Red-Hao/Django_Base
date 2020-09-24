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



# def del_book(request):
#     from book.models import BookInfo,PeopleInfo
#     #方法一:模型类对象.delete
#     # book = BookInfo.objects.get(name='汉语言入门')
#     # book.delete()
#
#     #方法二:模型类.objects.filter.delete()
#     BookInfo.objects.filter(name='英语入门').delete()


#基本查询数据
# def search_book(request):
#     from book.models import BookInfo
#     # get查询:查询单一结果,如果结果不存在,抛出模型类.DoseNotExist异常
#     BookInfo.objects.get(id=1)
#     #all():查询多个结果
#     BookInfo.objects.all()
#     #count()查询结果数量
#     BookInfo.objects.count()


#过滤查询数据
#过滤条件的表达语法:属性名称__比较运算符=值
# def search_book(request):
#     from book.models import BookInfo
#     #exact:表示判等
#     #查询编号为1的图书
#     BookInfo.objects.filter(id__exact=1)
#     #简写为:
#     BookInfo.objects.filter(id=1)
#     #模糊查询
#     #contains:是否包含
#     #查询书名包含'传'的图书
#     BookInfo.objects.filter(name__contains='传')
#     #startswith,endswith:以指定值开头或结尾
#     #查询书名以'部'结尾的图书
#     BookInfo.objects.filter(name__endswith='部')
#     #空查询
#     #isnull:是否为null
#     #查询书名为空的图书
#     BookInfo.objects.filter(name__isnull=True)
#     #范围查询
#     #in:是否包含在范围内
#     #查询编号为1或3或5的图书
#     BookInfo.objects.filter(id__in=[1,3,5])
#     #比较查询
#     # gt大于(greater then)
#     # gte大于等于(greater then equal)
#     # lt小于(less then)
#     # lte小于等于(less then equal)
#     #查询编号大于3的图书
#     BookInfo.objects.filter(id__gt=3)
#     #查询编号不等于3
#     BookInfo.objects.filter(exclude(id=3))
#     #日期查询
#     #查询1980年发表的书
#     BookInfo.objects.filter(pub_date__year=1980)
#     #查询1990年1月1日后发表的书
#     BookInfo.objects.filter(pub_date__gt='1990-1-1')



#两个属性之间的比较
def comparation_book(request):
    from book.models import BookInfo,PeopleInfo
    #F对象
    #查询阅读量大于等于评论量的图书
    from django.db.models import F,Q
    BookInfo.objects.filter(readcount__gt=F('commentcount'))
    #查询阅读量大于2倍评论量的书
    BookInfo.objects.filter(readcount__gt=F('commentcount')*2)
    #Q对象
    #查询阅读量大于20,并且编号小于30的书
    BookInfo.objects.filter(readcount__gt=20,id__lt=3)
    #查询阅读量大于20或编号小于3的书,只能使用Q对象实现
    BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))
    #查询编号不等于3的书
    BookInfo.objects.filter(~Q(id=3))

    #使用aggregate()过滤器调用聚合函数
    #聚合函数包括:avg,count,max,min,sum
    #查询图书的总阅读量
    from django.db.models import Sum
    BookInfo.objects.aggregate(Sum('readcount'))
    #返回的是一个字典类型{'属性名__聚合类小写':值}
    #查询图书总数
    #使用count时一般不使用aggregate()过滤器
    BookInfo.objects.count()
    #排序使用order_by()
    #升序
    BookInfo.objects.all().order_by('readcount')
    #降序
    BookInfo.objects.all().order_by('-readcount')

    #关联查询
    # 由一对多的访问语法:一对应的模型类对象.多对应的模型类名小写__set
    #查询书籍为1的所有人物信息
    book = BookInfo.objects.get(id=1)
    book.peopleinfo_set.all()
    #由多对一的访问语句:多对应的模型类对象.多对应的模型类中的关系类属性名
    #查询人物为1的书籍信息
    person = PeopleInfo.objects.get(id=1)
    person.book
    #person.book_id

    #关联过滤查询
    #查询图书,要求图书中有人物郭靖
    book = BookInfo.objects.filter(peopleinfo__name='郭靖')
    book

    #查询图书,要求图书中的人物描述含有八
    book = BookInfo.objects.filter(peopleinfo__description__contains='八')
    book

    #查询书名为天龙八部的所有人物
    people = PeopleInfo.objects.filter(book__name='天龙八部')
    people

    #查询图书阅读量大于30的所有人物
    people = PeopleInfo.objects.filter(book__readcount__gt=30)
    people

