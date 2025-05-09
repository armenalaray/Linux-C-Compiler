	.globl foo
foo:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl bar
bar:
	pushq %rbp
	movq %rsp, %rbp
	subq $0, %rsp
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
