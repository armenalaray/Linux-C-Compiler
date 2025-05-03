	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $56, %rsp
	movl $0, -4(%rbp)
	movl $0, -8(%rbp)
.Ltmp.5:
	cmpl $10, -8(%rbp)
	movl $0, -12(%rbp)
	setL -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.3
	movl $0, -20(%rbp)
.Ltmp.8:
	cmpl $10, -20(%rbp)
	movl $0, -24(%rbp)
	setL -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	cmpl $0, -28(%rbp)
	jE .Lbreak_tmp.4
	movl -8(%rbp), %eax
	cdq
	movl $2, %r10d
	idivl %r10d
	movl %eax, -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	movl -36(%rbp), %r11d
	imull $2, %r11d
	movl %r11d, -36(%rbp)
	movl -8(%rbp), %r10d
	cmpl %r10d, -36(%rbp)
	movl $0, -40(%rbp)
	setE -40(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -44(%rbp)
	cmpl $0, -44(%rbp)
	jE .Ltmp.16
	jmp .Lbreak_tmp.4
	jmp .Ltmp.15
.Ltmp.16:
	movl -4(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movl -8(%rbp), %r10d
	addl %r10d, -48(%rbp)
	movl -48(%rbp), %r10d
	movl %r10d, -4(%rbp)
.Ltmp.15:
.Lcontinue_tmp.4:
	movl -20(%rbp), %r10d
	movl %r10d, -52(%rbp)
	addl $1, -52(%rbp)
	movl -52(%rbp), %r10d
	movl %r10d, -20(%rbp)
	jmp .Ltmp.8
.Lbreak_tmp.4:
.Lcontinue_tmp.3:
	movl -8(%rbp), %r10d
	movl %r10d, -56(%rbp)
	addl $1, -56(%rbp)
	movl -56(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.5
.Lbreak_tmp.3:
	movl -4(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
