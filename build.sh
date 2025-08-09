
#python3 -m pdb "$(pwd)"/code/cd.py "$(pwd)"/test/test.c

# My compiler


#noLink="-c"


notAssembly="-s"

fC="--fold-constants"
pC="--propagate-copies"
eUC="--eliminate-unreachable-code"
eDS="--eliminate-dead-stores"
o="--optimize"

#lastStage="--codegen"
library="-lmath.h"

python3 "$(pwd)"/code/cd.py $lastStage $noLink $notAssembly $library $fC $pC $eUC $eDS $o "$(pwd)"/test_/test.c > "$(pwd)"/test_/testOptimizations.txt

echo $?

#ASSEMBLER
gcc "$(pwd)"/test_/test.s "$(pwd)"/test_/util.s -o test_/test

./test_/test
echo "from test: "$?

#if test -f test_/test; then
#    ./test_/test
#    echo "from test: "$?
#fi

################################
#BUILD SYSTEM
#cd ./../
#echo "$(pwd)"
#pyinstaller --onefile "$(pwd)"/CComp/code/cd.py
#./writing-a-c-compiler-tests/test_compiler "$(pwd)"/dist/cd --chapter 19





#python3 "$(pwd)"/code/test.py

# Real compiler

#gcc -S -fno-asynchronous-unwind-tables -fcf-protection=none test_/test.c -o test_/test.s

#gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none bin/util.c -o bin/util.s
#echo $?




# assembler






#gdb -x gdbcommands.txt 
#--args bin/return 

