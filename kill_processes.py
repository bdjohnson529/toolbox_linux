import os
import sys

processName = "vansCollect"
pid = []

# find offending processes
for dirname in os.listdir('/proc'):
    if dirname == 'curproc':
        continue

    try:
        with open('/proc/{}/stat'.format(dirname)) as fd:
            line = fd.readline()
            array = line.split()
    except Exception:
        continue

    if processName in line and "T" in array[2]:
        pid.append( array[0] )

# kill processes
for process in pid:
    os.system("kill -9 " + process)
