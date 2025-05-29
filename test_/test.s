	.section .rodata
	.align 8
tmp.50:
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
	mov %xmm0, -40(%rbp)
	mov %xmm1, -48(%rbp)
	mov %xmm2, -56(%rbp)
	mov %xmm3, -64(%rbp)
	mov %xmm4, -72(%rbp)
	mov %xmm5, -80(%rbp)
	mov %xmm6, -88(%rbp)
	mov %xmm7, -96(%rbp)
	mov 16(%rbp), %xmm14
	mov %xmm14, -104(%rbp)
	mov 24(%rbp), %xmm14
	mov %xmm14, -112(%rbp)
	movl 32(%rbp), %r10d
	movl %r10d, -116(%rbp)
	mov 40(%rbp), %xmm14
	mov %xmm14, -128(%rbp)
	movl 48(%rbp), %r10d
	movl %r10d, -132(%rbp)
	movl 56(%rbp), %r10d
	movl %r10d, -136(%rbp)
	mov tmp.50(%rip), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.51:
	.double 0.1
	.section .rodata
	.align 8
tmp.52:
	.double 9.223372036854776e+18
	.section .rodata
	.align 8
tmp.55:
	.double 3.0
	.section .rodata
	.align 8
tmp.58:
	.double 2.0
	.section .rodata
	.align 8
tmp.59:
	.double 3.0
	.section .rodata
	.align 8
tmp.60:
	.double 4.0
	.section .rodata
	.align 8
tmp.61:
	.double 5.0
	.section .rodata
	.align 8
tmp.62:
	.double 6.0
	.section .rodata
	.align 8
tmp.63:
	.double 6.0
	.section .rodata
	.align 8
tmp.64:
	.double 7.0
	.section .rodata
	.align 8
tmp.65:
	.double 8.0
	.section .rodata
	.align 8
tmp.66:
	.double 9.0
	.section .rodata
	.align 8
tmp.67:
	.double 10.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $224, %rsp
	mov tmp.51(%rip), %xmm15
	cmp tmp.52(%rip), %xmm15
	jAE .Ltmp.53
	movq %r11, -8(%rbp)
	jmp .Ltmp.54
.Ltmp.53:
	mov tmp.51(%rip), %xmm1
	sub tmp.52(%rip), %xmm1
	movq %r11, -8(%rbp)
	movq $9223372036854775808, %r10
	movq %r10, %rdx
	addq %rdx, -8(%rbp)
.Ltmp.54:
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	mov tmp.55(%rip), %xmm14
	mov %xmm14, -24(%rbp)
	cmpq $0, -16(%rbp)
	jL .Ltmp.56
	cvtsi2sdq %xmm14, -24(%rbp)
	mov %xmm15, -32(%rbp)
	jmp .Ltmp.57
.Ltmp.56:
	movq -16(%rbp), %rax
	movq %rax, %rdxq %rdxq $1, %raxq %rax, %rdx
	cvtsi2sdq %rax, %rdx
	mov %xmm15, -32(%rbp)
	mov -32(%rbp), %xmm15
	add -32(%rbp), %xmm15
.Ltmp.57:
	mov -32(%rbp), %xmm14
	mov %xmm14, -40(%rbp)
	mov -40(%rbp), %xmm15
	add -24(%rbp), %xmm15
	mov -40(%rbp), %xmm14
	mov %xmm14, -48(%rbp)
	mov tmp.58(%rip), %xmm14
	mov %xmm14, -56(%rbp)
	movl $101, -60(%rbp)
	mov tmp.59(%rip), %xmm14
	mov %xmm14, -72(%rbp)
	mov tmp.60(%rip), %xmm14
	mov %xmm14, -80(%rbp)
	mov tmp.61(%rip), %xmm14
	mov %xmm14, -88(%rbp)
	mov tmp.62(%rip), %xmm14
	mov %xmm14, -96(%rbp)
	movl $104, -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	movl $202, %r10d
	movslq %r10d, %r11
	movq %r11, -112(%rbp)
	movq -112(%rbp), %r10
	movq %r10, -120(%rbp)
	mov tmp.63(%rip), %xmm14
	mov %xmm14, -128(%rbp)
	mov tmp.64(%rip), %xmm14
	mov %xmm14, -136(%rbp)
	movl $105, %r10d
	movslq %r10d, %r11
	movq %r11, -144(%rbp)
	movq -144(%rbp), %r10
	movq %r10, -152(%rbp)
	mov tmp.65(%rip), %xmm14
	mov %xmm14, -160(%rbp)
	movl $120, -164(%rbp)
	mov tmp.66(%rip), %xmm14
	mov %xmm14, -176(%rbp)
	movl $121, -180(%rbp)
	movl $122, -184(%rbp)
	mov tmp.67(%rip), %xmm14
	mov %xmm14, -192(%rbp)
	movl $123, -196(%rbp)
	movl $124, -200(%rbp)
	movl -60(%rbp), %edi
	movl -104(%rbp), %esi
	movq -120(%rbp), %rdx
	movq -152(%rbp), %rcx
	movl -164(%rbp), %r8d
	movl -180(%rbp), %r9d
	mov -48(%rbp), %xmm0
	mov -56(%rbp), %xmm1
	mov -72(%rbp), %xmm2
	mov -80(%rbp), %xmm3
	mov -88(%rbp), %xmm4
	mov -96(%rbp), %xmm5
	mov -128(%rbp), %xmm6
	mov -136(%rbp), %xmm7
	movl -200(%rbp), %eax
	pushq %rax
	movl -196(%rbp), %eax
	pushq %rax
	pushq -192(%rbp)
	movl -184(%rbp), %eax
	pushq %rax
	pushq -176(%rbp)
	pushq -160(%rbp)
	call pass_parameters_3
	addq $48, %rsp
	mov %xmm0, -208(%rbp)
	movl %r11d, -212(%rbp)
	movl -212(%rbp), %eax
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
