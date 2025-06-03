	.globl int_to_pointer
	.text
int_to_pointer:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movslq i(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq l(%rip), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -32(%rbp), %r10
	cmpq %r10, -16(%rbp)
	movl $0, -36(%rbp)
	setE -36(%rbp)
	movl -36(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl pointer_to_int
	.text
pointer_to_int:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	leaq l.2(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movl $8, %r10d
	movslq %r10d, %r11
	movq %r11, -40(%rbp)
	movq -32(%rbp), %rax
	movq $0, %rdx
	divq -40(%rbp)
	movq %rdx, -48(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	cmpq %r10, -48(%rbp)
	movl $0, -60(%rbp)
	setE -60(%rbp)
	movl -60(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl cast_long_round_trip
	.text
cast_long_round_trip:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq l(%rip), %r10
	movq %r10, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -32(%rbp), %r10
	cmpq %r10, l(%rip)
	movl $0, -36(%rbp)
	setE -36(%rbp)
	movl -36(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl cast_ulong_round_trip
	.text
cast_ulong_round_trip:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	leaq l(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -48(%rbp), %r10
	cmpq %r10, -16(%rbp)
	movl $0, -52(%rbp)
	setE -52(%rbp)
	movl -52(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl cast_int_round_trip
	.text
cast_int_round_trip:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movslq i(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movl -16(%rbp), %r10d
	movl %r10d, -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $128, -24(%rbp)
	movl $0, -28(%rbp)
	setE -28(%rbp)
	movl -28(%rbp), %eax
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
	subq $64, %rsp
	call int_to_pointer
	movl %eax, -4(%rbp)
	cmpl $0, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.34
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.34:
	call pointer_to_int
	movl %eax, -16(%rbp)
	cmpl $0, -16(%rbp)
	movl $0, -20(%rbp)
	setE -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Ltmp.38
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.38:
	call cast_long_round_trip
	movl %eax, -28(%rbp)
	cmpl $0, -28(%rbp)
	movl $0, -32(%rbp)
	setE -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.42
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.42:
	call cast_ulong_round_trip
	movl %eax, -40(%rbp)
	cmpl $0, -40(%rbp)
	movl $0, -44(%rbp)
	setE -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.46
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.46:
	call cast_int_round_trip
	movl %eax, -52(%rbp)
	cmpl $0, -52(%rbp)
	movl $0, -56(%rbp)
	setE -56(%rbp)
	movl -56(%rbp), %r10d
	movl %r10d, -60(%rbp)
	cmpl $0, -60(%rbp)
	jE .Ltmp.50
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.50:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl i
	.data
	.align 4
i:
	.long 128
	.globl l
	.data
	.align 8
l:
	.quad 128
	.data
	.align 8
l.2:
	.quad 0
	.section	.note.GNU-stack,"",@progbits
