
#python3 -m pdb "$(pwd)"/code/cd.py "$(pwd)"/test/test.c

# My compiler



lastStage="--parse"
#noLink="-c"
library="-lmath.h"

python3 "$(pwd)"/code/cd.py $lastStage $noLink $library "$(pwd)"/test_/test.c
echo $?


if test -f test_/test; then
    ./test_/test
    echo "from test: "$?
fi




#python3 "$(pwd)"/code/test.py

# Real compiler
: '
gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none test/test.c -o test/test.s
echo $?
'



# assembler

: '
gcc "$(pwd)"/bin/return.s -o bin/return
./bin/return
echo $?
'


#gdb -x gdbcommands.txt 
#--args bin/return 

