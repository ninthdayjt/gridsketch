import time
import math
import os
import sys
import color_adapter as ca

import adapter_test as adapter1

inputdir = sys.argv[1]
outputdir = sys.argv[2]

C = ca.COLOR(projList=['test'])


def go(fullname, filename):
    if '.nc' in filename or '.NC' in filename:
        adapter1.adapter(fullname, filename, outputdir, C.get('test'))

start = time.clock()

for parent, dirnames, filenames in os.walk(inputdir):
    for filename in filenames:
        fullname = os.path.join(parent, filename)
        go(fullname, filename)


end = time.clock()
print("time: %f s" % (end - start))
