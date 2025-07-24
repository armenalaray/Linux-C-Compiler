	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl $0, -4(%rbp)
.Ltmp.5:
	call get_input
	movl %eax, -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.7
	movl $0, %r11d
	cmpl $0, %r11d
	jE .Ltmp.7
	movl $1, -16(%rbp)
	jmp .Ltmp.9
.Ltmp.7:
	movl $0, -16(%rbp)
.Ltmp.9:
	movl -16(%rbp), %r10d
	movl %r10d, -20(%rbp)
	cmpl $0, -20(%rbp)
	jE .Ltmp.11
	movl $1, -24(%rbp)
	negl -24(%rbp)
	movl -24(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.11:
	movl -12(%rbp), %r10d
	movl %r10d, -28(%rbp)
	movl -28(%rbp), %edi
	call process_input
	movl %eax, -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
.Lcontinue_tmp.4:
	movl -4(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -40(%rbp)
	jNE .Ltmp.5
.Lbreak_tmp.4:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
