	.section .rodata
	.align 8
tmp.20:
	.double 5.0
	.section .rodata
	.align 8
tmp.21:
	.double 1e+22
	.section .rodata
	.align 8
tmp.22:
	.double 4000000.0
	.section .rodata
	.align 8
tmp.23:
	.double 9.2e+74
	.section .rodata
	.align 8
tmp.24:
	.double 5.0000000000000004e+22
	.section .rodata
	.align 8
tmp.25:
	.double 2.944e+76
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movsd tmp.20(%rip), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd tmp.21(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd tmp.22(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd -8(%rbp), %xmm0
	movsd -16(%rbp), %xmm1
	movsd -24(%rbp), %xmm2
	call fma
	movsd %xmm0, -32(%rbp)
	movsd -32(%rbp), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd tmp.23(%rip), %xmm14
	movsd %xmm14, -48(%rbp)
	movl $5, -52(%rbp)
	movl -52(%rbp), %edi
	movsd -48(%rbp), %xmm0
	call ldexp
	movsd %xmm0, -64(%rbp)
	movsd -64(%rbp), %xmm14
	movsd %xmm14, -72(%rbp)
	movsd -40(%rbp), %xmm15
	comisd tmp.24(%rip), %xmm15
	movl $0, -76(%rbp)
	setNE -76(%rbp)
	movl -76(%rbp), %r10d
	movl %r10d, -80(%rbp)
	cmpl $0, -80(%rbp)
	jE .Ltmp.16
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.16:
	movsd -72(%rbp), %xmm15
	comisd tmp.25(%rip), %xmm15
	movl $0, -84(%rbp)
	setNE -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -88(%rbp)
	cmpl $0, -88(%rbp)
	jE .Ltmp.19
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.19:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
