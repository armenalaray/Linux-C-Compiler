	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq $9223372036854775807, %r10
	movq %r10, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	subq $2, -16(%rbp)
	movq $9223372036854775805, %r10
	cmpq %r10, -16(%rbp)
	movl $0, -20(%rbp)
	setE -20(%rbp)
	movl -20(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
