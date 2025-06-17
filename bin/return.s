	.globl test_static_nested
	.text
test_static_nested:
	pushq %rbp
	movq %rsp, %rbp
	subq $176, %rsp
	movl $0, -4(%rbp)
.Ltmp.6:
	cmpl $3, -4(%rbp)
	movl $0, -8(%rbp)
	setL -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Lbreak_tmp.4
	movl $0, -16(%rbp)
.Ltmp.9:
	cmpl $4, -16(%rbp)
	movl $0, -20(%rbp)
	setL -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Lbreak_tmp.5
	leaq nested_static_arr(%rip), %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movslq -4(%rbp), %r11
	movq %r11, -48(%rbp)
	movq -48(%rbp), %r10
	movq %r10, -56(%rbp)
	movq -40(%rbp), %rax
	movq -56(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movslq -16(%rbp), %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -72(%rbp), %rax
	movq -88(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -97(%rbp)
	movb -97(%rbp), %r10b
	movb %r10b, -98(%rbp)
	movb $0, -99(%rbp)
	movb -99(%rbp), %r10b
	movb %r10b, -100(%rbp)
	cmpl $1, -4(%rbp)
	movl $0, -104(%rbp)
	setE -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.24
	cmpl $0, -16(%rbp)
	movl $0, -108(%rbp)
	setE -108(%rbp)
	cmpl $0, -108(%rbp)
	jE .Ltmp.24
	movl $1, -112(%rbp)
	jmp .Ltmp.27
.Ltmp.24:
	movl $0, -112(%rbp)
.Ltmp.27:
	movl -112(%rbp), %r10d
	movl %r10d, -116(%rbp)
	cmpl $0, -116(%rbp)
	jE .Ltmp.30
	movb $98, -117(%rbp)
	movb -117(%rbp), %r10b
	movb %r10b, -100(%rbp)
	jmp .Ltmp.29
.Ltmp.30:
	cmpl $1, -4(%rbp)
	movl $0, -124(%rbp)
	setE -124(%rbp)
	cmpl $0, -124(%rbp)
	jE .Ltmp.33
	cmpl $1, -16(%rbp)
	movl $0, -128(%rbp)
	setE -128(%rbp)
	cmpl $0, -128(%rbp)
	jE .Ltmp.33
	movl $1, -132(%rbp)
	jmp .Ltmp.36
.Ltmp.33:
	movl $0, -132(%rbp)
.Ltmp.36:
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.29
	movb $99, -137(%rbp)
	movb -137(%rbp), %r10b
	movb %r10b, -100(%rbp)
.Ltmp.29:
	movsbl -98(%rbp), %r11d
	movq %r11, -144(%rbp)
	movsbl -100(%rbp), %r11d
	movq %r11, -148(%rbp)
	movl -148(%rbp), %r10d
	cmpl %r10d, -144(%rbp)
	movl $0, -152(%rbp)
	setNE -152(%rbp)
	movl -152(%rbp), %r10d
	movl %r10d, -156(%rbp)
	cmpl $0, -156(%rbp)
	jE .Ltmp.43
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.43:
.Lcontinue_tmp.5:
	movl -16(%rbp), %r10d
	movl %r10d, -160(%rbp)
	addl $1, -160(%rbp)
	movl -160(%rbp), %r10d
	movl %r10d, -16(%rbp)
	jmp .Ltmp.9
.Lbreak_tmp.5:
.Lcontinue_tmp.4:
	movl -4(%rbp), %r10d
	movl %r10d, -164(%rbp)
	addl $1, -164(%rbp)
	movl -164(%rbp), %r10d
	movl %r10d, -4(%rbp)
	jmp .Ltmp.6
.Lbreak_tmp.4:
	movl $1, %eax
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
	subq $16, %rsp
	call test_static_nested
	movl %eax, -4(%rbp)
	cmpl $0, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.49
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.49:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.data
	.align 1
nested_static_arr:
	.asciz ""
	.zero 3
	.asciz "bc"
	.zero 1
	.zero 4
	.section	.note.GNU-stack,"",@progbits
