	.globl char_to_uchar
	.text
char_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_schar
	.text
char_to_schar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_char
	.text
uchar_to_char:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_char
	.text
schar_to_char:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_schar
	.text
uchar_to_schar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_uchar
	.text
schar_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_int
	.text
char_to_int:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_uint
	.text
char_to_uint:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_long
	.text
char_to_long:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_ulong
	.text
char_to_ulong:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl char_to_double
	.text
char_to_double:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %eax
	cvtsi2sdl %eax, %xmm15
	movsd %xmm15, -16(%rbp)
	movsd -16(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_int
	.text
schar_to_int:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_uint
	.text
schar_to_uint:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_long
	.text
schar_to_long:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_ulong
	.text
schar_to_ulong:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl schar_to_double
	.text
schar_to_double:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movsbl -1(%rbp), %eax
	cvtsi2sdl %eax, %xmm15
	movsd %xmm15, -16(%rbp)
	movsd -16(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_int
	.text
uchar_to_int:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movzbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_uint
	.text
uchar_to_uint:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movzbl -1(%rbp), %r11d
	movl %r11d, -8(%rbp)
	movl -8(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_long
	.text
uchar_to_long:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movzbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_ulong
	.text
uchar_to_ulong:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movzbq -1(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uchar_to_double
	.text
uchar_to_double:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb %dil, -1(%rbp)
	movzbl -1(%rbp), %eax
	cvtsi2sdl %eax, %xmm15
	movsd %xmm15, -16(%rbp)
	movsd -16(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl int_to_char
	.text
int_to_char:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl %edi, -4(%rbp)
	movb -4(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb -5(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uint_to_char
	.text
uint_to_char:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl %edi, -4(%rbp)
	movb -4(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb -5(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl double_to_char
	.text
double_to_char:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd %xmm0, -8(%rbp)
	cvttsd2sil -8(%rbp), %eax
	movb %al, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl long_to_schar
	.text
long_to_schar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movb -8(%rbp), %r10b
	movb %r10b, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl ulong_to_schar
	.text
ulong_to_schar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movb -8(%rbp), %r10b
	movb %r10b, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl int_to_uchar
	.text
int_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl %edi, -4(%rbp)
	movb -4(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb -5(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl uint_to_uchar
	.text
uint_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl %edi, -4(%rbp)
	movb -4(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb -5(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl long_to_uchar
	.text
long_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movb -8(%rbp), %r10b
	movb %r10b, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl ulong_to_uchar
	.text
ulong_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, -8(%rbp)
	movb -8(%rbp), %r10b
	movb %r10b, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl double_to_uchar
	.text
double_to_uchar:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd %xmm0, -8(%rbp)
	cvttsd2sil -8(%rbp), %eax
	movb %al, -9(%rbp)
	movb -9(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.253:
	.double 10.0
	.section .rodata
	.align 16
tmp.254:
	.double -0.0
	.section .rodata
	.align 8
tmp.255:
	.double 250.0
	.section .rodata
	.align 8
tmp.256:
	.double 2.6
	.section .rodata
	.align 16
tmp.257:
	.double -0.0
	.section .rodata
	.align 8
tmp.258:
	.double 200.99
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $720, %rsp
	movb $127, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %r10b
	movb %r10b, -3(%rbp)
	movb -3(%rbp), %dil
	call char_to_uchar
	movb %al, -4(%rbp)
	movzbl -4(%rbp), %r11d
	movl %r11d, -8(%rbp)
	cmpl $127, -8(%rbp)
	movl $0, -12(%rbp)
	setNE -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Ltmp.74
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.74:
	movb -2(%rbp), %r10b
	movb %r10b, -17(%rbp)
	movb -17(%rbp), %dil
	call char_to_int
	movl %eax, -24(%rbp)
	cmpl $127, -24(%rbp)
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	movl -28(%rbp), %r10d
	movl %r10d, -32(%rbp)
	cmpl $0, -32(%rbp)
	jE .Ltmp.79
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.79:
	movb -2(%rbp), %r10b
	movb %r10b, -33(%rbp)
	movb -33(%rbp), %dil
	call char_to_ulong
	movq %rax, -48(%rbp)
	movl $127, %r10d
	movslq %r10d, %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	cmpq %r10, -48(%rbp)
	movl $0, -60(%rbp)
	setNE -60(%rbp)
	movl -60(%rbp), %r10d
	movl %r10d, -64(%rbp)
	cmpl $0, -64(%rbp)
	jE .Ltmp.85
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.85:
	movl $10, -68(%rbp)
	negl -68(%rbp)
	movb -68(%rbp), %r10b
	movb %r10b, -69(%rbp)
	movb -69(%rbp), %r10b
	movb %r10b, -70(%rbp)
	movb -70(%rbp), %r10b
	movb %r10b, -71(%rbp)
	movb -71(%rbp), %dil
	call schar_to_uchar
	movb %al, -72(%rbp)
	movzbl -72(%rbp), %r11d
	movl %r11d, -76(%rbp)
	cmpl $246, -76(%rbp)
	movl $0, -80(%rbp)
	setNE -80(%rbp)
	movl -80(%rbp), %r10d
	movl %r10d, -84(%rbp)
	cmpl $0, -84(%rbp)
	jE .Ltmp.93
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.93:
	movb -70(%rbp), %r10b
	movb %r10b, -85(%rbp)
	movb -85(%rbp), %dil
	call schar_to_long
	movq %rax, -96(%rbp)
	movl $10, -100(%rbp)
	negl -100(%rbp)
	movslq -100(%rbp), %r11
	movq %r11, -112(%rbp)
	movq -112(%rbp), %r10
	cmpq %r10, -96(%rbp)
	movl $0, -116(%rbp)
	setNE -116(%rbp)
	movl -116(%rbp), %r10d
	movl %r10d, -120(%rbp)
	cmpl $0, -120(%rbp)
	jE .Ltmp.100
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.100:
	movb -70(%rbp), %r10b
	movb %r10b, -121(%rbp)
	movb -121(%rbp), %dil
	call schar_to_uint
	movl %eax, -128(%rbp)
	movl $4294967286, %r10d
	cmpl %r10d, -128(%rbp)
	movl $0, -132(%rbp)
	setNE -132(%rbp)
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.105
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.105:
	movb -70(%rbp), %r10b
	movb %r10b, -137(%rbp)
	movb -137(%rbp), %dil
	call schar_to_double
	movsd %xmm0, -152(%rbp)
	movsd tmp.253(%rip), %xmm14
	movsd %xmm14, -160(%rbp)
	movsd -160(%rbp), %xmm15
	xorpd tmp.254(%rip), %xmm15
	movsd %xmm15, -160(%rbp)
	movsd -152(%rbp), %xmm15
	comisd -160(%rbp), %xmm15
	movl $0, -164(%rbp)
	setNE -164(%rbp)
	movl -164(%rbp), %r10d
	movl %r10d, -168(%rbp)
	cmpl $0, -168(%rbp)
	jE .Ltmp.111
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.111:
	movb $250, -169(%rbp)
	movb -169(%rbp), %r10b
	movb %r10b, -170(%rbp)
	movb -170(%rbp), %r10b
	movb %r10b, -171(%rbp)
	movb -171(%rbp), %dil
	call uchar_to_int
	movl %eax, -176(%rbp)
	cmpl $250, -176(%rbp)
	movl $0, -180(%rbp)
	setNE -180(%rbp)
	movl -180(%rbp), %r10d
	movl %r10d, -184(%rbp)
	cmpl $0, -184(%rbp)
	jE .Ltmp.117
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.117:
	movb -170(%rbp), %r10b
	movb %r10b, -185(%rbp)
	movb -185(%rbp), %dil
	call uchar_to_long
	movq %rax, -200(%rbp)
	movl $250, %r10d
	movslq %r10d, %r11
	movq %r11, -208(%rbp)
	movq -208(%rbp), %r10
	cmpq %r10, -200(%rbp)
	movl $0, -212(%rbp)
	setNE -212(%rbp)
	movl -212(%rbp), %r10d
	movl %r10d, -216(%rbp)
	cmpl $0, -216(%rbp)
	jE .Ltmp.123
	movl $9, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.123:
	movb -170(%rbp), %r10b
	movb %r10b, -217(%rbp)
	movb -217(%rbp), %dil
	call uchar_to_uint
	movl %eax, -224(%rbp)
	movl $250, -228(%rbp)
	movl -228(%rbp), %r10d
	cmpl %r10d, -224(%rbp)
	movl $0, -232(%rbp)
	setNE -232(%rbp)
	movl -232(%rbp), %r10d
	movl %r10d, -236(%rbp)
	cmpl $0, -236(%rbp)
	jE .Ltmp.129
	movl $10, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.129:
	movb -170(%rbp), %r10b
	movb %r10b, -237(%rbp)
	movb -237(%rbp), %dil
	call uchar_to_ulong
	movq %rax, -248(%rbp)
	movl $250, %r10d
	movslq %r10d, %r11
	movq %r11, -256(%rbp)
	movq -256(%rbp), %r10
	cmpq %r10, -248(%rbp)
	movl $0, -260(%rbp)
	setNE -260(%rbp)
	movl -260(%rbp), %r10d
	movl %r10d, -264(%rbp)
	cmpl $0, -264(%rbp)
	jE .Ltmp.135
	movl $11, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.135:
	movb -170(%rbp), %r10b
	movb %r10b, -265(%rbp)
	movb -265(%rbp), %dil
	call uchar_to_double
	movsd %xmm0, -280(%rbp)
	movsd -280(%rbp), %xmm15
	comisd tmp.255(%rip), %xmm15
	movl $0, -284(%rbp)
	setNE -284(%rbp)
	movl -284(%rbp), %r10d
	movl %r10d, -288(%rbp)
	cmpl $0, -288(%rbp)
	jE .Ltmp.140
	movl $12, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.140:
	movb -170(%rbp), %r10b
	movb %r10b, -289(%rbp)
	movb -289(%rbp), %dil
	call uchar_to_schar
	movb %al, -290(%rbp)
	movsbl -290(%rbp), %r11d
	movl %r11d, -296(%rbp)
	movl $6, -300(%rbp)
	negl -300(%rbp)
	movl -300(%rbp), %r10d
	cmpl %r10d, -296(%rbp)
	movl $0, -304(%rbp)
	setNE -304(%rbp)
	movl -304(%rbp), %r10d
	movl %r10d, -308(%rbp)
	cmpl $0, -308(%rbp)
	jE .Ltmp.147
	movl $13, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.147:
	movb -170(%rbp), %r10b
	movb %r10b, -309(%rbp)
	movb -309(%rbp), %dil
	call uchar_to_char
	movb %al, -310(%rbp)
	movsbl -310(%rbp), %r11d
	movl %r11d, -316(%rbp)
	movl $6, -320(%rbp)
	negl -320(%rbp)
	movl -320(%rbp), %r10d
	cmpl %r10d, -316(%rbp)
	movl $0, -324(%rbp)
	setNE -324(%rbp)
	movl -324(%rbp), %r10d
	movl %r10d, -328(%rbp)
	cmpl $0, -328(%rbp)
	jE .Ltmp.154
	movl $14, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.154:
	movl $128, -332(%rbp)
	negl -332(%rbp)
	movb -332(%rbp), %r10b
	movb %r10b, -333(%rbp)
	movb -333(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movl $128, -340(%rbp)
	movl -340(%rbp), %edi
	call int_to_char
	movb %al, -341(%rbp)
	movsbl -341(%rbp), %r11d
	movl %r11d, -348(%rbp)
	movsbl -2(%rbp), %r11d
	movl %r11d, -352(%rbp)
	movl -352(%rbp), %r10d
	cmpl %r10d, -348(%rbp)
	movl $0, -356(%rbp)
	setNE -356(%rbp)
	movl -356(%rbp), %r10d
	movl %r10d, -360(%rbp)
	cmpl $0, -360(%rbp)
	jE .Ltmp.163
	movl $15, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.163:
	movl $6, -364(%rbp)
	negl -364(%rbp)
	movb -364(%rbp), %r10b
	movb %r10b, -365(%rbp)
	movb -365(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movl $2147483898, -372(%rbp)
	movl -372(%rbp), %edi
	call uint_to_char
	movb %al, -373(%rbp)
	movsbl -373(%rbp), %r11d
	movl %r11d, -380(%rbp)
	movsbl -2(%rbp), %r11d
	movl %r11d, -384(%rbp)
	movl -384(%rbp), %r10d
	cmpl %r10d, -380(%rbp)
	movl $0, -388(%rbp)
	setNE -388(%rbp)
	movl -388(%rbp), %r10d
	movl %r10d, -392(%rbp)
	cmpl $0, -392(%rbp)
	jE .Ltmp.172
	movl $16, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.172:
	movl $2, -396(%rbp)
	negl -396(%rbp)
	movb -396(%rbp), %r10b
	movb %r10b, -397(%rbp)
	movb -397(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movsd tmp.256(%rip), %xmm14
	movsd %xmm14, -408(%rbp)
	movsd -408(%rbp), %xmm15
	xorpd tmp.257(%rip), %xmm15
	movsd %xmm15, -408(%rbp)
	movsd -408(%rbp), %xmm14
	movsd %xmm14, -416(%rbp)
	movsd -416(%rbp), %xmm0
	call double_to_char
	movb %al, -417(%rbp)
	movsbl -417(%rbp), %r11d
	movl %r11d, -424(%rbp)
	movsbl -2(%rbp), %r11d
	movl %r11d, -428(%rbp)
	movl -428(%rbp), %r10d
	cmpl %r10d, -424(%rbp)
	movl $0, -432(%rbp)
	setNE -432(%rbp)
	movl -432(%rbp), %r10d
	movl %r10d, -436(%rbp)
	cmpl $0, -436(%rbp)
	jE .Ltmp.182
	movl $17, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.182:
	movq $17592186044416, %r10
	movq %r10, -448(%rbp)
	movq -448(%rbp), %rdi
	call long_to_schar
	movb %al, -449(%rbp)
	movb -449(%rbp), %r10b
	movb %r10b, -450(%rbp)
	cmpb $0, -450(%rbp)
	jE .Ltmp.186
	movl $18, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.186:
	movl $126, -456(%rbp)
	negl -456(%rbp)
	movb -456(%rbp), %r10b
	movb %r10b, -457(%rbp)
	movb -457(%rbp), %r10b
	movb %r10b, -70(%rbp)
	movq $9224497936761618562, %r10
	movq %r10, -472(%rbp)
	movq -472(%rbp), %rdi
	call ulong_to_schar
	movb %al, -473(%rbp)
	movsbl -473(%rbp), %r11d
	movl %r11d, -480(%rbp)
	movsbl -70(%rbp), %r11d
	movl %r11d, -484(%rbp)
	movl -484(%rbp), %r10d
	cmpl %r10d, -480(%rbp)
	movl $0, -488(%rbp)
	setNE -488(%rbp)
	movl -488(%rbp), %r10d
	movl %r10d, -492(%rbp)
	cmpl $0, -492(%rbp)
	jE .Ltmp.195
	movl $19, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.195:
	movb $200, -493(%rbp)
	movb -493(%rbp), %r10b
	movb %r10b, -170(%rbp)
	movl $1234488, -500(%rbp)
	negl -500(%rbp)
	movl -500(%rbp), %r10d
	movl %r10d, -504(%rbp)
	movl -504(%rbp), %edi
	call int_to_uchar
	movb %al, -505(%rbp)
	movzbl -505(%rbp), %r11d
	movl %r11d, -512(%rbp)
	movzbl -170(%rbp), %r11d
	movl %r11d, -516(%rbp)
	movl -516(%rbp), %r10d
	cmpl %r10d, -512(%rbp)
	movl $0, -520(%rbp)
	setNE -520(%rbp)
	movl -520(%rbp), %r10d
	movl %r10d, -524(%rbp)
	cmpl $0, -524(%rbp)
	jE .Ltmp.204
	movl $20, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.204:
	movl $4293732808, -528(%rbp)
	movl -528(%rbp), %r10d
	movl %r10d, -532(%rbp)
	movl -532(%rbp), %edi
	call uint_to_uchar
	movb %al, -533(%rbp)
	movzbl -533(%rbp), %r11d
	movl %r11d, -540(%rbp)
	movzbl -170(%rbp), %r11d
	movl %r11d, -544(%rbp)
	movl -544(%rbp), %r10d
	cmpl %r10d, -540(%rbp)
	movl $0, -548(%rbp)
	setNE -548(%rbp)
	movl -548(%rbp), %r10d
	movl %r10d, -552(%rbp)
	cmpl $0, -552(%rbp)
	jE .Ltmp.212
	movl $21, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.212:
	movq $36283884951096, %r10
	movq %r10, -560(%rbp)
	negq -560(%rbp)
	movq -560(%rbp), %r10
	movq %r10, -568(%rbp)
	movq -568(%rbp), %rdi
	call long_to_uchar
	movb %al, -569(%rbp)
	movzbl -569(%rbp), %r11d
	movl %r11d, -576(%rbp)
	movzbl -170(%rbp), %r11d
	movl %r11d, -580(%rbp)
	movl -580(%rbp), %r10d
	cmpl %r10d, -576(%rbp)
	movl $0, -584(%rbp)
	setNE -584(%rbp)
	movl -584(%rbp), %r10d
	movl %r10d, -588(%rbp)
	cmpl $0, -588(%rbp)
	jE .Ltmp.220
	movl $22, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.220:
	movq $9224497936761618632, %r10
	movq %r10, -600(%rbp)
	movq -600(%rbp), %rdi
	call ulong_to_uchar
	movb %al, -601(%rbp)
	movzbl -601(%rbp), %r11d
	movl %r11d, -608(%rbp)
	movzbl -170(%rbp), %r11d
	movl %r11d, -612(%rbp)
	movl -612(%rbp), %r10d
	cmpl %r10d, -608(%rbp)
	movl $0, -616(%rbp)
	setNE -616(%rbp)
	movl -616(%rbp), %r10d
	movl %r10d, -620(%rbp)
	cmpl $0, -620(%rbp)
	jE .Ltmp.227
	movl $23, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.227:
	movsd tmp.258(%rip), %xmm14
	movsd %xmm14, -632(%rbp)
	movsd -632(%rbp), %xmm0
	call double_to_uchar
	movb %al, -633(%rbp)
	movzbl -633(%rbp), %r11d
	movl %r11d, -640(%rbp)
	movzbl -170(%rbp), %r11d
	movl %r11d, -644(%rbp)
	movl -644(%rbp), %r10d
	cmpl %r10d, -640(%rbp)
	movl $0, -648(%rbp)
	setNE -648(%rbp)
	movl -648(%rbp), %r10d
	movl %r10d, -652(%rbp)
	cmpl $0, -652(%rbp)
	jE .Ltmp.234
	movl $24, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.234:
	movb null_ptr.34(%rip), %r10b
	movb %r10b, -653(%rbp)
	movb -653(%rbp), %r10b
	movb %r10b, -654(%rbp)
	movb -654(%rbp), %r10b
	movb %r10b, -655(%rbp)
	cmpb $0, -655(%rbp)
	jE .Ltmp.237
	movl $25, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.237:
	movb $32, -656(%rbp)
	movb -656(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movsbq -2(%rbp), %r11
	movq %r11, -664(%rbp)
	movq -664(%rbp), %r10
	movq %r10, -672(%rbp)
	movb -672(%rbp), %r10b
	movb %r10b, -673(%rbp)
	movsbl -673(%rbp), %r11d
	movl %r11d, -680(%rbp)
	movsbl -2(%rbp), %r11d
	movl %r11d, -684(%rbp)
	movl -684(%rbp), %r10d
	cmpl %r10d, -680(%rbp)
	movl $0, -688(%rbp)
	setNE -688(%rbp)
	movl -688(%rbp), %r10d
	movl %r10d, -692(%rbp)
	cmpl $0, -692(%rbp)
	jE .Ltmp.245
	movl $26, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.245:
	movb $300, -693(%rbp)
	movsbl -693(%rbp), %r11d
	movl %r11d, -700(%rbp)
	movb $44, -701(%rbp)
	movsbl -701(%rbp), %r11d
	movl %r11d, -708(%rbp)
	movl -708(%rbp), %r10d
	cmpl %r10d, -700(%rbp)
	movl $0, -712(%rbp)
	setNE -712(%rbp)
	movl -712(%rbp), %r10d
	movl %r10d, -716(%rbp)
	cmpl $0, -716(%rbp)
	jE .Ltmp.252
	movl $27, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.252:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.bss
	.align 8
null_ptr.34:
	.zero 8
	.section	.note.GNU-stack,"",@progbits
