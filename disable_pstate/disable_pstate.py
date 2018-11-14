import sys
import re

input_file = sys.argv[1]
output_file = 'tmp.txt'

input_f = open(input_file)
output_f = open(output_file, "w+")

for line in input_f:

	if 'GRUB_CMDLINE_LINUX_DEFAULT' in line:
		# disable pstate driver on boot
		arr = line.rsplit('"', 1)
		arr[0] = arr[0] + " intel_pstate=disable "
		line = arr[0] + '"' + arr[1]

	output_f.write(line)
