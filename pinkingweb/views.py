from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


# class Testcase(View):
#     def get(self,request):
#         Testcase = Testcase_Models.objects.all()
#         print(Testcase)
#         ser = TestcaseSerializers(Testcase,many=True)
#         print(ser)
#         return JsonResponse(ser.data,safe=False)
#
#     @csrf_exempt
#     def post(self,request):
#         # Testcase.objects.create(nodeID="test01",remark=25)
#         a = request.POSsT.get('name','')
#         print(a)
#         return HttpResponse("ok")
#
# class Task(View):
#     def get(self,request):
#         Task = Task_models.objects.all()
#         ser = TaskSerializers(Task,many=True)
#         return JsonResponse(ser.data,safe=False)
#
#     @csrf_exempt
#     def post(self,request):
#         # Testcase.objects.create(nodeID="test01",remark=25)
#         a = request.POST.get('name','')
#         print(a)
#         return HttpResponse("ok")