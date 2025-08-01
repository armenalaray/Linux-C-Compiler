	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl %edi, -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, i+0(%rip)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	addl $1, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl $2, %edi
	call target
	movl %eax, -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	cmpl $2, i+0(%rip)
	movl $0, -12(%rbp)
	setNE -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.8
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.8:
	cmpl $3, -8(%rbp)
	movl $0, -16(%rbp)
	setNE -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Ltmp.11
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.11:
	movl $1, -20(%rbp)
	negl -20(%rbp)
	movl -20(%rbp), %edi
	call target
	movl %eax, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	movl $1, -32(%rbp)
	negl -32(%rbp)
	movl -32(%rbp), %r10d
	cmpl %r10d, i+0(%rip)
	movl $0, -36(%rbp)
	setNE -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.18
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.18:
	cmpl $0, -28(%rbp)
	movl $0, -40(%rbp)
	setNE -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Ltmp.21
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.21:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl i
	.bss
	.align 4
i:
	.zero 4
	.section	.note.GNU-stack,"",@progbits
