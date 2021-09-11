# -*- coding: utf-8 -*-
# @Time    : 2021/9/11 13:57
# @Author  : BLUE_JUZIUPUP
# @Email   : z1003033614@163.com
# @File    : Testcase.py
# @Software: PyCharm
# Create your views here.
import json

from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .serializer import TaskSerializers
from ..Models.Task import Task_models


class Task(View):
    def get(self, request):
        try:
            res = request.GET.get('id', None)
            if not res:
                Task = Task_models.objects.all()
                ser = TaskSerializers(Task, many=True)
            else:
                Task = Task_models.objects.get(id=res)
                ser = TaskSerializers(Task)
            return JsonResponse({"error": 0, "msg": {"data": ser.data}}, safe=False)
        except:
            return JsonResponse({"error": 9000006, "msg": 'args except'})

    def post(self, request):
        try:
            res = json.loads(request.body)
            for i in res:
                Task_models.objects.create(remark=i['nodeID'], report=i['remark'])
            return JsonResponse({"error": 0,"errmsg": "created"})
        except:
            return JsonResponse({"error": 9000006, "msg": 'args except'})

    def put(self, request):
        try:
            res = json.loads(request.body)
        except:
            return JsonResponse({"error": 9000002, "msg": 'except'})
        id = res['oldData']['id']
        if id:
            try:
                ob = Task_models.objects.get(id=id)
            except:
                return JsonResponse({"error": 9000004, "msg": 'id except'})
            ob.nodeID, ob.remark = res['newData']['nodeID'], res['newData']['remark']
            ob.save()
            ser = TaskSerializers(ob)
            return JsonResponse({"error": 0, "data": ser.data, "msg": 'data success'})
        else:
            return JsonResponse({"error": 9000003, "msg": 'id except'})

    def delete(self, request):
        try:
            id = request.GET['id']
        except:
            return JsonResponse({"error": 9000005, "msg": 'id except'})
        res = Task_models.objects.get(id=id)
        if res:
            res.delete()
            return JsonResponse({"error": 0, "msg": 'delete success'})
        return JsonResponse({"error": 9000001, "msg": 'delete fail'})