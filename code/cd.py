import os
import sys

prepC = "gcc -E -P " + sys.argv[1] + " -o "

iFile = os.path.dirname(sys.argv[1]) + "/" +  os.path.basename(sys.argv[1]).split('.')[0] + ".i"

prepC = prepC + iFile

if os.system(prepC) == 0:
#note here you already have a file in the same directory

	print(iFile)

	compC = "gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none " + iFile + " -o " + os.path.dirname(sys.argv[1]) + "/" + os.path.basename(sys.argv[1]).split('.')[0] + ".s"

	print(compC)
	if os.system(compC) == 0:
		a = 2

	os.remove(iFile)

