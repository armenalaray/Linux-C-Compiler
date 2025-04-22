    .globl main
main:
    # prologue
    # -2 2 1

    # base pointer
    #save the base pointer into the stack!
    #todo el control esta dentro de la funcion!

    #este es el pasado
    #pushq si te lo jala de la memoria
    pushq %rbp

    #en este preciso momento rsp apunta a address rbp
    #se esta moviendo hacia arriba crea el stack frame de la nueva funcion
    movq %rsp, %rbp

    # stack pointer
    #solo tienes 8 bytes
    subq $8, %rsp
    
    # esto es el codigo 
    # store 2 in rbp -4
    movl $2, -4(%rbp) stack(-4)

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


    # esto es el stack!!!!
    # function epilogue
    # aqui lo esta bajandro el stack
    movq %rbp, %rsp

    # este lo guarda en el rbp
    #vas a popear exactamente el address de rbp anterior a rbp
    popq %rbp

    # baja el stack siempre
    # digamos que apunta hasta abajo

    ret