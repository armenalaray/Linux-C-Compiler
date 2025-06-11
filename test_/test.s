	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl ale
	.data
	.align 8
ale:
	.double 0.0
	.globl c
	.bss
	.align 4
c:
	.zero 4
	.globl a
	.data
	.align 16
a:
	.long 1
	.long 2
	.zero 8
	.globl b
	.bss
	.align 16
b:
	.zero 16
	.section	.note.GNU-stack,"",@progbits
