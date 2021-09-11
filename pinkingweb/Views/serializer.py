# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 13:31
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : serializer.py
# @Software: PyCharm
from datetime import datetime

from rest_framework import serializers

class TestcaseSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    nodeID = serializers.CharField()
    remark = serializers.CharField()


class TaskSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    remark = serializers.CharField()
    report = serializers.CharField()
    create_at = serializers.DateTimeField()