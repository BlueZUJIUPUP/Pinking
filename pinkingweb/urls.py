# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 10:31
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from .Views.Testcase import Testcase#, TestcaseList
from .Views.Task import Task

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('testcase/',Testcase.as_view(),name = "testcase"),
    # path('testcaselist/',TestcaseList,name = "testcaselist"),
    path('task/',Task.as_view(),name = "Task"),
]