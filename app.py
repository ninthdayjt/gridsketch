import time
import math
import os
import sys

from adapter_one import adapter as adapter1


inputdir = sys.argv[1]
outputdir = sys.argv[2]


def go(fullname, filename):

    if '.nc' in filename or '.NC' in filename:
        adapter1(fullname, filename, outputdir)


start = time.clock()

for parent, dirnames, filenames in os.walk(inputdir):
    for filename in filenames:
        fullname = os.path.join(parent, filename)
        go(fullname, filename)


end = time.clock()
print("time: %f s" % (end - start))
