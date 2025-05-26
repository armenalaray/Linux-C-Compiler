	.globl addition
	.text
addition:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl ui_a(%rip), %r10d
	movl %r10d, -4(%rbp)
	movl $2147483653, %r10d
	addl %r10d, -4(%rbp)
	movl $2147483663, %r10d
	cmpl %r10d, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl subtraction
	.text
subtraction:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq ul_a(%rip), %r10
	movq %r10, -8(%rbp)
	movq ul_b(%rip), %r10
	subq %r10, -8(%rbp)
	movq $18446744072635808792, %r10
	cmpq %r10, -8(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl multiplication
	.text
multiplication:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl ui_a(%rip), %r10d
	movl %r10d, -4(%rbp)
	movl -4(%rbp), %r11d
	imull ui_b(%rip), %r11d
	movl %r11d, -4(%rbp)
	movl $3221225472, %r10d
	cmpl %r10d, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl division
	.text
division:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl ui_a(%rip), %eax
	movl $0, %edx
	divl ui_b(%rip)
	movl %eax, -4(%rbp)
	movl $0, -8(%rbp)
	movl -8(%rbp), %r10d
	cmpl %r10d, -4(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl division_large_dividend
	.text
division_large_dividend:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl ui_a(%rip), %eax
	movl $0, %edx
	divl ui_b(%rip)
	movl %eax, -4(%rbp)
	movl $2, -8(%rbp)
	movl -8(%rbp), %r10d
	cmpl %r10d, -4(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl division_by_literal
	.text
division_by_literal:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq ul_a(%rip), %rax
	movq $0, %rdx
	movq $5, %r10
	divq %r10
	movq %rax, -8(%rbp)
	movq $219902325555, %r10
	cmpq %r10, -8(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl remaind
	.text
remaind:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq ul_b(%rip), %rax
	movq $0, %rdx
	divq ul_a(%rip)
	movq %rdx, -8(%rbp)
	cmpq $5, -8(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl complement
	.text
complement:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl ui_a(%rip), %r10d
	movl %r10d, -4(%rbp)
	notl -4(%rbp)
	movl $0, -8(%rbp)
	movl -8(%rbp), %r10d
	cmpl %r10d, -4(%rbp)
	movl $0, -12(%rbp)
	setE -12(%rbp)
	movl -12(%rbp), %eax
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
	subq $96, %rsp
	movl $10, ui_a(%rip)
	call addition
	movl %eax, -4(%rbp)
	cmpl $0, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.22
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.22:
	movq $18446744072635809792, %r10
	movq %r10, ul_a(%rip)
	movq $1000, ul_b(%rip)
	call subtraction
	movl %eax, -16(%rbp)
	cmpl $0, -16(%rbp)
	movl $0, -20(%rbp)
	setE -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Ltmp.26
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.26:
	movl $1073741824, ui_a(%rip)
	movl $3, ui_b(%rip)
	call multiplication
	movl %eax, -28(%rbp)
	cmpl $0, -28(%rbp)
	movl $0, -32(%rbp)
	setE -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.30
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.30:
	movl $100, ui_a(%rip)
	movl $4294967294, %r10d
	movl %r10d, ui_b(%rip)
	call division
	movl %eax, -40(%rbp)
	cmpl $0, -40(%rbp)
	movl $0, -44(%rbp)
	setE -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.34
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.34:
	movl $4294967294, %r10d
	movl %r10d, ui_a(%rip)
	movl $2147483647, ui_b(%rip)
	call division_large_dividend
	movl %eax, -52(%rbp)
	cmpl $0, -52(%rbp)
	movl $0, -56(%rbp)
	setE -56(%rbp)
	movl -56(%rbp), %r10d
	movl %r10d, -60(%rbp)
	cmpl $0, -60(%rbp)
	jE .Ltmp.38
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.38:
	movq $1099511627775, %r10
	movq %r10, ul_a(%rip)
	call division_by_literal
	movl %eax, -64(%rbp)
	cmpl $0, -64(%rbp)
	movl $0, -68(%rbp)
	setE -68(%rbp)
	movl -68(%rbp), %r10d
	movl %r10d, -72(%rbp)
	cmpl $0, -72(%rbp)
	jE .Ltmp.42
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.42:
	movq $100, ul_a(%rip)
	movq $18446744073709551605, %r10
	movq %r10, ul_b(%rip)
	call remaind
	movl %eax, -76(%rbp)
	cmpl $0, -76(%rbp)
	movl $0, -80(%rbp)
	setE -80(%rbp)
	movl -80(%rbp), %r10d
	movl %r10d, -84(%rbp)
	cmpl $0, -84(%rbp)
	jE .Ltmp.46
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.46:
	movl $4294967295, %r10d
	movl %r10d, ui_a(%rip)
	call complement
	movl %eax, -88(%rbp)
	cmpl $0, -88(%rbp)
	movl $0, -92(%rbp)
	setE -92(%rbp)
	movl -92(%rbp), %r10d
	movl %r10d, -96(%rbp)
	cmpl $0, -96(%rbp)
	jE .Ltmp.50
	movl $8, %eax
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
	.globl ui_a
	.data
	.align 4
ui_a:
	.long 0
	.globl ui_b
	.data
	.align 4
ui_b:
	.long 0
	.globl ul_a
	.data
	.align 8
ul_a:
	.quad 0
	.globl ul_b
	.data
	.align 8
ul_b:
	.quad 0
	.section	.note.GNU-stack,"",@progbits
