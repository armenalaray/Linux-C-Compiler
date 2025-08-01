	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	leaq i+0(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, glob+0(%rip)
	movq -16(%rbp), %rax
	movl 0(%rax), %r10d
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
	cmpl $10, -4(%rbp)
	movl $0, -8(%rbp)
	setNE -8(%rbp)
	cmpl $0, -8(%rbp)
	jE .Ltmp.6
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.6:
	movq glob+0(%rip), %rax
	movl 0(%rax), %r10d
	movl %r10d, -12(%rbp)
	cmpl $10, -12(%rbp)
	movl $0, -16(%rbp)
	setNE -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Ltmp.10
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.10:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl glob
	.bss
	.align 8
glob:
	.zero 8
	.globl i
	.data
	.align 4
i:
	.long 10
	.section	.note.GNU-stack,"",@progbits
