	.file	"util.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Expected %d but found %d\n"
	.text
	.globl	check_one_int
	.type	check_one_int, @function
check_one_int:
	cmpl	%esi, %edi
	jne	.L6
	movl	$0, %eax
	ret
.L6:
	subq	$8, %rsp
	movl	%edi, %ecx
	movl	%esi, %edx
	leaq	.LC0(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_int, .-check_one_int
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"Expected argument %d to have value %d, actual value was %d\n"
	.text
	.globl	check_5_ints
	.type	check_5_ints, @function
check_5_ints:
	subq	$40, %rsp
	movq	%fs:40, %rax
	movq	%rax, 24(%rsp)
	xorl	%eax, %eax
	movl	%edi, (%rsp)
	movl	%esi, 4(%rsp)
	movl	%edx, 8(%rsp)
	movl	%ecx, 12(%rsp)
	movl	%r8d, 16(%rsp)
.L9:
	movl	(%rsp,%rax,4), %r8d
	cmpl	%r9d, %r8d
	jne	.L13
	addq	$1, %rax
	addl	$1, %r9d
	cmpq	$5, %rax
	jne	.L9
	movq	24(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L14
	movl	$0, %eax
	addq	$40, %rsp
	ret
.L13:
	movl	%r9d, %ecx
	movl	%eax, %edx
	leaq	.LC1(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L14:
	call	__stack_chk_fail@PLT
	.size	check_5_ints, .-check_5_ints
	.globl	check_12_ints
	.type	check_12_ints, @function
check_12_ints:
	subq	$72, %rsp
	movq	%fs:40, %rax
	movq	%rax, 56(%rsp)
	xorl	%eax, %eax
	movl	%edi, (%rsp)
	movl	%esi, 4(%rsp)
	movl	%edx, 8(%rsp)
	movl	%ecx, 12(%rsp)
	movl	%r8d, 16(%rsp)
	movl	%r9d, 20(%rsp)
	movl	80(%rsp), %eax
	movl	%eax, 24(%rsp)
	movl	88(%rsp), %eax
	movl	%eax, 28(%rsp)
	movl	96(%rsp), %eax
	movl	%eax, 32(%rsp)
	movl	104(%rsp), %eax
	movl	%eax, 36(%rsp)
	movl	112(%rsp), %eax
	movl	%eax, 40(%rsp)
	movl	120(%rsp), %eax
	movl	%eax, 44(%rsp)
	movl	128(%rsp), %ecx
	movl	$0, %eax
.L17:
	movl	(%rsp,%rax,4), %r8d
	cmpl	%ecx, %r8d
	jne	.L21
	addq	$1, %rax
	addl	$1, %ecx
	cmpq	$12, %rax
	jne	.L17
	movq	56(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L22
	movl	$0, %eax
	addq	$72, %rsp
	ret
.L21:
	movl	%eax, %edx
	leaq	.LC1(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L22:
	call	__stack_chk_fail@PLT
	.size	check_12_ints, .-check_12_ints
	.section	.rodata.str1.1
.LC2:
	.string	"Expected %c but found %c\n"
	.text
	.globl	check_one_uchar
	.type	check_one_uchar, @function
check_one_uchar:
	cmpb	%sil, %dil
	jne	.L28
	movl	$0, %eax
	ret
.L28:
	subq	$8, %rsp
	movzbl	%dil, %ecx
	movzbl	%sil, %edx
	leaq	.LC2(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_uchar, .-check_one_uchar
	.section	.rodata.str1.1
.LC3:
	.string	"Expected %u but found %u\n"
	.text
	.globl	check_one_uint
	.type	check_one_uint, @function
check_one_uint:
	cmpl	%esi, %edi
	jne	.L34
	movl	$0, %eax
	ret
.L34:
	subq	$8, %rsp
	movl	%edi, %ecx
	movl	%esi, %edx
	leaq	.LC3(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_uint, .-check_one_uint
	.section	.rodata.str1.1
.LC4:
	.string	"Expected %ld but found %ld\n"
	.text
	.globl	check_one_long
	.type	check_one_long, @function
check_one_long:
	cmpq	%rsi, %rdi
	jne	.L40
	movl	$0, %eax
	ret
.L40:
	subq	$8, %rsp
	movq	%rdi, %rcx
	movq	%rsi, %rdx
	leaq	.LC4(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_long, .-check_one_long
	.section	.rodata.str1.1
.LC5:
	.string	"Expected %lu but found %lu\n"
	.text
	.globl	check_one_ulong
	.type	check_one_ulong, @function
check_one_ulong:
	cmpq	%rsi, %rdi
	jne	.L46
	movl	$0, %eax
	ret
.L46:
	subq	$8, %rsp
	movq	%rdi, %rcx
	movq	%rsi, %rdx
	leaq	.LC5(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_ulong, .-check_one_ulong
	.section	.rodata.str1.1
.LC6:
	.string	"Expected %f but found %f\n"
	.text
	.globl	check_one_double
	.type	check_one_double, @function
check_one_double:
	movapd	%xmm1, %xmm2
	ucomisd	%xmm1, %xmm0
	jp	.L50
	jne	.L50
	movl	$0, %eax
	ret
.L50:
	subq	$8, %rsp
	movapd	%xmm0, %xmm1
	movapd	%xmm2, %xmm0
	leaq	.LC6(%rip), %rsi
	movl	$2, %edi
	movl	$2, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
	.size	check_one_double, .-check_one_double
	.section	.rodata.str1.8
	.align 8
.LC7:
	.string	"Expected argument %d to have value %ld, actual value was %ld\n"
	.text
	.globl	check_12_longs
	.type	check_12_longs, @function
check_12_longs:
	subq	$120, %rsp
	movq	176(%rsp), %rax
	movq	%fs:40, %r10
	movq	%r10, 104(%rsp)
	xorl	%r10d, %r10d
	movq	%rdi, (%rsp)
	movq	%rsi, 8(%rsp)
	movq	%rdx, 16(%rsp)
	movq	%rcx, 24(%rsp)
	movq	%r8, 32(%rsp)
	movq	%r9, 40(%rsp)
	movq	128(%rsp), %rdx
	movq	%rdx, 48(%rsp)
	movq	136(%rsp), %rdx
	movq	%rdx, 56(%rsp)
	movq	144(%rsp), %rdx
	movq	%rdx, 64(%rsp)
	movq	152(%rsp), %rdx
	movq	%rdx, 72(%rsp)
	movq	160(%rsp), %rdx
	movq	%rdx, 80(%rsp)
	movq	168(%rsp), %rdx
	movq	%rdx, 88(%rsp)
	movq	%rax, %rcx
	negq	%rax
	leaq	(%rsp,%rax,8), %rax
	movl	$0, %edx
.L55:
	movq	(%rax,%rcx,8), %r8
	cmpq	%rcx, %r8
	jne	.L59
	addl	$1, %edx
	addq	$1, %rcx
	cmpl	$12, %edx
	jne	.L55
	movq	104(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L60
	movl	$0, %eax
	addq	$120, %rsp
	ret
.L59:
	leaq	.LC7(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L60:
	call	__stack_chk_fail@PLT
	.size	check_12_longs, .-check_12_longs
	.globl	check_six_chars
	.type	check_six_chars, @function
check_six_chars:
	subq	$24, %rsp
	movq	%fs:40, %rax
	movq	%rax, 8(%rsp)
	xorl	%eax, %eax
	movb	%dil, 2(%rsp)
	movb	%sil, 3(%rsp)
	movb	%dl, 4(%rsp)
	movb	%cl, 5(%rsp)
	movb	%r8b, 6(%rsp)
	movb	%r9b, 7(%rsp)
	movl	32(%rsp), %ecx
	leaq	2(%rsp), %rdx
.L63:
	movsbl	(%rax,%rdx), %r8d
	cmpl	%ecx, %r8d
	jne	.L67
	addq	$1, %rax
	addl	$1, %ecx
	cmpq	$6, %rax
	jne	.L63
	movq	8(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L68
	movl	$0, %eax
	addq	$24, %rsp
	ret
.L67:
	movl	%eax, %edx
	leaq	.LC1(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L68:
	call	__stack_chk_fail@PLT
	.size	check_six_chars, .-check_six_chars
	.section	.rodata.str1.8
	.align 8
.LC8:
	.string	"Expected argument %d to have value %f, actual value was %f\n"
	.text
	.globl	check_14_doubles
	.type	check_14_doubles, @function
check_14_doubles:
	subq	$136, %rsp
	movsd	192(%rsp), %xmm8
	movq	%fs:40, %rax
	movq	%rax, 120(%rsp)
	xorl	%eax, %eax
	movsd	%xmm0, (%rsp)
	movsd	%xmm1, 8(%rsp)
	movsd	%xmm2, 16(%rsp)
	movsd	%xmm3, 24(%rsp)
	movsd	%xmm4, 32(%rsp)
	movsd	%xmm5, 40(%rsp)
	movsd	%xmm6, 48(%rsp)
	movsd	%xmm7, 56(%rsp)
	movsd	144(%rsp), %xmm0
	movsd	%xmm0, 64(%rsp)
	movsd	152(%rsp), %xmm0
	movsd	%xmm0, 72(%rsp)
	movsd	160(%rsp), %xmm0
	movsd	%xmm0, 80(%rsp)
	movsd	168(%rsp), %xmm0
	movsd	%xmm0, 88(%rsp)
	movsd	176(%rsp), %xmm0
	movsd	%xmm0, 96(%rsp)
	movsd	184(%rsp), %xmm0
	movsd	%xmm0, 104(%rsp)
.L72:
	movl	%eax, %edx
	pxor	%xmm0, %xmm0
	cvtsi2sdl	%eax, %xmm0
	addsd	%xmm8, %xmm0
	movsd	(%rsp,%rax,8), %xmm1
	ucomisd	%xmm0, %xmm1
	jp	.L74
	jne	.L74
	addq	$1, %rax
	cmpq	$14, %rax
	jne	.L72
	movq	120(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L77
	movl	$0, %eax
	addq	$136, %rsp
	ret
.L74:
	leaq	.LC8(%rip), %rsi
	movl	$2, %edi
	movl	$2, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L77:
	call	__stack_chk_fail@PLT
	.size	check_14_doubles, .-check_14_doubles
	.section	.rodata.str1.8
	.align 8
.LC9:
	.string	"Expected *k to point to have value %d, actual value was %ld\n"
	.align 8
.LC10:
	.string	"Expected *l to point to have value %d, actual value was %f\n"
	.text
	.globl	check_12_vals
	.type	check_12_vals, @function
check_12_vals:
	pushq	%rbx
	subq	$48, %rsp
	movl	%edi, %r11d
	movl	%edx, %eax
	movq	96(%rsp), %r10
	movq	104(%rsp), %rdi
	movl	112(%rsp), %edx
	movq	%fs:40, %rbx
	movq	%rbx, 40(%rsp)
	xorl	%ebx, %ebx
	movl	%r11d, (%rsp)
	movl	%esi, 4(%rsp)
	movl	%eax, 8(%rsp)
	movl	%ecx, 12(%rsp)
	movl	%r8d, 16(%rsp)
	movl	%r9d, 20(%rsp)
	movl	64(%rsp), %eax
	movl	%eax, 24(%rsp)
	movl	72(%rsp), %eax
	movl	%eax, 28(%rsp)
	movl	80(%rsp), %eax
	movl	%eax, 32(%rsp)
	movl	88(%rsp), %eax
	movl	%eax, 36(%rsp)
	movl	%edx, %ecx
	movl	$0, %eax
.L80:
	movl	(%rsp,%rax,4), %r8d
	cmpl	%ecx, %r8d
	jne	.L88
	addq	$1, %rax
	addl	$1, %ecx
	cmpq	$10, %rax
	jne	.L80
	movq	(%r10), %rcx
	leal	10(%rdx), %eax
	movslq	%eax, %rsi
	cmpq	%rsi, %rcx
	jne	.L89
	movsd	(%rdi), %xmm0
	addl	$11, %edx
	pxor	%xmm1, %xmm1
	cvtsi2sdl	%edx, %xmm1
	ucomisd	%xmm1, %xmm0
	jp	.L85
	jne	.L85
	movq	40(%rsp), %rax
	subq	%fs:40, %rax
	jne	.L90
	movl	$0, %eax
	addq	$48, %rsp
	popq	%rbx
	ret
.L88:
	movl	%eax, %edx
	leaq	.LC1(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L89:
	movl	%eax, %edx
	leaq	.LC9(%rip), %rsi
	movl	$2, %edi
	movl	$0, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L85:
	leaq	.LC10(%rip), %rsi
	movl	$2, %edi
	movl	$1, %eax
	call	__printf_chk@PLT
	movl	$-1, %edi
	call	exit@PLT
.L90:
	call	__stack_chk_fail@PLT
	.size	check_12_vals, .-check_12_vals
	.globl	id
	.type	id, @function
id:
	movl	%edi, %eax
	ret
	.size	id, .-id
	.globl	dbl_id
	.type	dbl_id, @function
dbl_id:
	ret
	.size	dbl_id, .-dbl_id
	.globl	long_id
	.type	long_id, @function
long_id:
	movq	%rdi, %rax
	ret
	.size	long_id, .-long_id
	.globl	unsigned_id
	.type	unsigned_id, @function
unsigned_id:
	movl	%edi, %eax
	ret
	.size	unsigned_id, .-unsigned_id
	.globl	uchar_id
	.type	uchar_id, @function
uchar_id:
	movl	%edi, %eax
	ret
	.size	uchar_id, .-uchar_id
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
