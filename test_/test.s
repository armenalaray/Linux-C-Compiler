	.globl sign_extend
	.text
sign_extend:
	pushq %rbp
	movq %rsp, %rbp
	subl $48, 
	movl %edi, -4(%rbp)
	movl %esi, -16(%rbp)
	movl %r11d, -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -32(%rbp)
	movl -16(%rbp), %r10d
	cmpl %r10d, -32(%rbp)
	movl $0, -36(%rbp)
	setE -36(%rbp)
	movl %r11d, -48(%rbp)
	movl -48(%rbp), %eax
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
	movl $10, -16(%rbp)
	movl -8(%rbp), %edi
	movl -16(%rbp), %esi
	call sign_extend
	movl %eax, -24(%rbp)
	cmpl $0, -24(%rbp)
	movl $0, -28(%rbp)
	setE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.12
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.12:
	movl $10, -36(%rbp)
	negl -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movl $10, -56(%rbp)
	negl -56(%rbp)
	movl -56(%rbp), %r10d
	movl %r10d, -64(%rbp)
	movl -48(%rbp), %edi
	movl -64(%rbp), %esi
	call sign_extend
	movl %eax, -72(%rbp)
	cmpl $0, -72(%rbp)
	movl $0, -76(%rbp)
	setE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.20
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.20:
	movl $100, %r10d
	movl %r11d, -88(%rbp)
	movl -88(%rbp), %r10d
	movl %r10d, -96(%rbp)
	cmpl $100, -96(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.24
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.24:
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
