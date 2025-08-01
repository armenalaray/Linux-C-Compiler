	.globl foo
	.text
foo:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -12(%rbp)
	movl -12(%rbp), %edi
	call putchar
	movl %eax, -16(%rbp)
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movl $65, -4(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %rdi
	call foo
	movl %eax, -28(%rbp)
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
	call target
	movl %eax, -4(%rbp)
	movl -4(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
