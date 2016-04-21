# -*- coding: UTF-8 -*-
__author__ = 'tangchao'

import sys

for i in range(1, len(sys.argv)):
    print "%d\t= 0x%x" % (int(sys.argv[i]), int(sys.argv[i]))

