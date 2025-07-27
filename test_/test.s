	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq $0, -8(%rbp)
	movq $0, -16(%rbp)
	movq $0, -24(%rbp)
	movq $0, %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	call target
	movq %rax, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	cmpq $0, -8(%rbp)
	movl $0, -20(%rbp)
	setE -20(%rbp)
	movl -20(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
