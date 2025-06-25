	.globl return_ptr
	.text
return_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -16(%rbp), %rax
	movq -32(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl check_char_ptr_argument
	.text
check_char_ptr_argument:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq %rdi, -8(%rbp)
	movb %sil, -9(%rbp)
	movq -8(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -10(%rbp)
	movsbl -10(%rbp), %r11d
	movl %r11d, -16(%rbp)
	movsbl -9(%rbp), %r11d
	movl %r11d, -20(%rbp)
	movl -20(%rbp), %r10d
	cmpl %r10d, -16(%rbp)
	movl $0, -24(%rbp)
	setE -24(%rbp)
	movl -24(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_void_ptr_as_int_ptr
	.text
return_void_ptr_as_int_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl get_dbl_array
	.text
get_dbl_array:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %r11
	imul $8, %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %rdi
	call malloc
	movq %rax, -32(%rbp)
	movq -32(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl set_doubles
	.text
set_doubles:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movq %rdi, -8(%rbp)
	movq %rsi, -16(%rbp)
	movsd %xmm0, -24(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
.Ltmp.41:
	movq -16(%rbp), %r10
	cmpq %r10, -40(%rbp)
	movl $0, -44(%rbp)
	setB -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Lbreak_tmp.28
	movq -8(%rbp), %r10
	movq %r10, -56(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movq -56(%rbp), %rax
	movq -72(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %rax
	movsd -24(%rbp), %xmm14
	movsd %xmm14, 0(%rax)
.Lcontinue_tmp.28:
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -88(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -96(%rbp)
	movq -88(%rbp), %r10
	addq %r10, -96(%rbp)
	movq -96(%rbp), %r10
	movq %r10, -40(%rbp)
	jmp .Ltmp.41
.Lbreak_tmp.28:
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_dbl_ptr_as_void_ptr
	.text
return_dbl_ptr_as_void_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movq -8(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.210:
	.double 4.0
	.section .rodata
	.align 8
tmp.211:
	.double 4.0
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $1216, %rsp
	movl $4, %r10d
	movslq %r10d, %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movq -16(%rbp), %rdi
	call malloc
	movq %rax, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movl $1, -44(%rbp)
	negl -44(%rbp)
	movq -40(%rbp), %rax
	movl -44(%rbp), %r10d
	movl %r10d, 0(%rax)
	movq -32(%rbp), %r10
	movq %r10, -56(%rbp)
	movl $1, -60(%rbp)
	negl -60(%rbp)
	movb -60(%rbp), %r10b
	movb %r10b, -61(%rbp)
	movb -61(%rbp), %r10b
	movb %r10b, -62(%rbp)
	movq -56(%rbp), %rdi
	movb -62(%rbp), %sil
	call check_char_ptr_argument
	movl %eax, -68(%rbp)
	cmpl $0, -68(%rbp)
	movl $0, -72(%rbp)
	setE -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	cmpl $0, -76(%rbp)
	jE .Ltmp.61
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.61:
	movq -32(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -88(%rbp), %rdi
	call return_void_ptr_as_int_ptr
	movq %rax, -96(%rbp)
	movq -40(%rbp), %r10
	cmpq %r10, -96(%rbp)
	movl $0, -100(%rbp)
	setNE -100(%rbp)
	movl -100(%rbp), %r10d
	movl %r10d, -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.66
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.66:
	movq -32(%rbp), %r10
	movq %r10, -112(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -120(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -128(%rbp)
	movq -32(%rbp), %r10
	cmpq %r10, -112(%rbp)
	movl $0, -132(%rbp)
	setNE -132(%rbp)
	cmpl $0, -132(%rbp)
	jNE .Ltmp.68
	movq -32(%rbp), %r10
	cmpq %r10, -120(%rbp)
	movl $0, -136(%rbp)
	setNE -136(%rbp)
	cmpl $0, -136(%rbp)
	jNE .Ltmp.68
	movl $0, -140(%rbp)
	jmp .Ltmp.71
.Ltmp.68:
	movl $1, -140(%rbp)
.Ltmp.71:
	cmpl $0, -140(%rbp)
	jNE .Ltmp.72
	movq -32(%rbp), %r10
	cmpq %r10, -128(%rbp)
	movl $0, -144(%rbp)
	setNE -144(%rbp)
	cmpl $0, -144(%rbp)
	jNE .Ltmp.72
	movl $0, -148(%rbp)
	jmp .Ltmp.75
.Ltmp.72:
	movl $1, -148(%rbp)
.Ltmp.75:
	movl -148(%rbp), %r10d
	movl %r10d, -152(%rbp)
	cmpl $0, -152(%rbp)
	jE .Ltmp.77
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.77:
	movq -32(%rbp), %r10
	movq %r10, -160(%rbp)
	movq -160(%rbp), %rdi
	call free
	movl $5, %r10d
	movslq %r10d, %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movq -176(%rbp), %rdi
	call get_dbl_array
	movq %rax, -184(%rbp)
	movq -184(%rbp), %r10
	movq %r10, -192(%rbp)
	movq -192(%rbp), %r10
	movq %r10, -200(%rbp)
	movq -200(%rbp), %r10
	movq %r10, -208(%rbp)
	movl $5, %r10d
	movslq %r10d, %r11
	movq %r11, -216(%rbp)
	movq -216(%rbp), %r10
	movq %r10, -224(%rbp)
	movsd tmp.210(%rip), %xmm14
	movsd %xmm14, -232(%rbp)
	movq -208(%rbp), %rdi
	movq -224(%rbp), %rsi
	movsd -232(%rbp), %xmm0
	call set_doubles
	movq -192(%rbp), %r10
	movq %r10, -240(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -248(%rbp)
	movq -248(%rbp), %r10
	movq %r10, -256(%rbp)
	movq -240(%rbp), %rax
	movq -256(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -264(%rbp)
	movq -264(%rbp), %rax
	movsd 0(%rax), %xmm14
	movsd %xmm14, -272(%rbp)
	movsd -272(%rbp), %xmm15
	comisd tmp.211(%rip), %xmm15
	movl $0, -276(%rbp)
	setNE -276(%rbp)
	movl -276(%rbp), %r10d
	movl %r10d, -280(%rbp)
	cmpl $0, -280(%rbp)
	jE .Ltmp.93
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.93:
	movq -192(%rbp), %r10
	movq %r10, -288(%rbp)
	movq -288(%rbp), %rdi
	call return_dbl_ptr_as_void_ptr
	movq %rax, -296(%rbp)
	movq -200(%rbp), %r10
	cmpq %r10, -296(%rbp)
	movl $0, -300(%rbp)
	setNE -300(%rbp)
	movl -300(%rbp), %r10d
	movl %r10d, -304(%rbp)
	cmpl $0, -304(%rbp)
	jE .Ltmp.98
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.98:
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -312(%rbp)
	movq -312(%rbp), %r10
	movq %r10, -320(%rbp)
	movq -192(%rbp), %r10
	movq %r10, -320(%rbp)
	movq -200(%rbp), %r10
	cmpq %r10, -320(%rbp)
	movl $0, -324(%rbp)
	setNE -324(%rbp)
	movl -324(%rbp), %r10d
	movl %r10d, -328(%rbp)
	cmpl $0, -328(%rbp)
	jE .Ltmp.102
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.102:
	leaq -320(%rbp), %r11
	movq %r11, -336(%rbp)
	movq -336(%rbp), %r10
	movq %r10, -320(%rbp)
	movq -200(%rbp), %r10
	cmpq %r10, -320(%rbp)
	movl $0, -340(%rbp)
	setE -340(%rbp)
	movl -340(%rbp), %r10d
	movl %r10d, -344(%rbp)
	cmpl $0, -344(%rbp)
	jE .Ltmp.106
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.106:
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -352(%rbp)
	movq -352(%rbp), %r10
	movq %r10, -120(%rbp)
	movq -120(%rbp), %r10
	movq %r10, -320(%rbp)
	movq -320(%rbp), %r10
	movq %r10, -360(%rbp)
	cmpq $0, -360(%rbp)
	jE .Ltmp.109
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.109:
	movq -192(%rbp), %r10
	movq %r10, -368(%rbp)
	movq -368(%rbp), %rdi
	call free
	movq $8, -376(%rbp)
	movq -376(%rbp), %rdi
	call malloc
	movq %rax, -384(%rbp)
	movq -384(%rbp), %r10
	movq %r10, -416(%rbp)
	movq $8, -424(%rbp)
	movq -424(%rbp), %rdi
	call malloc
	movq %rax, -432(%rbp)
	movq -432(%rbp), %r10
	movq %r10, -408(%rbp)
	movq $8, -440(%rbp)
	movq -440(%rbp), %rdi
	call malloc
	movq %rax, -448(%rbp)
	movq -448(%rbp), %r10
	movq %r10, -400(%rbp)
	leaq -416(%rbp), %r11
	movq %r11, -456(%rbp)
	movq -456(%rbp), %r10
	movq %r10, -464(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -472(%rbp)
	movq -472(%rbp), %r10
	movq %r10, -480(%rbp)
	movq -464(%rbp), %rax
	movq -480(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -488(%rbp)
	movq -488(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -496(%rbp)
	movq -496(%rbp), %rax
	movq $100, 0(%rax)
	leaq -416(%rbp), %r11
	movq %r11, -504(%rbp)
	movq -504(%rbp), %r10
	movq %r10, -512(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -520(%rbp)
	movq -520(%rbp), %r10
	movq %r10, -528(%rbp)
	movq -512(%rbp), %rax
	movq -528(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -536(%rbp)
	movq -536(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -544(%rbp)
	movq -544(%rbp), %rax
	movq $200, 0(%rax)
	leaq -416(%rbp), %r11
	movq %r11, -552(%rbp)
	movq -552(%rbp), %r10
	movq %r10, -560(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -568(%rbp)
	movq -568(%rbp), %r10
	movq %r10, -576(%rbp)
	movq -560(%rbp), %rax
	movq -576(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -584(%rbp)
	movq -584(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -592(%rbp)
	movq -592(%rbp), %rax
	movq $300, 0(%rax)
	leaq -416(%rbp), %r11
	movq %r11, -600(%rbp)
	movq -600(%rbp), %r10
	movq %r10, -608(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -616(%rbp)
	movq -616(%rbp), %r10
	movq %r10, -624(%rbp)
	movq -608(%rbp), %rax
	movq -624(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -632(%rbp)
	movq -632(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -640(%rbp)
	movq -640(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -648(%rbp)
	leaq -416(%rbp), %r11
	movq %r11, -656(%rbp)
	movq -656(%rbp), %r10
	movq %r10, -664(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -672(%rbp)
	movq -672(%rbp), %r10
	movq %r10, -680(%rbp)
	movq -664(%rbp), %rax
	movq -680(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -688(%rbp)
	movq -688(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -696(%rbp)
	movq -696(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -704(%rbp)
	movq -648(%rbp), %r10
	movq %r10, -712(%rbp)
	movq -704(%rbp), %r10
	addq %r10, -712(%rbp)
	leaq -416(%rbp), %r11
	movq %r11, -720(%rbp)
	movq -720(%rbp), %r10
	movq %r10, -728(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -736(%rbp)
	movq -736(%rbp), %r10
	movq %r10, -744(%rbp)
	movq -728(%rbp), %rax
	movq -744(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -752(%rbp)
	movq -752(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -760(%rbp)
	movq -760(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -768(%rbp)
	movq -712(%rbp), %r10
	movq %r10, -776(%rbp)
	movq -768(%rbp), %r10
	addq %r10, -776(%rbp)
	movq -776(%rbp), %r10
	movq %r10, -784(%rbp)
	cmpq $600, -784(%rbp)
	movl $0, -788(%rbp)
	setNE -788(%rbp)
	movl -788(%rbp), %r10d
	movl %r10d, -792(%rbp)
	cmpl $0, -792(%rbp)
	jE .Ltmp.160
	movl $9, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.160:
	leaq -416(%rbp), %r11
	movq %r11, -800(%rbp)
	movq -800(%rbp), %r10
	movq %r10, -808(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -816(%rbp)
	movq -816(%rbp), %r10
	movq %r10, -824(%rbp)
	movq -808(%rbp), %rax
	movq -824(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -832(%rbp)
	movq -832(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -840(%rbp)
	movq -840(%rbp), %r10
	movq %r10, -848(%rbp)
	movq -848(%rbp), %rdi
	call free
	leaq -416(%rbp), %r11
	movq %r11, -856(%rbp)
	movq -856(%rbp), %r10
	movq %r10, -864(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -872(%rbp)
	movq -872(%rbp), %r10
	movq %r10, -880(%rbp)
	movq -864(%rbp), %rax
	movq -880(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -888(%rbp)
	movq -888(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -896(%rbp)
	movq -896(%rbp), %r10
	movq %r10, -904(%rbp)
	movq -904(%rbp), %rdi
	call free
	leaq -416(%rbp), %r11
	movq %r11, -912(%rbp)
	movq -912(%rbp), %r10
	movq %r10, -920(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -928(%rbp)
	movq -928(%rbp), %r10
	movq %r10, -936(%rbp)
	movq -920(%rbp), %rax
	movq -936(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -944(%rbp)
	movq -944(%rbp), %rax
	movq 0(%rax), %r10
	movq %r10, -952(%rbp)
	movq -952(%rbp), %r10
	movq %r10, -960(%rbp)
	movq -960(%rbp), %rdi
	call free
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -968(%rbp)
	movq -968(%rbp), %r10
	movq %r10, -992(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -1000(%rbp)
	movq -1000(%rbp), %r10
	movq %r10, -984(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -1008(%rbp)
	movq -1008(%rbp), %r10
	movq %r10, -976(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -1016(%rbp)
	movq -1016(%rbp), %r10
	movq %r10, -1040(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -1048(%rbp)
	movq -1048(%rbp), %r10
	movq %r10, -1032(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -1056(%rbp)
	movq -1056(%rbp), %r10
	movq %r10, -1024(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -1064(%rbp)
	movq -1064(%rbp), %r10
	movq %r10, -1088(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -1096(%rbp)
	movq -1096(%rbp), %r10
	movq %r10, -1080(%rbp)
	movl $4, %r10d
	movslq %r10d, %r11
	movq %r11, -1104(%rbp)
	movq -1104(%rbp), %r10
	movq %r10, -1072(%rbp)
	leaq -992(%rbp), %r11
	movq %r11, -1112(%rbp)
	movq -1112(%rbp), %r10
	movq %r10, -1120(%rbp)
	leaq -1040(%rbp), %r11
	movq %r11, -1128(%rbp)
	movq -1128(%rbp), %r10
	movq %r10, -1136(%rbp)
	movq $24, -1144(%rbp)
	movq -1120(%rbp), %rdi
	movq -1136(%rbp), %rsi
	movq -1144(%rbp), %rdx
	call memcmp
	movl %eax, -1148(%rbp)
	cmpl $0, -1148(%rbp)
	movl $0, -1152(%rbp)
	setNE -1152(%rbp)
	movl -1152(%rbp), %r10d
	movl %r10d, -1156(%rbp)
	cmpl $0, -1156(%rbp)
	jE .Ltmp.199
	movl $10, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.199:
	leaq -992(%rbp), %r11
	movq %r11, -1168(%rbp)
	movq -1168(%rbp), %r10
	movq %r10, -1176(%rbp)
	leaq -1088(%rbp), %r11
	movq %r11, -1184(%rbp)
	movq -1184(%rbp), %r10
	movq %r10, -1192(%rbp)
	movq $24, -1200(%rbp)
	movq -1176(%rbp), %rdi
	movq -1192(%rbp), %rsi
	movq -1200(%rbp), %rdx
	call memcmp
	movl %eax, -1204(%rbp)
	movl $1, -1208(%rbp)
	negl -1208(%rbp)
	movl -1208(%rbp), %r10d
	cmpl %r10d, -1204(%rbp)
	movl $0, -1212(%rbp)
	setNE -1212(%rbp)
	movl -1212(%rbp), %r10d
	movl %r10d, -1216(%rbp)
	cmpl $0, -1216(%rbp)
	jE .Ltmp.209
	movl $11, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.209:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
