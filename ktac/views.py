# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
import ktapp.settings

import os
import sys
import ktacs
import logging

logger = logging.getLogger('sourceDns.webdns.views')

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
        if host == 'all':
            self.host = 'a'
        if process == 'all':
            self.process = None
        if net == 'all':
            self.net = None
        self.procType = None
        self.cmd = cmd
        logger.debug('ktacMain: %s %s %s %s', cmd,host,process,net)

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
    logger.debug(request)
    ktmain = ktacMain('q', None, None, None)
    result = ktmain.start()
    logger.debug(result)
    # result = '开通查询结果：'
    return JsonResponse({"result": result})

def ktproc(request):
    host = request.GET['host']
    proc = request.GET['process']
    netele = request.GET['ne']
    cmd = request.GET['cmd']
    logger.debug('host:%s proc:%s net:%s cmd:%s',host,proc,netele,cmd)
    ktmain = ktacMain(cmd, host, proc, netele)
    result = ktmain.start()
    return JsonResponse({"result": result})
