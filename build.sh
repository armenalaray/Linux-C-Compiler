
#python3 -m pdb "$(pwd)"/code/cd.py "$(pwd)"/test/test.c

# My compiler


#noLink="-c"


notAssembly="-S"

fC="--fold-constants"
pC="--propagate-copies"
eUC="--eliminate-unreachable-code"
eDS="--eliminate-dead-stores"
o="--optimize"

lastStage="--tacky"
library="-lmath.h"

python3 "$(pwd)"/code/cd.py $lastStage $noLink $notAssembly $library $fC $pC $eUC $eDS $o "$(pwd)"/test_/test.c
echo $?

if test -f test_/test; then
    ./test_/test
    echo "from test: "$?
fi

################################
#BUILD SYSTEM
#cd ./../
#echo "$(pwd)"
#pyinstaller --onefile "$(pwd)"/CComp/code/cd.py
#./writing-a-c-compiler-tests/test_compiler "$(pwd)"/dist/cd --chapter 19 --eliminate-unreachable-code





#python3 "$(pwd)"/code/test.py

# Real compiler

#gcc -S -fno-asynchronous-unwind-tables -fcf-protection=none test_/test.c -o test_/test.s
#gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none test_/test.c -o test_/optimizedtest.s
#echo $?




# assembler


#gcc "$(pwd)"/bin/main.s "$(pwd)"/bin/other.s -o bin/main
#./bin/main
#echo $?



#gdb -x gdbcommands.txt 
#--args bin/return 

