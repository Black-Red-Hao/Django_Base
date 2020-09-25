from django.urls import path

from Http.views import index

urlpatterns = [
    path('index/',index)
]