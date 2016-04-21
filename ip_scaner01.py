#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
__author__ = 'tangchao'

start = time.time()
begin = 1
end = 255
for i in range(begin, end):
    ip = '10.42.119.' + str(i)
    cmd = 'ping -n 1 %s\n' % ip
    p = os.popen(cmd).readline()
    for line in p:
        if not line:
            continue
        if line.upper().find('TTL') >= 0:
            print "ip: %s is ok ***" % ip
            break
end = time.time()
print "Elapsed time: %.2fs\n" % (end - start)
