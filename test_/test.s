	.globl foo
	.text
foo:
	pushq %rbp
	movq %rsp, %rbp
	subq $224, %rsp
	movq %rdi, -8(%rbp)
	movl %esi, -12(%rbp)
	movl %edx, -16(%rbp)
	movl %ecx, -20(%rbp)
	movq %r8, -32(%rbp)
	movl %r9d, -36(%rbp)
	movq 16(%rbp), %r10
	movq %r10, -48(%rbp)
	movl 24(%rbp), %r10d
	movl %r10d, -52(%rbp)
	movq $1, -64(%rbp)
	negq -64(%rbp)
	movq -64(%rbp), %r10
	cmpq %r10, -8(%rbp)
	movl $0, -68(%rbp)
	setNE -68(%rbp)
	movl -68(%rbp), %r10d
	movl %r10d, -72(%rbp)
	cmpl $0, -72(%rbp)
	jE .Ltmp.19
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.19:
	cmpl $2, -12(%rbp)
	movl $0, -84(%rbp)
	setNE -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -88(%rbp)
	cmpl $0, -88(%rbp)
	jE .Ltmp.23
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.23:
	cmpl $0, -16(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.27
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -112(%rbp)
	movq -112(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.27:
	movl $5, -116(%rbp)
	negl -116(%rbp)
	movl -116(%rbp), %r10d
	cmpl %r10d, -20(%rbp)
	movl $0, -120(%rbp)
	setNE -120(%rbp)
	movl -120(%rbp), %r10d
	movl %r10d, -124(%rbp)
	cmpl $0, -124(%rbp)
	jE .Ltmp.32
	movl $4, %r10d
	movslq %r10d, %r11
	movq %r11, -136(%rbp)
	movq -136(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.32:
	movq $101, -144(%rbp)
	negq -144(%rbp)
	movq -144(%rbp), %r10
	cmpq %r10, -32(%rbp)
	movl $0, -148(%rbp)
	setNE -148(%rbp)
	movl -148(%rbp), %r10d
	movl %r10d, -152(%rbp)
	cmpl $0, -152(%rbp)
	jE .Ltmp.37
	movl $5, %r10d
	movslq %r10d, %r11
	movq %r11, -160(%rbp)
	movq -160(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.37:
	movl $123, -164(%rbp)
	negl -164(%rbp)
	movl -164(%rbp), %r10d
	cmpl %r10d, -36(%rbp)
	movl $0, -168(%rbp)
	setNE -168(%rbp)
	movl -168(%rbp), %r10d
	movl %r10d, -172(%rbp)
	cmpl $0, -172(%rbp)
	jE .Ltmp.42
	movl $6, %r10d
	movslq %r10d, %r11
	movq %r11, -184(%rbp)
	movq -184(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.42:
	movq $10, -192(%rbp)
	negq -192(%rbp)
	movq -192(%rbp), %r10
	cmpq %r10, -48(%rbp)
	movl $0, -196(%rbp)
	setNE -196(%rbp)
	movl -196(%rbp), %r10d
	movl %r10d, -200(%rbp)
	cmpl $0, -200(%rbp)
	jE .Ltmp.47
	movl $7, %r10d
	movslq %r10d, %r11
	movq %r11, -208(%rbp)
	movq -208(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.47:
	cmpl $1234, -52(%rbp)
	movl $0, -212(%rbp)
	setNE -212(%rbp)
	movl -212(%rbp), %r10d
	movl %r10d, -216(%rbp)
	cmpl $0, -216(%rbp)
	jE .Ltmp.51
	movl $8, %r10d
	movslq %r10d, %r11
	movq %r11, -224(%rbp)
	movq -224(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.51:
	movq -8(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $240, %rsp
	movl $1, -4(%rbp)
	negl -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	movq $4294967298, %r10
	movq %r10, -16(%rbp)
	movq $4294967296, %r10
	movq %r10, -24(%rbp)
	negq -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq $21474836475, %r10
	movq %r10, -40(%rbp)
	movl $101, -44(%rbp)
	negl -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movl $123, -52(%rbp)
	negl -52(%rbp)
	movslq -52(%rbp), %r11
	movq %r11, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movl $10, -76(%rbp)
	negl -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	movq $9223372036854774574, %r10
	movq %r10, -88(%rbp)
	negq -88(%rbp)
	movq -88(%rbp), %r10
	movq %r10, -96(%rbp)
	movslq -8(%rbp), %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %r10
	movq %r10, -112(%rbp)
	movl -16(%rbp), %r10d
	movl %r10d, -116(%rbp)
	movl -116(%rbp), %r10d
	movl %r10d, -128(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -132(%rbp)
	movl -132(%rbp), %r10d
	movl %r10d, -144(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -148(%rbp)
	movl -148(%rbp), %r10d
	movl %r10d, -160(%rbp)
	movslq -48(%rbp), %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -180(%rbp)
	movl -180(%rbp), %r10d
	movl %r10d, -192(%rbp)
	movslq -80(%rbp), %r11
	movq %r11, -200(%rbp)
	movq -200(%rbp), %r10
	movq %r10, -208(%rbp)
	movl -96(%rbp), %r10d
	movl %r10d, -212(%rbp)
	movl -212(%rbp), %r10d
	movl %r10d, -224(%rbp)
	movq -112(%rbp), %rdi
	movl -128(%rbp), %esi
	movl -144(%rbp), %edx
	movl -160(%rbp), %ecx
	movq -176(%rbp), %r8
	movl -192(%rbp), %r9d
	movl -224(%rbp), %eax
	pushq %rax
	pushq -208(%rbp)
	call foo
	addq $16, %rsp
	movq %rax, -232(%rbp)
	movl -232(%rbp), %r10d
	movl %r10d, -236(%rbp)
	movl -236(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
