	.globl f
	.text
f:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movl %edi, -4(%rbp)
	movl %esi, -8(%rbp)
	movl $3, -12(%rbp)
	movl -12(%rbp), %r11d
	imul -8(%rbp), %r11d
	movl %r11d, -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	movl -4(%rbp), %r10d
	addl %r10d, -16(%rbp)
	movl $10, -20(%rbp)
	movl -16(%rbp), %r10d
	subl %r10d, -20(%rbp)
	movl -20(%rbp), %eax
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
	movl $1, -4(%rbp)
	movl $2, -8(%rbp)
	movl -4(%rbp), %edi
	movl -8(%rbp), %esi
	call f
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
