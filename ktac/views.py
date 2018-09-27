# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import ktapp.settings

import os
import sys
import ktacs

# Create your views here.
def index(request):
    return render(request,'ktac/index.html')

def ktac(request):
    result = '开通查询结果：'
    return JsonResponse({"result": result})

class ktacMain(ktacs.Main):
    def __init__(self,cmd, host, process, net):
        self.Name = os.path.join('/app/kt4/operation/ktweb/', 'ktac/ktweb_ktac.py')
        self.baseName = os.path.basename(self.Name)
        self.argc = 4 #len(sys.argv)
        self.conn = None
        self.host = host
        self.process = process
        self.net = net
        self.procType = None
        self.cmd = cmd


    def checkArgv(self):
        if self.process is None and self.net is None:
            self.procType = 'all'
        else:
            self.procType = ''
            if self.process:
                self.procType = '%sp' % self.procType
            if self.net:
                self.procType = '%sn' % self.procType


def ktqry(request):
    ktmain = ktacMain('q', None, None, None)
    result = ktmain.start()
    # result = '开通查询结果：'
    return JsonResponse({"result": result})

def ktexe(request):
    result = '开通执行结果：'
    return JsonResponse({"result": result})
