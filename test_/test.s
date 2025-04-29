	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $36, %rsp
	movl $2147483646, -4(%rbp)
	movl $0, -8(%rbp)
	movl -4(%rbp), %eax
	cdq
	movl $6, %r10d
	idivl %r10d
	movl %eax, -12(%rbp)
	cmpl $0, -8(%rbp)
	movl $0, -16(%rbp)
	setE -16(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -16(%rbp), %r10d
	addl %r10d, -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	movl -28(%rbp), %r11d
	imull $2, %r11d
	movl %r11d, -28(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -32(%rbp)
	subl $1431655762, -32(%rbp)
	movl -32(%rbp), %r10d
	cmpl %r10d, -28(%rbp)
	movl $0, -36(%rbp)
	setE -36(%rbp)
	movl -36(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
