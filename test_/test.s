	.globl foo
	.text
foo:
	pushq %rbp
	movq %rsp, %rbp
	subq $160, %rsp
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
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.19:
	cmpl $2, -12(%rbp)
	movl $0, -76(%rbp)
	setNE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.22
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.22:
	cmpl $0, -16(%rbp)
	movl $0, -84(%rbp)
	setNE -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -88(%rbp)
	cmpl $0, -88(%rbp)
	jE .Ltmp.25
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.25:
	movl $5, -92(%rbp)
	negl -92(%rbp)
	movl -92(%rbp), %r10d
	cmpl %r10d, -20(%rbp)
	movl $0, -96(%rbp)
	setNE -96(%rbp)
	movl -96(%rbp), %r10d
	movl %r10d, -100(%rbp)
	cmpl $0, -100(%rbp)
	jE .Ltmp.29
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.29:
	movq $101, -112(%rbp)
	negq -112(%rbp)
	movq -112(%rbp), %r10
	cmpq %r10, -32(%rbp)
	movl $0, -116(%rbp)
	setNE -116(%rbp)
	movl -116(%rbp), %r10d
	movl %r10d, -120(%rbp)
	cmpl $0, -120(%rbp)
	jE .Ltmp.33
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.33:
	movl $123, -124(%rbp)
	negl -124(%rbp)
	movl -124(%rbp), %r10d
	cmpl %r10d, -36(%rbp)
	movl $0, -128(%rbp)
	setNE -128(%rbp)
	movl -128(%rbp), %r10d
	movl %r10d, -132(%rbp)
	cmpl $0, -132(%rbp)
	jE .Ltmp.37
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.37:
	movq $10, -144(%rbp)
	negq -144(%rbp)
	movq -144(%rbp), %r10
	cmpq %r10, -48(%rbp)
	movl $0, -148(%rbp)
	setNE -148(%rbp)
	movl -148(%rbp), %r10d
	movl %r10d, -152(%rbp)
	cmpl $0, -152(%rbp)
	jE .Ltmp.41
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.41:
	cmpl $1234, -52(%rbp)
	movl $0, -156(%rbp)
	setNE -156(%rbp)
	movl -156(%rbp), %r10d
	movl %r10d, -160(%rbp)
	cmpl $0, -160(%rbp)
	jE .Ltmp.44
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.44:
	movl $0, %eax
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
	subq $192, %rsp
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
	movl %r10d, -120(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -124(%rbp)
	movl -124(%rbp), %r10d
	movl %r10d, -128(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -132(%rbp)
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	movslq -48(%rbp), %r11
	movq %r11, -144(%rbp)
	movq -144(%rbp), %r10
	movq %r10, -152(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -156(%rbp)
	movl -156(%rbp), %r10d
	movl %r10d, -160(%rbp)
	movslq -80(%rbp), %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movl -96(%rbp), %r10d
	movl %r10d, -180(%rbp)
	movl -180(%rbp), %r10d
	movl %r10d, -184(%rbp)
	movq -112(%rbp), %rdi
	movl -120(%rbp), %esi
	movl -128(%rbp), %edx
	movl -136(%rbp), %ecx
	movq -152(%rbp), %r8
	movl -160(%rbp), %r9d
	movl -184(%rbp), %eax
	pushq %rax
	pushq -176(%rbp)
	call foo
	addq $16, %rsp
	movl %eax, -188(%rbp)
	movl -188(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
