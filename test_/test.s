	.globl sign_extend
	.text
sign_extend:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl %edi, -4(%rbp)
	movq %esi, -16(%rbp)
	movslq -4(%rbp), %r11d
	movq %r11d, -24(%rbp)
	movq -16(%rbp), %r10d
	cmpq %r10d, -24(%rbp)
	movl $0, -28(%rbp)
	setG -28(%rbp)
	movslq -28(%rbp), %r11d
	movq %r11d, -40(%rbp)
	movq -40(%rbp), %r10d
	movq %r10d, -48(%rbp)
	movq -16(%rbp), %r10d
	cmpq %r10d, -48(%rbp)
	movl $0, -52(%rbp)
	setE -52(%rbp)
	movslq -52(%rbp), %r11d
	movq %r11d, -64(%rbp)
	movq -64(%rbp), %eax
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
	subq $112, %rsp
	movl $10, -8(%rbp)
	movq $10, -16(%rbp)
	movq -8(%rbp), %edi
	movq -16(%rbp), %esi
	call sign_extend
	movq %eax, -24(%rbp)
	cmpq $0, -24(%rbp)
	movl $0, -28(%rbp)
	setE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.14
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.14:
	movl $10, -36(%rbp)
	negl -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movq $10, -56(%rbp)
	negq -56(%rbp)
	movq -56(%rbp), %r10d
	movq %r10d, -64(%rbp)
	movq -48(%rbp), %edi
	movq -64(%rbp), %esi
	call sign_extend
	movq %eax, -72(%rbp)
	cmpq $0, -72(%rbp)
	movl $0, -76(%rbp)
	setE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.22
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.22:
	movl $100, %r10d
	movslq %r10d, %r11d
	movq %r11d, -88(%rbp)
	movq -88(%rbp), %r10d
	movq %r10d, -96(%rbp)
	cmpq $100, -96(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.26
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.26:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl a
	.data
	.align 4
a:
	.long 3
	.section	.note.GNU-stack,"",@progbits
