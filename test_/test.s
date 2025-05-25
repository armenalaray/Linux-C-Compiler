	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movl $2147483660, %r10d
	cmpl %r10d, u(%rip)
	movl $0, -4(%rbp)
	setNE -4(%rbp)
	movl -4(%rbp), %r10d
	movl %r10d, -8(%rbp)
	cmpl $0, -8(%rbp)
	jE .Ltmp.2
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.2:
	movl $2147483646, -12(%rbp)
	negl -12(%rbp)
	movl -12(%rbp), %r10d
	cmpl %r10d, i(%rip)
	movl $0, -16(%rbp)
	setNE -16(%rbp)
	movl -16(%rbp), %r10d
	movl %r10d, -20(%rbp)
	cmpl $0, -20(%rbp)
	jE .Ltmp.6
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.6:
	movq $9223372036854775716, %r10
	movq %r10, -32(%rbp)
	negq -32(%rbp)
	movq -32(%rbp), %r10
	cmpq %r10, l(%rip)
	movl $0, -36(%rbp)
	setNE -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Ltmp.10
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.10:
	movq $2147483650, %r10
	cmpq %r10, l2(%rip)
	movl $0, -44(%rbp)
	setNE -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.13
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.13:
	movq $4294967294, %r10
	cmpq %r10, ul(%rip)
	movl $0, -52(%rbp)
	setNE -52(%rbp)
	movl -52(%rbp), %r10d
	movl %r10d, -56(%rbp)
	cmpl $0, -56(%rbp)
	jE .Ltmp.16
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.16:
	movq $9223372036854775798, %r10
	cmpq %r10, ul2(%rip)
	movl $0, -60(%rbp)
	setNE -60(%rbp)
	movl -60(%rbp), %r10d
	movl %r10d, -64(%rbp)
	cmpl $0, -64(%rbp)
	jE .Ltmp.19
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.19:
	movl $2147483498, -68(%rbp)
	negl -68(%rbp)
	movl -68(%rbp), %r10d
	cmpl %r10d, i2(%rip)
	movl $0, -72(%rbp)
	setNE -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	cmpl $0, -76(%rbp)
	jE .Ltmp.23
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.23:
	movl $2147483798, %r10d
	cmpl %r10d, ui2(%rip)
	movl $0, -80(%rbp)
	setNE -80(%rbp)
	movl -80(%rbp), %r10d
	movl %r10d, -84(%rbp)
	cmpl $0, -84(%rbp)
	jE .Ltmp.26
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.26:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl u
	.data
	.align 4
u:
	.long 2147483660
	.globl i
	.data
	.align 4
i:
	.long -2147483646
	.globl l
	.data
	.align 8
l:
	.quad -9223372036854775716
	.globl l2
	.data
	.align 8
l2:
	.quad 2147483650
	.globl ul
	.data
	.align 8
ul:
	.quad 4294967294
	.globl ul2
	.data
	.align 8
ul2:
	.quad 9223372036854775798
	.globl i2
	.data
	.align 4
i2:
	.long -2147483498
	.globl ui2
	.data
	.align 4
ui2:
	.long 2147483798
	.section	.note.GNU-stack,"",@progbits
