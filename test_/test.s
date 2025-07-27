	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl $0, -4(%rbp)
	movl -4(%rbp), %eax
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
