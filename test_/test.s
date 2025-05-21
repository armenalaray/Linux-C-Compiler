	.globl sign_extend
	.text
sign_extend:
	pushq %rbp
	movq %rsp, %rbp
	subl $64, 
	movl %edi, -4(%rbp)
	movq %esi, -16(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -20(%rbp)
	negl -20(%rbp)
	movslq -20(%rbp), %r11d
	movq %r11d, -32(%rbp)
	movq -32(%rbp), %r10d
	movq %r10d, -40(%rbp)
	movq -16(%rbp), %r10d
	cmpl %r10d, -40(%rbp)
	movl $0, -44(%rbp)
	setE -44(%rbp)
	movslq -44(%rbp), %r11d
	movq %r11d, -56(%rbp)
	movq -56(%rbp), %eax
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
	subl $112, 
	movl $10, -8(%rbp)
	movq $10, -16(%rbp)
	movq -8(%rbp), %edi
	movq -16(%rbp), %esi
	call sign_extend
	movq %eax, -24(%rbp)
	cmpl $0, -24(%rbp)
	movl $0, -28(%rbp)
	setE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.13
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.13:
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
	cmpl $0, -72(%rbp)
	movl $0, -76(%rbp)
	setE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.21
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.21:
	movl $100, %r10d
	movslq %r10d, %r11d
	movq %r11d, -88(%rbp)
	movq -88(%rbp), %r10d
	movq %r10d, -96(%rbp)
	cmpl $100, -96(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.25
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.25:
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
