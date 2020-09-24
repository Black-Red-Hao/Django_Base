from django.urls import path
from book.views import goods

urlpatterns = [
    # path('index/',index)
    path('<cat_id>/<goods_id>/',goods),

]