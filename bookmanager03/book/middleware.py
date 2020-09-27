from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print('请求前被调用')

    def process_view(self,request,view_func,view_args,view_kwargs):
        print('处理视图前调用')

    def process_response(self,request,response):
        print('响应前调用')
        return response
