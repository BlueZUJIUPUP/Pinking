# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 13:58
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Models.py
# @Software: PyCharm
#
from django.db import models

class Testcase_models(models.Model):
    id = models.AutoField(primary_key=True)
    nodeID = models.CharField(max_length=20)
    remark = models.CharField(max_length=50,default=0)

    class Meta:
        db_table = "Testcase"