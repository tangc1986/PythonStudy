#! /usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import sys
import threading

__author__ = 'tangchao'


def pro(cc):
    ip = '10.42.119.' + str(cc)
    cmd = 'ping -n 1 %s\n' % ip
    p = os.popen(cmd).readline()
    for line in p:
        if not line:
            continue
        if line.upper().find('TTL') >= 0:
            sys.stdout.write("ip: %s is ok ***" % ip)
            break


def main():
    start = time.time()
    threads = []
    for i in range(1, 255):
        t = threading.Thread(target=pro, args=(i,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print "Elapsed time: %.2fs\n" % (end - start)


if __name__ == "__main__":
    main()
