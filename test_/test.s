	.globl validate_stack_bytes
	.text
validate_stack_bytes:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl %edi, -4(%rbp)
	leaq to_validate+0(%rip), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	leaq tmp.43+0(%rip), %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movq -24(%rbp), %rdi
	movq -40(%rbp), %rsi
	call strcmp
	movl %eax, -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.48
	movl -4(%rbp), %r10d
	movl %r10d, -52(%rbp)
	movl -52(%rbp), %edi
	call exit
.Ltmp.48:
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_int_struct
	.text
return_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movb $0, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -8(%rbp)
	movb $0, -9(%rbp)
	movb -9(%rbp), %r10b
	movb %r10b, -7(%rbp)
	movb $0, -10(%rbp)
	movb -10(%rbp), %r10b
	movb %r10b, -6(%rbp)
	movb $0, -11(%rbp)
	movb -11(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb $0, -12(%rbp)
	movb -12(%rbp), %r10b
	movb %r10b, -4(%rbp)
	movb $0, -13(%rbp)
	movb -13(%rbp), %r10b
	movb %r10b, -3(%rbp)
	movb $0, -14(%rbp)
	movb -14(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movb -2(%rbp), %al
	shl $8, %rax
	movb -3(%rbp), %al
	shl $8, %rax
	movb -4(%rbp), %al
	shl $8, %rax
	movb -5(%rbp), %al
	shl $8, %rax
	movb -6(%rbp), %al
	shl $8, %rax
	movb -7(%rbp), %al
	shl $8, %rax
	movb -8(%rbp), %al
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl validate_one_int_struct
	.text
validate_one_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $80, %rsp
	movl %edi, -4(%rbp)
	movl $0, -8(%rbp)
.Ltmp.57:
	cmpl $7, -8(%rbp)
	movl $0, -12(%rbp)
	setL -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.37
	leaq one_int_struct+0(%rip), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movslq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -32(%rbp), %rax
	movq -48(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -57(%rbp)
	movb -57(%rbp), %r10b
	movb %r10b, -58(%rbp)
	cmpb $0, -58(%rbp)
	jE .Ltmp.67
	movl -4(%rbp), %r10d
	movl %r10d, -64(%rbp)
	movl -64(%rbp), %edi
	call exit
.Ltmp.67:
.Lcontinue_tmp.37:
	movl -8(%rbp), %r10d
	movl %r10d, -68(%rbp)
	addl $1, -68(%rbp)
	movl -68(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.57
.Lbreak_tmp.37:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_int_struct
	.text
test_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	call return_int_struct
	movb %al, -23(%rbp)
	shr $8, %rax
	movb %al, -22(%rbp)
	shr $8, %rax
	movb %al, -21(%rbp)
	shr $8, %rax
	movb %al, -20(%rbp)
	shr $8, %rax
	movb %al, -19(%rbp)
	shr $8, %rax
	movb %al, -18(%rbp)
	shr $8, %rax
	movb %al, -17(%rbp)
	movl -23(%rbp), %r10d
	movl %r10d, one_int_struct+0(%rip)
	movb -19(%rbp), %r10b
	movb %r10b, one_int_struct+4(%rip)
	movb -18(%rbp), %r10b
	movb %r10b, one_int_struct+5(%rip)
	movb -17(%rbp), %r10b
	movb %r10b, one_int_struct+6(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $1, -28(%rbp)
	movl -28(%rbp), %edi
	call validate_stack_bytes
	movl $2, -32(%rbp)
	movl -32(%rbp), %edi
	call validate_one_int_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_two_int_struct
	.text
return_two_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movb $20, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -16(%rbp)
	movb $21, -17(%rbp)
	movb -17(%rbp), %r10b
	movb %r10b, -15(%rbp)
	movb $22, -18(%rbp)
	movb -18(%rbp), %r10b
	movb %r10b, -14(%rbp)
	movb $23, -19(%rbp)
	movb -19(%rbp), %r10b
	movb %r10b, -13(%rbp)
	movb $24, -20(%rbp)
	movb -20(%rbp), %r10b
	movb %r10b, -12(%rbp)
	movb $25, -21(%rbp)
	movb -21(%rbp), %r10b
	movb %r10b, -11(%rbp)
	movb $26, -22(%rbp)
	movb -22(%rbp), %r10b
	movb %r10b, -10(%rbp)
	movb $27, -23(%rbp)
	movb -23(%rbp), %r10b
	movb %r10b, -9(%rbp)
	movb $28, -24(%rbp)
	movb -24(%rbp), %r10b
	movb %r10b, -8(%rbp)
	movb $29, -25(%rbp)
	movb -25(%rbp), %r10b
	movb %r10b, -7(%rbp)
	movb $30, -26(%rbp)
	movb -26(%rbp), %r10b
	movb %r10b, -6(%rbp)
	movb $31, -27(%rbp)
	movb -27(%rbp), %r10b
	movb %r10b, -5(%rbp)
	movb $32, -28(%rbp)
	movb -28(%rbp), %r10b
	movb %r10b, -4(%rbp)
	movb $33, -29(%rbp)
	movb -29(%rbp), %r10b
	movb %r10b, -3(%rbp)
	movb $34, -30(%rbp)
	movb -30(%rbp), %r10b
	movb %r10b, -2(%rbp)
	movq -16(%rbp), %rax
	movb -2(%rbp), %dl
	shl $8, %rdx
	movb -3(%rbp), %dl
	shl $8, %rdx
	movb -4(%rbp), %dl
	shl $8, %rdx
	movb -5(%rbp), %dl
	shl $8, %rdx
	movb -6(%rbp), %dl
	shl $8, %rdx
	movb -7(%rbp), %dl
	shl $8, %rdx
	movb -8(%rbp), %dl
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl validate_two_int_struct
	.text
validate_two_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movl %edi, -4(%rbp)
	movl $0, -8(%rbp)
.Ltmp.88:
	cmpl $15, -8(%rbp)
	movl $0, -12(%rbp)
	setL -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.38
	leaq two_int_struct+0(%rip), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movslq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -32(%rbp), %rax
	movq -48(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -57(%rbp)
	movsbl -57(%rbp), %r11d
	movl %r11d, -64(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -68(%rbp)
	addl $20, -68(%rbp)
	movl -68(%rbp), %r10d
	cmpl %r10d, -64(%rbp)
	movl $0, -72(%rbp)
	setNE -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	cmpl $0, -76(%rbp)
	jE .Ltmp.101
	movl -4(%rbp), %r10d
	movl %r10d, -80(%rbp)
	movl -80(%rbp), %edi
	call exit
.Ltmp.101:
.Lcontinue_tmp.38:
	movl -8(%rbp), %r10d
	movl %r10d, -84(%rbp)
	addl $1, -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.88
.Lbreak_tmp.38:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_two_int_struct
	.text
test_two_int_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	call return_two_int_struct
	movq %rax, -31(%rbp)
	movb %dl, -23(%rbp)
	shr $8, %rdx
	movb %dl, -22(%rbp)
	shr $8, %rdx
	movb %dl, -21(%rbp)
	shr $8, %rdx
	movb %dl, -20(%rbp)
	shr $8, %rdx
	movb %dl, -19(%rbp)
	shr $8, %rdx
	movb %dl, -18(%rbp)
	shr $8, %rdx
	movb %dl, -17(%rbp)
	movq -31(%rbp), %r10
	movq %r10, two_int_struct+0(%rip)
	movl -23(%rbp), %r10d
	movl %r10d, two_int_struct+8(%rip)
	movb -19(%rbp), %r10b
	movb %r10b, two_int_struct+12(%rip)
	movb -18(%rbp), %r10b
	movb %r10b, two_int_struct+13(%rip)
	movb -17(%rbp), %r10b
	movb %r10b, two_int_struct+14(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $3, -36(%rbp)
	movl -36(%rbp), %edi
	call validate_stack_bytes
	movl $4, -40(%rbp)
	movl -40(%rbp), %edi
	call validate_two_int_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.235:
	.double 234.5
	.globl return_one_xmm_struct
	.text
return_one_xmm_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd tmp.235+0(%rip), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd -8(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.236:
	.double 234.5
	.globl validate_one_double_struct
	.text
validate_one_double_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movl %edi, -4(%rbp)
	movsd one_double_struct+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd -16(%rbp), %xmm15
	comisd tmp.236+0(%rip), %xmm15
	movl $0, -20(%rbp)
	setNE -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Ltmp.110
	movl -4(%rbp), %r10d
	movl %r10d, -28(%rbp)
	movl -28(%rbp), %edi
	call exit
.Ltmp.110:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_one_double_struct
	.text
test_one_double_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	call return_one_xmm_struct
	movsd %xmm0, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, one_double_struct+0(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $5, -28(%rbp)
	movl -28(%rbp), %edi
	call validate_stack_bytes
	movl $6, -32(%rbp)
	movl -32(%rbp), %edi
	call validate_one_double_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.237:
	.double 234.5
	.section .rodata
	.align 8
tmp.238:
	.double 678.25
	.globl return_two_xmm_struct
	.text
return_two_xmm_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd tmp.237+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd tmp.238+0(%rip), %xmm14
	movsd %xmm14, -8(%rbp)
	movsd -16(%rbp), %xmm0
	movsd -8(%rbp), %xmm1
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.239:
	.double 234.5
	.section .rodata
	.align 8
tmp.240:
	.double 678.25
	.globl validate_two_doubles_struct
	.text
validate_two_doubles_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl %edi, -4(%rbp)
	movsd two_doubles_struct+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movsd -16(%rbp), %xmm15
	comisd tmp.239+0(%rip), %xmm15
	movl $0, -20(%rbp)
	setNE -20(%rbp)
	cmpl $0, -20(%rbp)
	jNE .Ltmp.117
	movsd two_doubles_struct+8(%rip), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd -32(%rbp), %xmm15
	comisd tmp.240+0(%rip), %xmm15
	movl $0, -36(%rbp)
	setNE -36(%rbp)
	cmpl $0, -36(%rbp)
	jNE .Ltmp.117
	movl $0, -40(%rbp)
	jmp .Ltmp.121
.Ltmp.117:
	movl $1, -40(%rbp)
.Ltmp.121:
	movl -40(%rbp), %r10d
	movl %r10d, -44(%rbp)
	cmpl $0, -44(%rbp)
	jE .Ltmp.123
	movl -4(%rbp), %r10d
	movl %r10d, -48(%rbp)
	movl -48(%rbp), %edi
	call exit
.Ltmp.123:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_two_doubles_struct
	.text
test_two_doubles_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	call return_two_xmm_struct
	movsd %xmm0, -32(%rbp)
	movsd %xmm1, -24(%rbp)
	movq -32(%rbp), %r10
	movq %r10, two_doubles_struct+0(%rip)
	movq -24(%rbp), %r10
	movq %r10, two_doubles_struct+8(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $7, -36(%rbp)
	movl -36(%rbp), %edi
	call validate_stack_bytes
	movl $8, -40(%rbp)
	movl -40(%rbp), %edi
	call validate_two_doubles_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.241:
	.double 678.25
	.globl return_mixed_struct
	.text
return_mixed_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $32, %rsp
	movb $125, -1(%rbp)
	movb -1(%rbp), %r10b
	movb %r10b, -24(%rbp)
	movsd tmp.241+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	movq -24(%rbp), %rax
	movsd -16(%rbp), %xmm0
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.242:
	.double 678.25
	.globl validate_mixed_struct
	.text
validate_mixed_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl %edi, -4(%rbp)
	movb mixed_struct+0(%rip), %r10b
	movb %r10b, -5(%rbp)
	movsbl -5(%rbp), %r11d
	movl %r11d, -12(%rbp)
	cmpl $125, -12(%rbp)
	movl $0, -16(%rbp)
	setNE -16(%rbp)
	cmpl $0, -16(%rbp)
	jNE .Ltmp.132
	movsd mixed_struct+8(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd -24(%rbp), %xmm15
	comisd tmp.242+0(%rip), %xmm15
	movl $0, -28(%rbp)
	setNE -28(%rbp)
	cmpl $0, -28(%rbp)
	jNE .Ltmp.132
	movl $0, -32(%rbp)
	jmp .Ltmp.136
.Ltmp.132:
	movl $1, -32(%rbp)
.Ltmp.136:
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.138
	movl -4(%rbp), %r10d
	movl %r10d, -40(%rbp)
	movl -40(%rbp), %edi
	call exit
.Ltmp.138:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_mixed_struct
	.text
test_mixed_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	call return_mixed_struct
	movq %rax, -32(%rbp)
	movsd %xmm0, -24(%rbp)
	movq -32(%rbp), %r10
	movq %r10, mixed_struct+0(%rip)
	movq -24(%rbp), %r10
	movq %r10, mixed_struct+8(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $9, -36(%rbp)
	movl -36(%rbp), %edi
	call validate_stack_bytes
	movl $10, -40(%rbp)
	movl -40(%rbp), %edi
	call validate_mixed_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_stack_struct
	.text
return_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movq %rdi, -8(%rbp)
	movb $90, -9(%rbp)
	movb -9(%rbp), %r10b
	movb %r10b, -37(%rbp)
	movb $91, -38(%rbp)
	movb -38(%rbp), %r10b
	movb %r10b, -36(%rbp)
	movb $92, -39(%rbp)
	movb -39(%rbp), %r10b
	movb %r10b, -35(%rbp)
	movb $93, -40(%rbp)
	movb -40(%rbp), %r10b
	movb %r10b, -34(%rbp)
	movb $94, -41(%rbp)
	movb -41(%rbp), %r10b
	movb %r10b, -33(%rbp)
	movb $95, -42(%rbp)
	movb -42(%rbp), %r10b
	movb %r10b, -32(%rbp)
	movb $96, -43(%rbp)
	movb -43(%rbp), %r10b
	movb %r10b, -31(%rbp)
	movb $97, -44(%rbp)
	movb -44(%rbp), %r10b
	movb %r10b, -30(%rbp)
	movb $98, -45(%rbp)
	movb -45(%rbp), %r10b
	movb %r10b, -29(%rbp)
	movb $99, -46(%rbp)
	movb -46(%rbp), %r10b
	movb %r10b, -28(%rbp)
	movb $100, -47(%rbp)
	movb -47(%rbp), %r10b
	movb %r10b, -27(%rbp)
	movb $101, -48(%rbp)
	movb -48(%rbp), %r10b
	movb %r10b, -26(%rbp)
	movb $102, -49(%rbp)
	movb -49(%rbp), %r10b
	movb %r10b, -25(%rbp)
	movb $103, -50(%rbp)
	movb -50(%rbp), %r10b
	movb %r10b, -24(%rbp)
	movb $104, -51(%rbp)
	movb -51(%rbp), %r10b
	movb %r10b, -23(%rbp)
	movb $105, -52(%rbp)
	movb -52(%rbp), %r10b
	movb %r10b, -22(%rbp)
	movb $106, -53(%rbp)
	movb -53(%rbp), %r10b
	movb %r10b, -21(%rbp)
	movb $107, -54(%rbp)
	movb -54(%rbp), %r10b
	movb %r10b, -20(%rbp)
	movb $108, -55(%rbp)
	movb -55(%rbp), %r10b
	movb %r10b, -19(%rbp)
	movb $109, -56(%rbp)
	movb -56(%rbp), %r10b
	movb %r10b, -18(%rbp)
	movb $110, -57(%rbp)
	movb -57(%rbp), %r10b
	movb %r10b, -17(%rbp)
	movb $111, -58(%rbp)
	movb -58(%rbp), %r10b
	movb %r10b, -16(%rbp)
	movb $112, -59(%rbp)
	movb -59(%rbp), %r10b
	movb %r10b, -15(%rbp)
	movb $113, -60(%rbp)
	movb -60(%rbp), %r10b
	movb %r10b, -14(%rbp)
	movb $114, -61(%rbp)
	movb -61(%rbp), %r10b
	movb %r10b, -13(%rbp)
	movb $115, -62(%rbp)
	movb -62(%rbp), %r10b
	movb %r10b, -12(%rbp)
	movb $116, -63(%rbp)
	movb -63(%rbp), %r10b
	movb %r10b, -11(%rbp)
	movb $117, -64(%rbp)
	movb -64(%rbp), %r10b
	movb %r10b, -10(%rbp)
	movq -8(%rbp), %rax
	movq -37(%rbp), %r10
	movq %r10, 0(%rax)
	movq -29(%rbp), %r10
	movq %r10, 8(%rax)
	movq -21(%rbp), %r10
	movq %r10, 16(%rax)
	movl -13(%rbp), %r10d
	movl %r10d, 24(%rax)
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl validate_stack_struct
	.text
validate_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movl %edi, -4(%rbp)
	movl $0, -8(%rbp)
.Ltmp.171:
	cmpl $28, -8(%rbp)
	movl $0, -12(%rbp)
	setL -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.39
	leaq stack_struct+0(%rip), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movslq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -32(%rbp), %rax
	movq -48(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -57(%rbp)
	movsbl -57(%rbp), %r11d
	movl %r11d, -64(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -68(%rbp)
	addl $90, -68(%rbp)
	movl -68(%rbp), %r10d
	cmpl %r10d, -64(%rbp)
	movl $0, -72(%rbp)
	setNE -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	cmpl $0, -76(%rbp)
	jE .Ltmp.184
	movl -4(%rbp), %r10d
	movl %r10d, -80(%rbp)
	movl -80(%rbp), %edi
	call exit
.Ltmp.184:
.Lcontinue_tmp.39:
	movl -8(%rbp), %r10d
	movl %r10d, -84(%rbp)
	addl $1, -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.171
.Lbreak_tmp.39:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_stack_struct
	.text
test_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	leaq -44(%rbp), %rdi
	call return_stack_struct
	movq -44(%rbp), %r10
	movq %r10, stack_struct+0(%rip)
	movq -36(%rbp), %r10
	movq %r10, stack_struct+8(%rip)
	movq -28(%rbp), %r10
	movq %r10, stack_struct+16(%rip)
	movl -20(%rbp), %r10d
	movl %r10d, stack_struct+24(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $11, -48(%rbp)
	movl -48(%rbp), %edi
	call validate_stack_bytes
	movl $12, -52(%rbp)
	movl -52(%rbp), %edi
	call validate_stack_struct
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_irregular_stack_struct
	.text
return_irregular_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movq %rdi, -8(%rbp)
	movb $70, -9(%rbp)
	movb -9(%rbp), %r10b
	movb %r10b, -28(%rbp)
	movb $71, -29(%rbp)
	movb -29(%rbp), %r10b
	movb %r10b, -27(%rbp)
	movb $72, -30(%rbp)
	movb -30(%rbp), %r10b
	movb %r10b, -26(%rbp)
	movb $73, -31(%rbp)
	movb -31(%rbp), %r10b
	movb %r10b, -25(%rbp)
	movb $74, -32(%rbp)
	movb -32(%rbp), %r10b
	movb %r10b, -24(%rbp)
	movb $75, -33(%rbp)
	movb -33(%rbp), %r10b
	movb %r10b, -23(%rbp)
	movb $76, -34(%rbp)
	movb -34(%rbp), %r10b
	movb %r10b, -22(%rbp)
	movb $77, -35(%rbp)
	movb -35(%rbp), %r10b
	movb %r10b, -21(%rbp)
	movb $78, -36(%rbp)
	movb -36(%rbp), %r10b
	movb %r10b, -20(%rbp)
	movb $79, -37(%rbp)
	movb -37(%rbp), %r10b
	movb %r10b, -19(%rbp)
	movb $80, -38(%rbp)
	movb -38(%rbp), %r10b
	movb %r10b, -18(%rbp)
	movb $81, -39(%rbp)
	movb -39(%rbp), %r10b
	movb %r10b, -17(%rbp)
	movb $82, -40(%rbp)
	movb -40(%rbp), %r10b
	movb %r10b, -16(%rbp)
	movb $83, -41(%rbp)
	movb -41(%rbp), %r10b
	movb %r10b, -15(%rbp)
	movb $84, -42(%rbp)
	movb -42(%rbp), %r10b
	movb %r10b, -14(%rbp)
	movb $85, -43(%rbp)
	movb -43(%rbp), %r10b
	movb %r10b, -13(%rbp)
	movb $86, -44(%rbp)
	movb -44(%rbp), %r10b
	movb %r10b, -12(%rbp)
	movb $87, -45(%rbp)
	movb -45(%rbp), %r10b
	movb %r10b, -11(%rbp)
	movb $88, -46(%rbp)
	movb -46(%rbp), %r10b
	movb %r10b, -10(%rbp)
	movq -8(%rbp), %rax
	movq -28(%rbp), %r10
	movq %r10, 0(%rax)
	movq -20(%rbp), %r10
	movq %r10, 8(%rax)
	movb -12(%rbp), %r10b
	movb %r10b, 16(%rax)
	movb -11(%rbp), %r10b
	movb %r10b, 17(%rax)
	movb -10(%rbp), %r10b
	movb %r10b, 18(%rax)
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl validate_irregular_stack_struct
	.text
validate_irregular_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $96, %rsp
	movl %edi, -4(%rbp)
	movl $0, -8(%rbp)
.Ltmp.209:
	cmpl $19, -8(%rbp)
	movl $0, -12(%rbp)
	setL -12(%rbp)
	movl -12(%rbp), %r10d
	movl %r10d, -16(%rbp)
	cmpl $0, -16(%rbp)
	jE .Lbreak_tmp.40
	leaq irregular_stack_struct+0(%rip), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movslq -8(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -32(%rbp), %rax
	movq -48(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -57(%rbp)
	movsbl -57(%rbp), %r11d
	movl %r11d, -64(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -68(%rbp)
	addl $70, -68(%rbp)
	movl -68(%rbp), %r10d
	cmpl %r10d, -64(%rbp)
	movl $0, -72(%rbp)
	setNE -72(%rbp)
	movl -72(%rbp), %r10d
	movl %r10d, -76(%rbp)
	cmpl $0, -76(%rbp)
	jE .Ltmp.222
	movl -4(%rbp), %r10d
	movl %r10d, -80(%rbp)
	movl -80(%rbp), %edi
	call exit
.Ltmp.222:
.Lcontinue_tmp.40:
	movl -8(%rbp), %r10d
	movl %r10d, -84(%rbp)
	addl $1, -84(%rbp)
	movl -84(%rbp), %r10d
	movl %r10d, -8(%rbp)
	jmp .Ltmp.209
.Lbreak_tmp.40:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_irregular_stack_struct
	.text
test_irregular_stack_struct:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movb $101, -16(%rbp)
	movb $102, -15(%rbp)
	movb $103, -14(%rbp)
	movb $104, -13(%rbp)
	movb $105, -12(%rbp)
	movb $106, -11(%rbp)
	movb $107, -10(%rbp)
	movb $108, -9(%rbp)
	movb $109, -8(%rbp)
	movb $110, -7(%rbp)
	movb $111, -6(%rbp)
	movb $112, -5(%rbp)
	movb $113, -4(%rbp)
	movb $114, -3(%rbp)
	movb $115, -2(%rbp)
	movb $0, -1(%rbp)
	leaq -35(%rbp), %rdi
	call return_irregular_stack_struct
	movq -35(%rbp), %r10
	movq %r10, irregular_stack_struct+0(%rip)
	movq -27(%rbp), %r10
	movq %r10, irregular_stack_struct+8(%rip)
	movb -19(%rbp), %r10b
	movb %r10b, irregular_stack_struct+16(%rip)
	movb -18(%rbp), %r10b
	movb %r10b, irregular_stack_struct+17(%rip)
	movb -17(%rbp), %r10b
	movb %r10b, irregular_stack_struct+18(%rip)
	movq -16(%rbp), %r10
	movq %r10, to_validate+0(%rip)
	movq -8(%rbp), %r10
	movq %r10, to_validate+8(%rip)
	movl $13, -40(%rbp)
	movl -40(%rbp), %edi
	call validate_stack_bytes
	movl $14, -44(%rbp)
	movl -44(%rbp), %edi
	call validate_irregular_stack_struct
	movl $0, %eax
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
	subq $32, %rsp
	call test_int_struct
	movl %eax, -4(%rbp)
	call test_two_int_struct
	movl %eax, -8(%rbp)
	call test_one_double_struct
	movl %eax, -12(%rbp)
	call test_two_doubles_struct
	movl %eax, -16(%rbp)
	call test_mixed_struct
	movl %eax, -20(%rbp)
	call test_stack_struct
	movl %eax, -24(%rbp)
	call test_irregular_stack_struct
	movl %eax, -28(%rbp)
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.bss
	.align 1
to_validate:
	.zero 16
	.bss
	.align 1
one_int_struct:
	.zero 7
	.bss
	.align 1
two_int_struct:
	.zero 15
	.bss
	.align 8
one_double_struct:
	.zero 8
	.bss
	.align 8
two_doubles_struct:
	.zero 16
	.bss
	.align 8
mixed_struct:
	.zero 16
	.bss
	.align 1
stack_struct:
	.zero 28
	.bss
	.align 1
irregular_stack_struct:
	.zero 19
	.section .rodata
	.align 16
tmp.43:
	.asciz "efghijklmnopqrs"
	.section	.note.GNU-stack,"",@progbits
