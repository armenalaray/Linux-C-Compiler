	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $24, %rsp
	movl $12345, -4(%rbp)
	movl $5, -8(%rbp)
.Ltmp.3:
	cmpl $0, -8(%rbp)
	movl $0, -12(%rbp)
	setGE -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.2
	movl -4(%rbp), %eax
	cdq
	movl $3, %r10d
	idivl %r10d
	movl %eax, -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -4(%rbp)
.Lcontinue_tmp.2:
	movl -8(%rbp), %r10d
	movl %r10d, -24(%rbp)
	subl $1, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.3
.Lbreak_tmp.2:
	movl -4(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
