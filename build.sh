
#python3 -m pdb "$(pwd)"/code/cd.py "$(pwd)"/test/test.c

#compile

python3 "$(pwd)"/code/cd.py "$(pwd)"/test/test.c
exit_status=$?
echo $exit_status

number=0
if [ $exit_status -eq $number ]; then
    ls -la /home/alejandro/CComp/test/test
    ./test/test
    echo $?
fi

#python3 "$(pwd)"/code/test.py

#gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none "$(pwd)"/test/test.i -o test/test.s

#./bin/cd test.c

#compiler

#assembler
#gcc "$(pwd)"/bin/return.s -o bin/return


#echo $?
