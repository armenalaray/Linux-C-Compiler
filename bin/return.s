    .globl main
main:
    # prologue
    # -2 2 1

    # base pointer
    pushq %rbp
    movq %rsp, %rbp

    # stack pointer
    subq $8, %rsp
    
    # store 2 in rbp -4
    movl $2, -4(%rbp)

    # aqui ya lo moviste se nega en la memoria
    # 32 bit value
    # esta es la direccion de memoria
    negl -4(%rbp)

    # aqui la movemos a -8
    movl -4(%rbp), %r10d
    movl %r10d, -8(%rbp)

    #this is ~
    notl -8(%rbp)

    movl -8(%rbp), %eax

    # function epilogue
    # aqui lo esta bajandro el stack
    movq %rbp, %rsp
    popq %rbp

    # baja el stack siempre
    # digamos que apunta hasta abajo

    ret