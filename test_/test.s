	.globl get_null_pointer
	.text
get_null_pointer:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.55:
	.double 5.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $192, %rsp
	leaq -8(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	call get_null_pointer
	movq %rax, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	xorpd %xmm0, %xmm0
	comisd tmp.55(%rip), %xmm0
	jE .Ltmp.11
	cmpq $0, -40(%rbp)
	jE .Ltmp.11
	movl $1, -44(%rbp)
	jmp .Ltmp.13
.Ltmp.11:
	movl $0, -44(%rbp)
.Ltmp.13:
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.15
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.15:
	movl $0, -52(%rbp)
	cmpq $0, -24(%rbp)
	jNE .Ltmp.16
	movl $10, -52(%rbp)
	cmpl $0, -52(%rbp)
	jNE .Ltmp.16
	movl $0, -56(%rbp)
	jmp .Ltmp.18
.Ltmp.16:
	movl $1, -56(%rbp)
.Ltmp.18:
	cmpl $0, -56(%rbp)
	movl $0, -60(%rbp)
	setE -60(%rbp)
	movl -60(%rbp), %r10d
	movl %r10d, -64(%rbp)
	cmpl $0, -64(%rbp)
	jE .Ltmp.21
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.21:
	cmpl $0, -52(%rbp)
	movl $0, -68(%rbp)
	setNE -68(%rbp)
	movl -68(%rbp), %r10d
	movl %r10d, -72(%rbp)
	cmpl $0, -72(%rbp)
	jE .Ltmp.24
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.24:
	cmpq $0, -24(%rbp)
	movl $0, -76(%rbp)
	setE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.27
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.27:
	movq -24(%rbp), %r10
	movq %r10, -88(%rbp)
	cmpq $0, -88(%rbp)
	jE .Ltmp.29
	movl $1, -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -96(%rbp)
	jmp .Ltmp.32
.Ltmp.29:
	movl $2, -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -96(%rbp)
.Ltmp.32:
	movl -96(%rbp), %r10d
	movl %r10d, -104(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -112(%rbp)
	cmpq $0, -112(%rbp)
	jE .Ltmp.35
	movl $3, -116(%rbp)
	movl -116(%rbp), %r10d
	movl %r10d, -120(%rbp)
	jmp .Ltmp.38
.Ltmp.35:
	movl $4, -124(%rbp)
	movl -124(%rbp), %r10d
	movl %r10d, -120(%rbp)
.Ltmp.38:
	movl -120(%rbp), %r10d
	movl %r10d, -128(%rbp)
	cmpl $1, -104(%rbp)
	movl $0, -132(%rbp)
	setNE -132(%rbp)
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.42
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.42:
	cmpl $4, -128(%rbp)
	movl $0, -140(%rbp)
	setNE -140(%rbp)
	movl -140(%rbp), %r10d
	movl %r10d, -144(%rbp)
	cmpl $0, -144(%rbp)
	jE .Ltmp.45
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.45:
	movl $0, -148(%rbp)
.Lcontinue_tmp.7:
	movq -24(%rbp), %r10
	movq %r10, -160(%rbp)
	cmpq $0, -160(%rbp)
	jE .Lbreak_tmp.7
	cmpl $10, -148(%rbp)
	movl $0, -164(%rbp)
	setGE -164(%rbp)
	movl -164(%rbp), %r10d
	movl %r10d, -168(%rbp)
	cmpl $0, -168(%rbp)
	jE .Ltmp.49
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -176(%rbp)
	movq -176(%rbp), %r10
	movq %r10, -24(%rbp)
	jmp .Lcontinue_tmp.7
.Ltmp.49:
	movl -148(%rbp), %r10d
	movl %r10d, -180(%rbp)
	addl $1, -180(%rbp)
	movl -180(%rbp), %r10d
	movl %r10d, -148(%rbp)
	jmp .Lcontinue_tmp.7
.Lbreak_tmp.7:
	cmpl $10, -148(%rbp)
	movl $0, -184(%rbp)
	setNE -184(%rbp)
	movl -184(%rbp), %r10d
	movl %r10d, -188(%rbp)
	cmpl $0, -188(%rbp)
	jE .Ltmp.54
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.54:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
