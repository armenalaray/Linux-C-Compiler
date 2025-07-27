	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl %edi, -4(%rbp)
	movl %esi, -8(%rbp)
	movsd %xmm0, -16(%rbp)
	movsd -16(%rbp), %xmm14
	movsd %xmm14, -24(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -28(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -32(%rbp)
	movsd -16(%rbp), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd -40(%rbp), %xmm15
	addsd -16(%rbp), %xmm15
	movsd %xmm15, -40(%rbp)
	movsd -40(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.16:
	.double 10.0
	.section .rodata
	.align 8
tmp.17:
	.double 10.0
	.section .rodata
	.align 8
tmp.18:
	.double 20.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movl $0, -4(%rbp)
	movl $1, -8(%rbp)
	movsd tmp.16+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movl $0, %edi
	movl $1, %esi
	movsd tmp.17+0(%rip), %xmm0
	call target
	movsd %xmm0, -24(%rbp)
	movsd -24(%rbp), %xmm15
	comisd tmp.18+0(%rip), %xmm15
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -28(%rbp)
	jE .Ltmp.15
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.15:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
