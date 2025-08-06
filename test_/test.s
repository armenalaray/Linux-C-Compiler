	.section .rodata
	.align 8
tmp.95:
	.double 1.0
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd glob+0(%rip), %xmm12
	addsd tmp.95+0(%rip), %xmm12
	movsd %xmm12, %xmm13
	addsd glob+0(%rip), %xmm13
	movsd %xmm13, glob2+0(%rip)
	movsd %xmm12, %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.96:
	.double 11.0
	.section .rodata
	.align 8
tmp.97:
	.double 21.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	call target
	movsd %xmm0, %xmm13
	movsd %xmm13, %xmm0
	movsd tmp.96+0(%rip), %xmm1
	call check_one_double
	movl %eax, %r9d
	movsd glob2+0(%rip), %xmm0
	movsd tmp.97+0(%rip), %xmm1
	call check_one_double
	movl %eax, %r9d
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl glob
	.data
	.align 8
glob:
	.double 10.0
	.globl glob2
	.data
	.align 8
glob2:
	.double 0.0
	.section	.note.GNU-stack,"",@progbits
