	.globl ale
	.text
ale:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movl %esi, -12(%rbp)
	movl -12(%rbp), %eax
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
	subq $48, %rsp
	movl $4, %r11d
	cmpl $2, %r11d
	movl $0, -4(%rbp)
	setA -4(%rbp)
	movslq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movl $4, %eax
	movl $0, %edx
	movl $2, %r10d
	divl %r10d
	movl %edx, -28(%rbp)
	movl -28(%rbp), %r11d
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.bss
	.align 4
i:
	.zero 4
	.bss
	.align 8
j:
	.zero 8
	.section	.note.GNU-stack,"",@progbits
