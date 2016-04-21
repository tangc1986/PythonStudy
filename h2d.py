# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import sys

for i in range(1, len(sys.argv)):
    print "0x%x\t= %d" % (int(sys.argv[i], 16), int(sys.argv[i], 16))

