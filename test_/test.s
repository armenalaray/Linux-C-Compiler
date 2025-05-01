	.globl main
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $108, %rsp
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	movl -4(%rbp), %r10d
	cmpl %r10d, -8(%rbp)
	movl $0, -12(%rbp)
	setG -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Ltmp.14
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	movl -24(%rbp), %r11d
	imull -28(%rbp), %r11d
	movl %r11d, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -32(%rbp)
	movl -32(%rbp), %r11d
	imull -36(%rbp), %r11d
	movl %r11d, -32(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -40(%rbp)
	movl -32(%rbp), %r10d
	subl %r10d, -40(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movl -48(%rbp), %r11d
	imull -28(%rbp), %r11d
	movl %r11d, -48(%rbp)
	movl -48(%rbp), %r10d
	movl %r10d, -52(%rbp)
	movl -52(%rbp), %r11d
	imull -56(%rbp), %r11d
	movl %r11d, -52(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -60(%rbp)
	movl -52(%rbp), %r10d
	subl %r10d, -60(%rbp)
	movl -64(%rbp), %r10d
	movl %r10d, -68(%rbp)
	movl -68(%rbp), %r11d
	imull -28(%rbp), %r11d
	movl %r11d, -68(%rbp)
	movl -60(%rbp), %r10d
	movl %r10d, -72(%rbp)
	movl -68(%rbp), %r10d
	subl %r10d, -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	jmp .Ltmp.13
.Ltmp.14:
	movl $2, -80(%rbp)
	movl -80(%rbp), %r11d
	imull -20(%rbp), %r11d
	movl %r11d, -80(%rbp)
	movl -80(%rbp), %r10d
	movl %r10d, -84(%rbp)
	movl -84(%rbp), %r11d
	imull -28(%rbp), %r11d
	movl %r11d, -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -88(%rbp)
	movl -88(%rbp), %r11d
	imull -36(%rbp), %r11d
	movl %r11d, -88(%rbp)
	movl -88(%rbp), %r10d
	movl %r10d, -92(%rbp)
	movl $2, -96(%rbp)
	movl -96(%rbp), %r11d
	imull -44(%rbp), %r11d
	movl %r11d, -96(%rbp)
	movl -96(%rbp), %r10d
	movl %r10d, -100(%rbp)
	movl -100(%rbp), %r11d
	imull -28(%rbp), %r11d
	movl %r11d, -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	movl -104(%rbp), %r11d
	imull -56(%rbp), %r11d
	movl %r11d, -104(%rbp)
	movl -104(%rbp), %r10d
	movl %r10d, -108(%rbp)
.Ltmp.13:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
