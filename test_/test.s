	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $36, %rsp
	movl $5, -4(%rbp)
	negl -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	movl -8(%rbp), %r11d
	imull $4, %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	cdq
	movl $2, %r10d
	idivl %r10d
	movl %eax, -12(%rbp)
	movl $2, -16(%rbp)
	addl $1, -16(%rbp)
	movl $3, %eax
	cdq
	idivl -16(%rbp)
	movl %edx, -20(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -24(%rbp)
	movl -20(%rbp), %r10d
	subl %r10d, -24(%rbp)
	movl $20, -28(%rbp)
	notl -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	subl $4, -32(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -36(%rbp)
	movl -32(%rbp), %r10d
	subl %r10d, -36(%rbp)
	movl -36(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
