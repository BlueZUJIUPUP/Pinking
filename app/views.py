from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View

from .models import User


class UserInfo(View):
    def get(self,request):
        User.objects.create(username="xiaohong",age=25)
        return HttpResponse("ok")