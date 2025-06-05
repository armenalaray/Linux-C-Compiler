	.globl modify_ptr
	.text
modify_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	cmpq $0, -16(%rbp)
	jE .Ltmp.6
	movq -8(%rbp), %r10
	movq %r10, p.1(%rip)
.Ltmp.6:
	movq p.1(%rip), %rax
	movq 0(%rax), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.47:
	.double 5.0
	.globl increment_ptr
	.text
increment_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq dbl_ptr(%rip), %rax
	movsd 0(%rax), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd -8(%rbp), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd -16(%rbp), %xmm15
	addsd tmp.47(%rip), %xmm15
	movsd %xmm15, -16(%rbp)
	movq dbl_ptr(%rip), %rax
	movsd -16(%rbp), %xmm14
	movsd %xmm14, 0(%rax)
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
tmp.48:
	.double 10.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $208, %rsp
	leaq x(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movl $20, x(%rip)
	movq -16(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -20(%rbp)
	cmpl $20, -20(%rbp)
	movl $0, -24(%rbp)
	setNE -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	cmpl $0, -28(%rbp)
	jE .Ltmp.14
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.14:
	movq -16(%rbp), %rax
	movl $100, 0(%rax)
	cmpl $100, x(%rip)
	movl $0, -32(%rbp)
	setNE -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.17
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.17:
	movl $4294967295, %r10d
	cmpl %r10d, w(%rip)
	movl $0, -40(%rbp)
	setNE -40(%rbp)
	movl -40(%rbp), %r10d
	movl %r10d, -44(%rbp)
	cmpl $0, -44(%rbp)
	jE .Ltmp.20
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.20:
	movl $4294967295, %r10d
	cmpl %r10d, y(%rip)
	movl $0, -48(%rbp)
	setNE -48(%rbp)
	movl -48(%rbp), %r10d
	movl %r10d, -52(%rbp)
	cmpl $0, -52(%rbp)
	jE .Ltmp.23
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.23:
	movq dbl_ptr(%rip), %r10
	movq %r10, -64(%rbp)
	cmpq $0, -64(%rbp)
	jE .Ltmp.25
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.25:
	movq $1000, -72(%rbp)
	leaq -72(%rbp), %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -88(%rbp), %rdi
	call modify_ptr
	movq %rax, -96(%rbp)
	cmpq $1000, -96(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.31
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.31:
	movl $1, -108(%rbp)
	negl -108(%rbp)
	movslq -108(%rbp), %r11
	movq %r11, -120(%rbp)
	movq -120(%rbp), %r10
	movq %r10, -72(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -128(%rbp)
	movq -128(%rbp), %r10
	movq %r10, -136(%rbp)
	movq -136(%rbp), %rdi
	call modify_ptr
	movq %rax, -144(%rbp)
	movq -72(%rbp), %r10
	cmpq %r10, -144(%rbp)
	movl $0, -148(%rbp)
	setNE -148(%rbp)
	movl -148(%rbp), %r10d
	movl %r10d, -152(%rbp)
	cmpl $0, -152(%rbp)
	jE .Ltmp.39
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.39:
	movsd tmp.48(%rip), %xmm14
	movsd %xmm14, -160(%rbp)
	leaq -160(%rbp), %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, dbl_ptr(%rip)
	call increment_ptr
	movl %eax, -172(%rbp)
	movq dbl_ptr(%rip), %rax
	movsd 0(%rax), %xmm14
	movsd %xmm14, -184(%rbp)
	movl $15, %r10d
	cvtsi2sdl %r10d, %xmm15
	movsd %xmm15, -192(%rbp)
	movsd -184(%rbp), %xmm15
	comisd -192(%rbp), %xmm15
	movl $0, -196(%rbp)
	setNE -196(%rbp)
	movl -196(%rbp), %r10d
	movl %r10d, -200(%rbp)
	cmpl $0, -200(%rbp)
	jE .Ltmp.46
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.46:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl w
	.data
	.align 4
w:
	.long 4294967295
	.globl x
	.data
	.align 4
x:
	.long 10
	.globl y
	.data
	.align 4
y:
	.long 4294967295
	.globl dbl_ptr
	.data
	.align 8
dbl_ptr:
	.quad 0
	.data
	.align 8
p.1:
	.quad 0
	.section	.note.GNU-stack,"",@progbits
