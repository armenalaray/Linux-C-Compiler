    .globl main
main:
    # prologue
    # -2 2 1

    pushq %rbp
    movq %rsp, %rbp
    subq $8, %rsp
    
    # store 2 in rbp -4
    movl $2, -4(%rbp)
    
    3 negl -4(%rbp)
    4 movl -4(%rbp), %r10d
    5 movl %r10d, -8(%rbp)
    6 notl -8(%rbp)
    7 movl -8(%rbp), %eax

    movq %rbp, %rsp
    popq %rbp
    ret