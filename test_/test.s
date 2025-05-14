	.globl return_a
	.text
return_a:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl a(%rip), %eax
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
	subq $32, %rsp
	movl $3, -4(%rbp)
	cmpl $5, a(%rip)
	movl $0, -8(%rbp)
	setNE -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.3
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.3:
	movl $4, a(%rip)
	call return_a
	movl %eax, -16(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -16(%rbp), %r10d
	addl %r10d, -20(%rbp)
	movl -20(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl a
	.data
	.align 4
a:
	.long 5
	.section	.note.GNU-stack,"",@progbits
