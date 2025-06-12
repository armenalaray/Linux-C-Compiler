	.section .rodata
	.align 8
tmp.77:
	.double 0.0
	.section .rodata
	.align 8
tmp.78:
	.double 1.0
	.section .rodata
	.align 8
tmp.79:
	.double 2.0
	.section .rodata
	.align 8
tmp.80:
	.double 3.0
	.section .rodata
	.align 8
tmp.81:
	.double 4.0
	.section .rodata
	.align 8
tmp.82:
	.double 5.0
	.section .rodata
	.align 8
tmp.83:
	.double 6.0
	.section .rodata
	.align 8
tmp.84:
	.double 7.0
	.section .rodata
	.align 8
tmp.85:
	.double 8.0
	.section .rodata
	.align 8
tmp.86:
	.double 9.0
	.section .rodata
	.align 8
tmp.87:
	.double 10.0
	.globl callee
	.text
callee:
	pushq %rbp
	movq %rsp, %rbp
	subq $176, %rsp
	movsd %xmm0, -8(%rbp)
	movsd %xmm1, -16(%rbp)
	movsd %xmm2, -24(%rbp)
	movsd %xmm3, -32(%rbp)
	movsd %xmm4, -40(%rbp)
	movsd %xmm5, -48(%rbp)
	movsd %xmm6, -56(%rbp)
	movsd %xmm7, -64(%rbp)
	movsd 16(%rbp), %xmm14
	movsd %xmm14, -72(%rbp)
	movsd 24(%rbp), %xmm14
	movsd %xmm14, -80(%rbp)
	movsd 32(%rbp), %xmm14
	movsd %xmm14, -88(%rbp)
	movsd -8(%rbp), %xmm15
	comisd tmp.77(%rip), %xmm15
	movl $0, -92(%rbp)
	setNE -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -96(%rbp)
	cmpl $0, -96(%rbp)
	jE .Ltmp.18
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.18:
	movsd -16(%rbp), %xmm15
	comisd tmp.78(%rip), %xmm15
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.21
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.21:
	movsd -24(%rbp), %xmm15
	comisd tmp.79(%rip), %xmm15
	movl $0, -108(%rbp)
	setNE -108(%rbp)
	movl -108(%rbp), %r10d
	movl %r10d, -112(%rbp)
	cmpl $0, -112(%rbp)
	jE .Ltmp.24
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.24:
	movsd -32(%rbp), %xmm15
	comisd tmp.80(%rip), %xmm15
	movl $0, -116(%rbp)
	setNE -116(%rbp)
	movl -116(%rbp), %r10d
	movl %r10d, -120(%rbp)
	cmpl $0, -120(%rbp)
	jE .Ltmp.27
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.27:
	movsd -40(%rbp), %xmm15
	comisd tmp.81(%rip), %xmm15
	movl $0, -124(%rbp)
	setNE -124(%rbp)
	movl -124(%rbp), %r10d
	movl %r10d, -128(%rbp)
	cmpl $0, -128(%rbp)
	jE .Ltmp.30
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.30:
	movsd -48(%rbp), %xmm15
	comisd tmp.82(%rip), %xmm15
	movl $0, -132(%rbp)
	setNE -132(%rbp)
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.33
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.33:
	movsd -56(%rbp), %xmm15
	comisd tmp.83(%rip), %xmm15
	movl $0, -140(%rbp)
	setNE -140(%rbp)
	movl -140(%rbp), %r10d
	movl %r10d, -144(%rbp)
	cmpl $0, -144(%rbp)
	jE .Ltmp.36
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.36:
	movsd -64(%rbp), %xmm15
	comisd tmp.84(%rip), %xmm15
	movl $0, -148(%rbp)
	setNE -148(%rbp)
	movl -148(%rbp), %r10d
	movl %r10d, -152(%rbp)
	cmpl $0, -152(%rbp)
	jE .Ltmp.39
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.39:
	movsd -72(%rbp), %xmm15
	comisd tmp.85(%rip), %xmm15
	movl $0, -156(%rbp)
	setNE -156(%rbp)
	movl -156(%rbp), %r10d
	movl %r10d, -160(%rbp)
	cmpl $0, -160(%rbp)
	jE .Ltmp.42
	movl $9, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.42:
	movsd -80(%rbp), %xmm15
	comisd tmp.86(%rip), %xmm15
	movl $0, -164(%rbp)
	setNE -164(%rbp)
	movl -164(%rbp), %r10d
	movl %r10d, -168(%rbp)
	cmpl $0, -168(%rbp)
	jE .Ltmp.45
	movl $10, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.45:
	movsd -88(%rbp), %xmm15
	comisd tmp.87(%rip), %xmm15
	movl $0, -172(%rbp)
	setNE -172(%rbp)
	movl -172(%rbp), %r10d
	movl %r10d, -176(%rbp)
	cmpl $0, -176(%rbp)
	jE .Ltmp.48
	movl $11, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.48:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.88:
	.double 0.0
	.section .rodata
	.align 8
