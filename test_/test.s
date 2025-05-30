	.section .rodata
	.align 8
tmp.44:
	.double 1.0
	.section .rodata
	.align 8
tmp.45:
	.double 1.0
	.section .rodata
	.align 8
tmp.46:
	.double 1.0
	.section .rodata
	.align 8
tmp.47:
	.double 1.0
	.section .rodata
	.align 8
tmp.48:
	.double 4.0
	.section .rodata
	.align 8
tmp.49:
	.double 0.125
	.section .rodata
	.align 8
tmp.50:
	.double 0.125
	.section .rodata
	.align 8
tmp.51:
	.double 0.125
	.section .rodata
	.align 8
tmp.52:
	.double 0.125
	.section .rodata
	.align 8
tmp.53:
	.double 0.5
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $192, %rsp
	movsd tmp.44(%rip), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd tmp.45(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd tmp.46(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd tmp.47(%rip), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd -8(%rbp), %xmm15
	comisd -16(%rbp), %xmm15
	movl $0, -36(%rbp)
	setE -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.9
	movsd -8(%rbp), %xmm15
	comisd -24(%rbp), %xmm15
	movl $0, -40(%rbp)
	setE -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Ltmp.9
	movl $1, -44(%rbp)
	jmp .Ltmp.12
.Ltmp.9:
	movl $0, -44(%rbp)
.Ltmp.12:
	cmpl $0, -44(%rbp)
	jE .Ltmp.13
	movsd -8(%rbp), %xmm15
	comisd -32(%rbp), %xmm15
	movl $0, -48(%rbp)
	setE -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.13
	movl $1, -52(%rbp)
	jmp .Ltmp.16
.Ltmp.13:
	movl $0, -52(%rbp)
.Ltmp.16:
	cmpl $0, -52(%rbp)
	movl $0, -56(%rbp)
	setE -56(%rbp)
	movl -56(%rbp), %r10d
	movl %r10d, -60(%rbp)
	cmpl $0, -60(%rbp)
	jE .Ltmp.19
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.19:
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -72(%rbp)
	movsd -72(%rbp), %xmm15
	addsd -16(%rbp), %xmm15
	movsd %xmm15, -72(%rbp)
	movsd -72(%rbp), %xmm14
	movsd %xmm14, -80(%rbp)
	movsd -80(%rbp), %xmm15
	addsd -24(%rbp), %xmm15
	movsd %xmm15, -80(%rbp)
	movsd -80(%rbp), %xmm14
	movsd %xmm14, -88(%rbp)
	movsd -88(%rbp), %xmm15
	addsd -32(%rbp), %xmm15
	movsd %xmm15, -88(%rbp)
	movsd -88(%rbp), %xmm15
	comisd tmp.48(%rip), %xmm15
	movl $0, -92(%rbp)
	setNE -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -96(%rbp)
	cmpl $0, -96(%rbp)
	jE .Ltmp.25
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.25:
	movsd tmp.49(%rip), %xmm14
	movsd %xmm14, -104(%rbp)
	movsd tmp.50(%rip), %xmm14
	movsd %xmm14, -112(%rbp)
	movsd tmp.51(%rip), %xmm14
	movsd %xmm14, -120(%rbp)
	movsd tmp.52(%rip), %xmm14
	movsd %xmm14, -128(%rbp)
	movsd -104(%rbp), %xmm15
	comisd -112(%rbp), %xmm15
	movl $0, -132(%rbp)
	setE -132(%rbp)
	cmpl $0, -132(%rbp)
	jE .Ltmp.27
	movsd -104(%rbp), %xmm15
	comisd -120(%rbp), %xmm15
	movl $0, -136(%rbp)
	setE -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.27
	movl $1, -140(%rbp)
	jmp .Ltmp.30
.Ltmp.27:
	movl $0, -140(%rbp)
.Ltmp.30:
	cmpl $0, -140(%rbp)
	jE .Ltmp.31
	movsd -104(%rbp), %xmm15
	comisd -128(%rbp), %xmm15
	movl $0, -144(%rbp)
	setE -144(%rbp)
	cmpl $0, -144(%rbp)
	jE .Ltmp.31
	movl $1, -148(%rbp)
	jmp .Ltmp.34
.Ltmp.31:
	movl $0, -148(%rbp)
.Ltmp.34:
	cmpl $0, -148(%rbp)
	movl $0, -152(%rbp)
	setE -152(%rbp)
	movl -152(%rbp), %r10d
	movl %r10d, -156(%rbp)
	cmpl $0, -156(%rbp)
	jE .Ltmp.37
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.37:
	movsd -104(%rbp), %xmm14
	movsd %xmm14, -168(%rbp)
	movsd -168(%rbp), %xmm15
	addsd -112(%rbp), %xmm15
	movsd %xmm15, -168(%rbp)
	movsd -168(%rbp), %xmm14
	movsd %xmm14, -176(%rbp)
	movsd -176(%rbp), %xmm15
	addsd -120(%rbp), %xmm15
	movsd %xmm15, -176(%rbp)
	movsd -176(%rbp), %xmm14
	movsd %xmm14, -184(%rbp)
	movsd -184(%rbp), %xmm15
	addsd -128(%rbp), %xmm15
	movsd %xmm15, -184(%rbp)
	movsd -184(%rbp), %xmm15
	comisd tmp.53(%rip), %xmm15
	movl $0, -188(%rbp)
	setNE -188(%rbp)
	movl -188(%rbp), %r10d
	movl %r10d, -192(%rbp)
	cmpl $0, -192(%rbp)
	jE .Ltmp.43
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.43:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
