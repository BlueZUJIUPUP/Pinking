# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 14:02
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Task.py
# @Software: PyCharm

import datetime

from django.db import models
from django.utils import timezone


class Task_models(models.Model):
    id = models.AutoField(primary_key=True)
    remark = models.CharField(max_length=50,default=0)
    report = models.CharField(max_length=50,default='')
    create_at = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "Task"