tmp.89:
	.double 1.0
	.section .rodata
	.align 8
tmp.90:
	.double 2.0
	.section .rodata
	.align 8
tmp.91:
	.double 3.0
	.section .rodata
	.align 8
tmp.92:
	.double 4.0
	.section .rodata
	.align 8
tmp.93:
	.double 5.0
	.section .rodata
	.align 8
tmp.94:
	.double 1.0
	.section .rodata
	.align 8
tmp.95:
	.double 3.0
	.section .rodata
	.align 8
tmp.96:
	.double 5.0
	.section .rodata
	.align 8
tmp.97:
	.double 7.0
	.section .rodata
	.align 8
tmp.98:
	.double 9.0
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $208, %rsp
	movl %edi, -4(%rbp)
	movl %esi, -8(%rbp)
	movl %edx, -12(%rbp)
	movl %ecx, -16(%rbp)
	movl %r8d, -20(%rbp)
	movsd tmp.88(%rip), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd tmp.89(%rip), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd tmp.90(%rip), %xmm14
	movsd %xmm14, -48(%rbp)
	movsd tmp.91(%rip), %xmm14
	movsd %xmm14, -56(%rbp)
	movsd tmp.92(%rip), %xmm14
	movsd %xmm14, -64(%rbp)
	movsd tmp.93(%rip), %xmm14
	movsd %xmm14, -72(%rbp)
	cvtsi2sdl -20(%rbp), %xmm15
	movsd %xmm15, -80(%rbp)
	movsd -80(%rbp), %xmm14
	movsd %xmm14, -88(%rbp)
	movsd -88(%rbp), %xmm15
	addsd tmp.94(%rip), %xmm15
	movsd %xmm15, -88(%rbp)
	movsd -88(%rbp), %xmm14
	movsd %xmm14, -96(%rbp)
	cvtsi2sdl -16(%rbp), %xmm15
	movsd %xmm15, -104(%rbp)
	movsd -104(%rbp), %xmm14
	movsd %xmm14, -112(%rbp)
	movsd -112(%rbp), %xmm15
	addsd tmp.95(%rip), %xmm15
	movsd %xmm15, -112(%rbp)
	movsd -112(%rbp), %xmm14
	movsd %xmm14, -120(%rbp)
	cvtsi2sdl -12(%rbp), %xmm15
	movsd %xmm15, -128(%rbp)
	movsd -128(%rbp), %xmm14
	movsd %xmm14, -136(%rbp)
	movsd -136(%rbp), %xmm15
	addsd tmp.96(%rip), %xmm15
	movsd %xmm15, -136(%rbp)
	movsd -136(%rbp), %xmm14
	movsd %xmm14, -144(%rbp)
	cvtsi2sdl -8(%rbp), %xmm15
	movsd %xmm15, -152(%rbp)
	movsd -152(%rbp), %xmm14
	movsd %xmm14, -160(%rbp)
	movsd -160(%rbp), %xmm15
	addsd tmp.97(%rip), %xmm15
	movsd %xmm15, -160(%rbp)
	movsd -160(%rbp), %xmm14
	movsd %xmm14, -168(%rbp)
	cvtsi2sdl -4(%rbp), %xmm15
	movsd %xmm15, -176(%rbp)
	movsd -176(%rbp), %xmm14
	movsd %xmm14, -184(%rbp)
	movsd -184(%rbp), %xmm15
	addsd tmp.98(%rip), %xmm15
	movsd %xmm15, -184(%rbp)
	movsd -184(%rbp), %xmm14
	movsd %xmm14, -192(%rbp)
	subq $8, %rsp
	movsd -32(%rbp), %xmm0
	movsd -40(%rbp), %xmm1
	movsd -48(%rbp), %xmm2
	movsd -56(%rbp), %xmm3
	movsd -64(%rbp), %xmm4
	movsd -72(%rbp), %xmm5
	movsd -96(%rbp), %xmm6
	movsd -120(%rbp), %xmm7
	pushq -192(%rbp)
	pushq -168(%rbp)
	pushq -144(%rbp)
	call callee
	addq $32, %rsp
	movl %eax, -196(%rbp)
	movl -196(%rbp), %eax
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
	subq $32, %rsp
	movl $1, -4(%rbp)
	movl $2, -8(%rbp)
	movl $3, -12(%rbp)
	movl $4, -16(%rbp)
	movl $5, -20(%rbp)
	movl -4(%rbp), %edi
	movl -8(%rbp), %esi
	movl -12(%rbp), %edx
	movl -16(%rbp), %ecx
	movl -20(%rbp), %r8d
	call target
	movl %eax, -24(%rbp)
	movl -24(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
