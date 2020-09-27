from django.utils.deprecation import MiddlewareMixin


class TestMiddleware1(MiddlewareMixin):
    def process_request(self,request):
        print('请求前1被调用')

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('处理视图1前调用')
        # username = request.COOKIES.get('name')
        # if username is None:
        #     print('没有用户信息')
        # else:
        #     print('有用户信息')

    def process_response(self,request,response):
        print('响应1前调用')
        return response


# class TestMiddleware2(MiddlewareMixin):
#
#     def process_request(self,request):
#         print('请求前2调用')
#
#     def process_view(self,request,view_func,view_args,view_kwargs):
#         print('处理视图前2调用')
#
#     def process_response(self,request,response):
#         print('响应前2调用')
#         return response
