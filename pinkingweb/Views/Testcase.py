# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 13:56
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Testcase.py
# @Software: PyCharm
import json

from django.http import JsonResponse, HttpResponse, QueryDict
from django.http.multipartparser import MultiPartParser
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .serializer import TestcaseSerializers
from ..Models.Testcase import Testcase_models

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# def TestcaseList(request):
#     Testcase = Testcase_models.objects.all()
#     ser = TestcaseSerializers(Testcase, many=True)
#     return JsonResponse(ser.data, safe=False)
def priority(args):
    if args == '高':
        return 2
    elif args == '中':
        return 1
    else:
        return 0


def status(args):
    if args == '可执行':
        return 0
    else:
        return 1


class Testcase(View):

    def get(self, request):
        try:
            res = request.GET.get('id', None)
            if not res:
                Testcase = Testcase_models.objects.all()
                ser = TestcaseSerializers(Testcase, many=True)
            else:
                Testcase = Testcase_models.objects.get(id=res)
                ser = TestcaseSerializers(Testcase)
            return JsonResponse({"error": 0, "msg": {"data": ser.data}}, safe=False)
        except:
            return JsonResponse({"error": 9000006, "msg": 'args except'})

    @csrf_exempt
    def post(self, request):
        try:
            # res = request.POST
            print(json.loads(request.body))
            res = json.loads(request.body)['params']
            print(f'res:{res["nodeID"]}')

        except:
            return JsonResponse({"error": 9000006, "msg": 'args except'})
        if not res['nodeID']:
            return JsonResponse({"error": 9000007, "msg": 'args except'})
        Testcase = Testcase_models.objects.create(
            nodeID=res['nodeID'],
            remark=res['remark'],
            priority=priority(res['priority']),
            status=status(res['status'])
        )
        ser = TestcaseSerializers(Testcase)
        return JsonResponse({"error": 0, "data": ser.data, "msg": 'data success'})

    def put(self, request):
        try:
            print(json.loads(request.body))
            res = json.loads(request.body)
            print(f'res:{res}')
            id = res['id']
        except:
            return JsonResponse({"error": 9000002, "msg": 'except'})
        # id = res['oldData']['id']
        if id:
            try:
                ob = Testcase_models.objects.get(id=id)
            except:
                return JsonResponse({"error": 9000004, "msg": 'id except'})
            ob.nodeID = res['nodeID']
            ob.remark = res['remark']
            ob.priority = priority(res['priority'])
            ob.status = status(res['status'])
            ob.create_time = timezone.now()
            ob.author = res['author']
            ob.save()
            ser = TestcaseSerializers(ob)
            return JsonResponse({"error": 0, "data": ser.data, "msg": 'data success'})

        else:
            return JsonResponse({"error": 9000003, "msg": 'id except'})


def delete(self, request):
    try:
        id = request.GET['id']
    except:
        return JsonResponse({"error": 9000005, "msg": 'id except'})
    res = Testcase_models.objects.get(id=id)
    if res:
        res.delete()
        return JsonResponse({"error": 0, "msg": 'delete success'})
    return JsonResponse({"error": 9000001, "msg": 'delete fail'})
