	.globl check_pointers
	.text
check_pointers:
	pushq %rbp
	movq %rsp, %rbp
	subq $80, %rsp
	movl %edi, -4(%rbp)
	movl %esi, -8(%rbp)
	movq %rdx, -16(%rbp)
	movq %rcx, -24(%rbp)
	cmpl $100, -4(%rbp)
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	cmpl $0, -28(%rbp)
	jNE .Ltmp.12
	cmpl $101, -8(%rbp)
	movl $0, -32(%rbp)
	setNE -32(%rbp)
	cmpl $0, -32(%rbp)
	jNE .Ltmp.12
	movl $0, -36(%rbp)
	jmp .Ltmp.15
.Ltmp.12:
	movl $1, -36(%rbp)
.Ltmp.15:
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.17
	movl $1, -44(%rbp)
	movl $1, %edi
	call exit
.Ltmp.17:
	movq -16(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -48(%rbp)
	cmpl $60, -48(%rbp)
	movl $0, -52(%rbp)
	setNE -52(%rbp)
	cmpl $0, -52(%rbp)
	jNE .Ltmp.21
	movq -24(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -56(%rbp)
	cmpl $61, -56(%rbp)
	movl $0, -60(%rbp)
	setNE -60(%rbp)
	cmpl $0, -60(%rbp)
	jNE .Ltmp.21
	movl $0, -64(%rbp)
	jmp .Ltmp.25
.Ltmp.21:
	movl $1, -64(%rbp)
.Ltmp.25:
	movl -64(%rbp), %r10d
	movl %r10d, -68(%rbp)
	cmpl $0, -64(%rbp)
	jE .Ltmp.27
	movl $2, -72(%rbp)
	movl $2, %edi
	call exit
.Ltmp.27:
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl callee
	.text
callee:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq %rdi, -8(%rbp)
	movq %rsi, -16(%rbp)
	movq -16(%rbp), %r10
	cmpq %r10, -8(%rbp)
	movl $0, -20(%rbp)
	setNE -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -20(%rbp)
	jE .Ltmp.31
	movl $3, -28(%rbp)
	movl $3, %edi
	call exit
.Ltmp.31:
	movq -16(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -32(%rbp)
	cmpl $10, -32(%rbp)
	movl $0, -36(%rbp)
	setNE -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.36
	movl $4, -44(%rbp)
	movl $4, %edi
	call exit
.Ltmp.36:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movq %rdi, -8(%rbp)
	movq %rsi, -16(%rbp)
	movl $100, -20(%rbp)
	movl $101, -24(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -40(%rbp)
	movl $100, %edi
	movl $101, %esi
	movq -8(%rbp), %rdx
	movq -16(%rbp), %rcx
	call check_pointers
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -8(%rbp), %rax
	movl $10, 0(%rax)
	movq -8(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -56(%rbp)
	movq -8(%rbp), %rdi
	movq -8(%rbp), %rsi
	call callee
	movl %eax, -60(%rbp)
	movl -60(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl $60, -4(%rbp)
	movl $61, -8(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	leaq -8(%rbp), %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movq -16(%rbp), %rdi
	movq -32(%rbp), %rsi
	call target
	movl %eax, -44(%rbp)
	movl -44(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
