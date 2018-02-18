import os
import sys
from time import sleep


def FindProcess(processName):

    pid_list = []

    dirs = sorted( os.listdir('/proc') )

    for dirname in dirs:

        if dirname == 'curproc':
            continue

        try:
            with open('/proc/{}/stat'.format(dirname)) as fd:
                line = fd.readline()
                array = line.split()

                if processName in line:
                    pid = array[0]
                    pid_list.append( pid )

        except Exception:
            continue

    return pid_list


def KillProcess(process):

    messageTerm = "Terminate process " + str(process) + " ? (Y/n) "
    yes = {'yes', 'y', 'Yes', 'Y', 'YES'}
    no = {'no', 'n', 'No', 'N', 'NO'}

    approve=raw_input(messageTerm)

    while True:

        if approve in yes:

            print "Terminating process " + str(process)
            os.system("kill -9 " + process)
            return True

        elif approve in no:

            print "Skipped."
            return False


def main():

    processName = raw_input("search for this process: ")

    while True:
        pid_list = []

        pid_list = FindProcess(processName)

        if not pid_list:
            print "No more instances found containing " + processName
            return 0


        for i in range(0,len(pid_list) ):
            ret = KillProcess(pid_list[i])
            if ret:
                print "Successfully terminated."
                sleep(0.1)
                break


if __name__ == "__main__":
    main()