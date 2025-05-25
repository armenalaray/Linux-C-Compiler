	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq $9223372036854775803, %r10
	cmpq %r10, x(%rip)
	movl $0, -4(%rbp)
	setNE -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	cmpl $0, -8(%rbp)
	jE .Ltmp.2
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.2:
	movl $10, %r10d
	movslq %r10d, %r11
	movq %r11, -16(%rbp)
	movq x(%rip), %r10
	movq %r10, -24(%rbp)
	movq -16(%rbp), %r10
	addq %r10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, x(%rip)
	movq $9223372036854775813, %r10
	cmpq %r10, x(%rip)
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.7
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.7:
	cmpq $0, zero_long(%rip)
	jNE .Ltmp.8
	cmpl $0, zero_int(%rip)
	jNE .Ltmp.8
	movl $0, -36(%rbp)
	jmp .Ltmp.10
.Ltmp.8:
	movl $1, -36(%rbp)
.Ltmp.10:
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Ltmp.12
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.12:
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.data
	.align 8
x:
	.quad 9223372036854775803
	.globl zero_long
	.data
	.align 8
zero_long:
	.quad 0
	.globl zero_int
	.data
	.align 4
zero_int:
	.long 0
	.section	.note.GNU-stack,"",@progbits
