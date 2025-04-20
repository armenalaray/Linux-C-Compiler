
#python3 -m pdb "$(pwd)"/code/cd.py "$(pwd)"/test/test.c

# My compiler


python3 "$(pwd)"/code/cd.py --lex "$(pwd)"/test/test.c

exit_status=$?
echo $exit_status

number=0
if [ $exit_status -eq $number ]; then
    ls -la /home/alejandro/CComp/test/test
    ./test/test
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
#./bin/return
#echo $?

gdb -x gdbcommands.txt 
#--args bin/return 
'

