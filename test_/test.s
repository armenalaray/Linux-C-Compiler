	.globl callee
	.text
callee:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl $0, -4(%rbp)
	cmpl $0, -4(%rbp)
	jE .Ltmp.3
	call callee
	movl %eax, -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	jmp .Ltmp.2
.Ltmp.3:
	movl $40, -12(%rbp)
.Ltmp.2:
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	addl $5, -16(%rbp)
	movl -16(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	call target
	movl %eax, -4(%rbp)
	movl -4(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
