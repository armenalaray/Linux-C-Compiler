	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
