	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r11
	imulq $5, %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	subq $10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq $21474836440, %r10
	cmpq %r10, -32(%rbp)
	movl $0, -36(%rbp)
	setE -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Ltmp.6
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.6:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq $4294967290, %r10
	movq %r10, -8(%rbp)
	movq -8(%rbp), %rdi
	call target
	movl %eax, -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
