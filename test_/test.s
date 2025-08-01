	.globl callee
	.text
callee:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, b+0(%rip)
	movq -8(%rbp), %rax
	movl $100, 0(%rax)
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
	movl $10, -4(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rdi
	call callee
	movl -4(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -20(%rbp), %eax
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
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	cmpl $100, -8(%rbp)
	movl $0, -12(%rbp)
	setNE -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.10
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.10:
	cmpl $10, b+0(%rip)
	movl $0, -16(%rbp)
	setNE -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Ltmp.13
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.13:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl b
	.bss
	.align 4
b:
	.zero 4
	.section	.note.GNU-stack,"",@progbits
