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
    
    movl $2, -4(%rbp)

    movl $9, %eax

    cdq

    idivl -4(%rbp)

    movl %edx, %eax

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