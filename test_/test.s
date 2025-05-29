	.section .rodata
	.align 8
tmp.49:
	.double 1.0
	.globl pass_parameters_3
	.text
pass_parameters_3:
	pushq %rbp
	movq %rsp, %rbp
	subq $144, %rsp
	movl %edi, -4(%rbp)
	movl %esi, -8(%rbp)
	movq %rdx, -16(%rbp)
	movq %rcx, -24(%rbp)
	movl %r8d, -28(%rbp)
	movl %r9d, -32(%rbp)
	movsd %xmm0, -40(%rbp)
	movsd %xmm1, -48(%rbp)
	movsd %xmm2, -56(%rbp)
	movsd %xmm3, -64(%rbp)
	movsd %xmm4, -72(%rbp)
	movsd %xmm5, -80(%rbp)
	movsd %xmm6, -88(%rbp)
	movsd %xmm7, -96(%rbp)
	movsd 16(%rbp), %xmm14
	movsd %xmm14, -104(%rbp)
	movsd 24(%rbp), %xmm14
	movsd %xmm14, -112(%rbp)
	movl 32(%rbp), %r10d
	movl %r10d, -116(%rbp)
	movsd 40(%rbp), %xmm14
	movsd %xmm14, -128(%rbp)
	movl 48(%rbp), %r10d
	movl %r10d, -132(%rbp)
	movl 56(%rbp), %r10d
	movl %r10d, -136(%rbp)
	movsd tmp.49(%rip), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.52:
	.double 3.0
	.section .rodata
	.align 8
tmp.53:
	.double 2.0
	.section .rodata
	.align 8
tmp.54:
	.double 3.0
	.section .rodata
	.align 8
tmp.55:
	.double 4.0
	.section .rodata
	.align 8
tmp.56:
	.double 5.0
	.section .rodata
	.align 8
tmp.57:
	.double 6.0
	.section .rodata
	.align 8
tmp.58:
	.double 6.0
	.section .rodata
	.align 8
tmp.59:
	.double 7.0
	.section .rodata
	.align 8
tmp.60:
	.double 8.0
	.section .rodata
	.align 8
tmp.61:
	.double 9.0
	.section .rodata
	.align 8
tmp.62:
	.double 10.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $208, %rsp
	movq $2, %r11
	cmpq $0, %r11
	jL .Ltmp.50
	movq $2, %r10
	cvtsi2sdq $2, %r10
	movsd %xmm15, -8(%rbp)
	jmp .Ltmp.51
.Ltmp.50:
	movq $2, %rax
	movq %rax, %rdxq %rdx
	andq $1, %rax
	orq %rax, %rdx
	cvtsi2sdq %rax, %rdx
	movsd %xmm15, -8(%rbp)
	movsd -8(%rbp), %xmm15
	addsd -8(%rbp), %xmm15
.Ltmp.51:
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd tmp.52(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd -16(%rbp), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd -32(%rbp), %xmm15
	divsd -24(%rbp), %xmm15
	movsd -32(%rbp), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd tmp.53(%rip), %xmm14
	movsd %xmm14, -48(%rbp)
	movl $101, -52(%rbp)
	movsd tmp.54(%rip), %xmm14
	movsd %xmm14, -64(%rbp)
	movsd tmp.55(%rip), %xmm14
	movsd %xmm14, -72(%rbp)
	movsd tmp.56(%rip), %xmm14
	movsd %xmm14, -80(%rbp)
	movsd tmp.57(%rip), %xmm14
	movsd %xmm14, -88(%rbp)
	movl $104, -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -96(%rbp)
	movl $202, %r10d
	movslq %r10d, %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %r10
	movq %r10, -112(%rbp)
	movsd tmp.58(%rip), %xmm14
	movsd %xmm14, -120(%rbp)
	movsd tmp.59(%rip), %xmm14
	movsd %xmm14, -128(%rbp)
	movl $105, %r10d
	movslq %r10d, %r11
	movq %r11, -136(%rbp)
	movq -136(%rbp), %r10
	movq %r10, -144(%rbp)
	movsd tmp.60(%rip), %xmm14
	movsd %xmm14, -152(%rbp)
	movl $120, -156(%rbp)
	movsd tmp.61(%rip), %xmm14
	movsd %xmm14, -168(%rbp)
	movl $121, -172(%rbp)
	movl $122, -176(%rbp)
	movsd tmp.62(%rip), %xmm14
	movsd %xmm14, -184(%rbp)
	movl $123, -188(%rbp)
	movl $124, -192(%rbp)
	movl -52(%rbp), %edi
	movl -96(%rbp), %esi
	movq -112(%rbp), %rdx
	movq -144(%rbp), %rcx
	movl -156(%rbp), %r8d
	movl -172(%rbp), %r9d
	movsd -40(%rbp), %xmm0
	movsd -48(%rbp), %xmm1
	movsd -64(%rbp), %xmm2
	movsd -72(%rbp), %xmm3
	movsd -80(%rbp), %xmm4
	movsd -88(%rbp), %xmm5
	movsd -120(%rbp), %xmm6
	movsd -128(%rbp), %xmm7
	movl -192(%rbp), %eax
	pushq %rax
	movl -188(%rbp), %eax
	pushq %rax
	pushq -184(%rbp)
	movl -176(%rbp), %eax
	pushq %rax
	pushq -168(%rbp)
	pushq -152(%rbp)
	call pass_parameters_3
	addq $48, %rsp
	movsd %xmm0, -200(%rbp)
	cvttsd2sil %xmm0, -200(%rbp)
	movl %r11d, -204(%rbp)
	movl -204(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.data
	.align 8
ale:
	.double 0.0
	.section	.note.GNU-stack,"",@progbits
