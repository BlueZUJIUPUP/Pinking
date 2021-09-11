# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 0:03
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include

from .views import UserInfo

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',UserInfo.as_view(),name = "UserInfo"),
]