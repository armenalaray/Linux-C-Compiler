	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $20, %rsp
	movl $5, -4(%rbp)
	movl -4(%rbp), 
	movl , -4(%rbp)
	movl -4(%rbp), %eax
	movl $2, %r10d
	movl %eax, -8(%rbp)
	movl $2, -12(%rbp)
	movl $3, %eax
	movl , -16(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -16(%rbp), %r10d
	movl -20(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
