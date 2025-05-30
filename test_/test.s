	.globl non_zero
	.text
non_zero:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd %xmm0, -8(%rbp)
	xorpd %xmm0, %xmm0
	comisd -8(%rbp), %xmm0
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.12:
	.double 2e+20
	.globl multiply_by_large_num
	.text
multiply_by_large_num:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd %xmm0, -8(%rbp)
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd -16(%rbp), %xmm15
	mulsd tmp.12(%rip), %xmm15
	movsd %xmm15, -16(%rbp)
	movsd -16(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.13:
	.double 2.5e-320
	.section .rodata
	.align 8
tmp.14:
	.double 4.999944335913415e-300
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movsd tmp.13(%rip), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd -16(%rbp), %xmm0
	call multiply_by_large_num
	movsd %xmm0, -24(%rbp)
	movsd -24(%rbp), %xmm15
	comisd tmp.14(%rip), %xmm15
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.9
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.9:
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd -40(%rbp), %xmm0
	call non_zero
	movl %eax, -44(%rbp)
	movl -44(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
