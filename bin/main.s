
	.globl return_struct
	.text
return_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $144, %rsp
	leaq on_page_boundary+0(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movl $9, %r10d
	movslq %r10d, %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -16(%rbp), %rax
	movq -32(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -40(%rbp)
	movl $1, -44(%rbp)
	negl -44(%rbp)
	movb -44(%rbp), %r10b
	movb %r10b, -45(%rbp)
	movq -40(%rbp), %rax
	movb -45(%rbp), %r10b
	movb %r10b, 0(%rax)
	leaq on_page_boundary+0(%rip), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	movq %r10, -64(%rbp)
	movl $8, %r10d
	movslq %r10d, %r11
	movq %r11, -72(%rbp)
	movq -72(%rbp), %r10
	movq %r10, -80(%rbp)
	movq -64(%rbp), %rax
	movq -80(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -88(%rbp)
	movl $2, -92(%rbp)
	negl -92(%rbp)
	movb -92(%rbp), %r10b
	movb %r10b, -93(%rbp)
	movq -88(%rbp), %rax
	movb -93(%rbp), %r10b
	movb %r10b, 0(%rax)
	leaq on_page_boundary+0(%rip), %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %r10
	movq %r10, -112(%rbp)
	movl $7, %r10d
	movslq %r10d, %r11
	movq %r11, -120(%rbp)
	movq -120(%rbp), %r10
	movq %r10, -128(%rbp)
	movq -112(%rbp), %rax
	movq -128(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -136(%rbp)
	movl $3, -140(%rbp)
	negl -140(%rbp)
	movb -140(%rbp), %r10b
	movb %r10b, -141(%rbp)
	movq -136(%rbp), %rax
	movb -141(%rbp), %r10b
	movb %r10b, 0(%rax)
	movq on_page_boundary+0(%rip), %rax
	movb on_page_boundary+9(%rip), %dl
	shl $8, %rdx
	movb on_page_boundary+8(%rip), %dl
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
	subq $272, %rsp
	call return_struct
	movq %rax, -10(%rbp)
	movb %dl, -2(%rbp)
	shr $8, %rdx
	movb %dl, -1(%rbp)
	movq -10(%rbp), %r10
	movq %r10, -20(%rbp)
	movb -2(%rbp), %r10b
	movb %r10b, -12(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -11(%rbp)
	movl $0, -24(%rbp)
.Ltmp.26:
	cmpl $7, -24(%rbp)
	movl $0, -28(%rbp)
	setL -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Lbreak_tmp.3
	leaq -20(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movslq -24(%rbp), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	movq %r10, -64(%rbp)
	movq -48(%rbp), %rax
	movq -64(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -72(%rbp)
	movq -72(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -73(%rbp)
	movb -73(%rbp), %r10b
	movb %r10b, -74(%rbp)
	cmpb $0, -74(%rbp)
	jE .Ltmp.36
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.36:
.Lcontinue_tmp.3:
	movl -24(%rbp), %r10d
	movl %r10d, -80(%rbp)
	addl $1, -80(%rbp)
	movl -80(%rbp), %r10d
	movl %r10d, -24(%rbp)
	jmp .Ltmp.26
.Lbreak_tmp.3:
	leaq -20(%rbp), %r11
	movq %r11, -88(%rbp)
	movq -88(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -88(%rbp)
	movq -88(%rbp), %r10
	movq %r10, -96(%rbp)
	movl $7, %r10d
	movslq %r10d, %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %r10
	movq %r10, -112(%rbp)
	movq -96(%rbp), %rax
	movq -112(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -120(%rbp)
	movq -120(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -121(%rbp)
	movsbl -121(%rbp), %r11d
	movl %r11d, -128(%rbp)
	movl $3, -132(%rbp)
	negl -132(%rbp)
	movl -132(%rbp), %r10d
	cmpl %r10d, -128(%rbp)
	movl $0, -136(%rbp)
	setNE -136(%rbp)
	movl -136(%rbp), %r10d
	movl %r10d, -140(%rbp)
	cmpl $0, -140(%rbp)
	jE .Ltmp.48
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.48:
	leaq -20(%rbp), %r11
	movq %r11, -152(%rbp)
	movq -152(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -152(%rbp)
	movq -152(%rbp), %r10
	movq %r10, -160(%rbp)
	movl $8, %r10d
	movslq %r10d, %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movq -160(%rbp), %rax
	movq -176(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -184(%rbp)
	movq -184(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -185(%rbp)
	movsbl -185(%rbp), %r11d
	movl %r11d, -192(%rbp)
	movl $2, -196(%rbp)
	negl -196(%rbp)
	movl -196(%rbp), %r10d
	cmpl %r10d, -192(%rbp)
	movl $0, -200(%rbp)
	setNE -200(%rbp)
	movl -200(%rbp), %r10d
	movl %r10d, -204(%rbp)
	cmpl $0, -204(%rbp)
	jE .Ltmp.59
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.59:
	leaq -20(%rbp), %r11
	movq %r11, -216(%rbp)
	movq -216(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -216(%rbp)
	movq -216(%rbp), %r10
	movq %r10, -224(%rbp)
	movl $9, %r10d
	movslq %r10d, %r11
	movq %r11, -232(%rbp)
	movq -232(%rbp), %r10
	movq %r10, -240(%rbp)
	movq -224(%rbp), %rax
	movq -240(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -248(%rbp)
	movq -248(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -249(%rbp)
	movsbl -249(%rbp), %r11d
	movl %r11d, -256(%rbp)
	movl $1, -260(%rbp)
	negl -260(%rbp)
	movl -260(%rbp), %r10d
	cmpl %r10d, -256(%rbp)
	movl $0, -264(%rbp)
	setNE -264(%rbp)
	movl -264(%rbp), %r10d
	movl %r10d, -268(%rbp)
	cmpl $0, -268(%rbp)
	jE .Ltmp.70
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.70:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
