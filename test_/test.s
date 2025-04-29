	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $112, %rsp
	movl $2, -4(%rbp)
	movl $7, -8(%rbp)
	movl $0, -12(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -16(%rbp)
	movl -16(%rbp), %r11d
	imull -4(%rbp), %r11d
	movl %r11d, -16(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -20(%rbp), %r11d
	imull -8(%rbp), %r11d
	movl %r11d, -20(%rbp)
	movl -16(%rbp), %r10d
	movl %r10d, -24(%rbp)
	movl -20(%rbp), %r10d
	addl %r10d, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	cmpl $0, -28(%rbp)
	movl $0, -32(%rbp)
	setG -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.12
	movl $10, -12(%rbp)
	jmp .Ltmp.11
.Ltmp.12:
	cmpl $0, -28(%rbp)
	movl $0, -40(%rbp)
	setL -40(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -44(%rbp)
	cmpl $0, -44(%rbp)
	jE .Ltmp.15
	movl $10, -48(%rbp)
	negl -48(%rbp)
	movl -48(%rbp), %r10d
	movl %r10d, -12(%rbp)
	jmp .Ltmp.11
.Ltmp.15:
	cmpl $0, -28(%rbp)
	movl $0, -52(%rbp)
	setE -52(%rbp)
	movl -52(%rbp), %r10d
	movl %r10d, -56(%rbp)
	cmpl $0, -56(%rbp)
	jE .Ltmp.19
	movl $0, -12(%rbp)
	jmp .Ltmp.11
.Ltmp.19:
	movl $50, -12(%rbp)
.Ltmp.11:
	movl $4, -60(%rbp)
	movl $2, -64(%rbp)
	cmpl $0, -60(%rbp)
	jNE .Ltmp.20
	cmpl $0, -64(%rbp)
	jNE .Ltmp.20
	movl $0, -68(%rbp)
	jmp .Ltmp.22
.Ltmp.20:
	movl $1, -68(%rbp)
.Ltmp.22:
	movl -68(%rbp), %r10d
	movl %r10d, -72(%rbp)
	cmpl $0, -72(%rbp)
	jE .Ltmp.25
	cmpl $10, -12(%rbp)
	movl $0, -76(%rbp)
	setG -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.28
	movl $4, -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -88(%rbp)
	jmp .Ltmp.31
.Ltmp.28:
	movl $5, -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -88(%rbp)
.Ltmp.31:
	movl -88(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	jmp .Ltmp.24
.Ltmp.25:
	cmpl $2, -64(%rbp)
	movl $0, -96(%rbp)
	setG -96(%rbp)
	movl -96(%rbp), %r10d
	movl %r10d, -100(%rbp)
	cmpl $0, -100(%rbp)
	jE .Ltmp.35
	movl $4, -104(%rbp)
	movl -104(%rbp), %r10d
	movl %r10d, -108(%rbp)
	jmp .Ltmp.38
.Ltmp.35:
	movl $5, -112(%rbp)
	movl -112(%rbp), %r10d
	movl %r10d, -108(%rbp)
.Ltmp.38:
	movl -108(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.24:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
