# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request,'ktac/index.html')

def ktac(request):
    result = '开通查询结果：'
    return JsonResponse({"result": result})

def ktexe(request):
    result = '开通执行结果：'
    return JsonResponse({"result": result})
