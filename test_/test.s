	.globl test_add_constant_to_pointer
	.text
test_add_constant_to_pointer:
	pushq %rbp
	movq %rsp, %rbp
	subq $112, %rsp
	movq $0, -96(%rbp)
	movq $0, -88(%rbp)
	movq $3, -80(%rbp)
	movq $0, -72(%rbp)
	movq $0, -64(%rbp)
	movq $0, -56(%rbp)
	movq $0, -48(%rbp)
	movq $0, -40(%rbp)
	movq $0, -32(%rbp)
	movq $0, -24(%rbp)
	movq $13, -16(%rbp)
	movq $0, -8(%rbp)
	leaq -96(%rbp), %r9
	movq %r9, %rax
	leaq 80(%rax), %r9
	movq %r9, %rax
	movq 0(%rax), %r9
	cmpq $13, %r9
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_add_negative_index
	.text
test_add_negative_index:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl $0, %r9d
	movl %r9d, -48(%rbp)
	movl $0, %r9d
	movl %r9d, -44(%rbp)
	movl $2, %r9d
	movl %r9d, -40(%rbp)
	movl $0, %r9d
	movl %r9d, -36(%rbp)
	movl $0, %r9d
	movl %r9d, -32(%rbp)
	movl $0, %r9d
	movl %r9d, -28(%rbp)
	movl $0, %r9d
	movl %r9d, -24(%rbp)
	movl $0, %r9d
	movl %r9d, -20(%rbp)
	movl $0, %r9d
	movl %r9d, -16(%rbp)
	movl $0, %r9d
	movl %r9d, -12(%rbp)
	movl $42, %r9d
	movl %r9d, -8(%rbp)
	movl $0, -4(%rbp)
	leaq -48(%rbp), %r9
	movq %r9, %rax
	leaq 48(%rax), %r8
	movl $10, %r9d
	negl %r9d
	movslq %r9d, %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 4), %r9
	movq %r9, %rax
	movl 0(%rax), %r8d
	movl $2, %r9d
	cmpl %r9d, %r8d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_add_pointer_to_int
	.text
test_add_pointer_to_int:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl $0, -32(%rbp)
	movl $98, -28(%rbp)
	movl $99, -24(%rbp)
	movl $0, -20(%rbp)
	movl $0, -16(%rbp)
	leaq -32(%rbp), %r9
	movq %r9, %rax
	leaq 8(%rax), %rsi
	leaq -32(%rbp), %r9
	movq %r9, %rax
	leaq 8(%rax), %r8
	cmpq %r8, %rsi
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.103
	movq %r8, %rax
	movl 0(%rax), %r9d
	cmpl $99, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.103
	movl $1, %r9d
	jmp .Ltmp.107
.Ltmp.103:
	movl $0, %r9d
.Ltmp.107:
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.358:
	.double 6.0
	.section .rodata
	.align 8
tmp.359:
	.double 0.0
	.section .rodata
	.align 8
tmp.360:
	.double 0.0
	.section .rodata
	.align 8
tmp.361:
	.double 0.0
	.section .rodata
	.align 8
tmp.362:
	.double 0.0
	.section .rodata
	.align 8
tmp.363:
	.double 0.0
	.section .rodata
	.align 8
tmp.364:
	.double 6.0
	.globl test_add_different_index_types
	.text
test_add_different_index_types:
	pushq %rbp
	movq %rsp, %rbp
	subq $112, %rsp
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -96(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -88(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -80(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -72(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -64(%rbp)
	movsd tmp.358+0(%rip), %xmm14
	movsd %xmm14, -56(%rbp)
	movsd tmp.359+0(%rip), %xmm14
	movsd %xmm14, -48(%rbp)
	movsd tmp.360+0(%rip), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd tmp.361+0(%rip), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd tmp.362+0(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd tmp.363+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	leaq -96(%rbp), %r9
	movq %r9, %rax
	leaq 40(%rax), %rcx
	leaq -96(%rbp), %r9
	movq %r9, %rax
	leaq 40(%rax), %rdi
	leaq -96(%rbp), %r8
	movl $5, %r9d
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %rsi
	leaq -96(%rbp), %r8
	movq $5, %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %r8
	cmpq %rdi, %rcx
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.133
	cmpq %rsi, %rcx
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.133
	movl $1, %r9d
	jmp .Ltmp.136
.Ltmp.133:
	movl $0, %r9d
.Ltmp.136:
	cmpl $0, %r9d
	jE .Ltmp.137
	cmpq %r8, %rcx
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.137
	movl $1, %r9d
	jmp .Ltmp.140
.Ltmp.137:
	movl $0, %r9d
.Ltmp.140:
	cmpl $0, %r9d
	jE .Ltmp.141
	movq %r8, %rax
	movsd 0(%rax), %xmm13
	comisd tmp.364+0(%rip), %xmm13
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.141
	movl $1, %r9d
	jmp .Ltmp.145
.Ltmp.141:
	movl $0, %r9d
.Ltmp.145:
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_add_complex_expressions
	.text
test_add_complex_expressions:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	pushq %rbx
	pushq %r12
	movl $2, %r9d
	negl %r9d
	movl %r9d, -4(%rbp)
	leaq -4(%rbp), %rbx
	cmpl $0, flag.13+0(%rip)
	jE .Ltmp.149
	leaq arr.18+0(%rip), %r9
	movq %r9, %rdi
	call get_elem1_ptr
	movq %rax, %r9
	movq %r9, %r12
	jmp .Ltmp.155
.Ltmp.149:
	leaq arr.18+0(%rip), %r9
	movq %r9, %rdi
	call get_elem2_ptr
	movq %rax, %r9
	movq %r9, %r12
.Ltmp.155:
	call return_one
	movl %eax, %r9d
	movq %rbx, %rax
	movl 0(%rax), %ebx
	addl %ebx, %r9d
	movslq %r9d, %r9
	movq %r12, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 4), %rbx
	leaq arr.18+0(%rip), %r9
	movq %r9, %rax
	leaq 4(%rax), %r9
	cmpq %r9, %rbx
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.173
	movq %rbx, %rax
	movl 0(%rax), %r9d
	cmpl $2, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.173
	movl $1, %r9d
	jmp .Ltmp.177
.Ltmp.173:
	movl $0, %r9d
.Ltmp.177:
	movl %r9d, %eax
	popq %r12
	popq %rbx
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl return_one
	.text
return_one:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl get_elem1_ptr
	.text
get_elem1_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, %r9
	movq %r9, %rax
	leaq 4(%rax), %r9
	movq %r9, %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl get_elem2_ptr
	.text
get_elem2_ptr:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movq %rdi, %r9
	movq %r9, %rax
	leaq 8(%rax), %r9
	movq %r9, %rax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_add_multi_dimensional
	.text
test_add_multi_dimensional:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl $1, -48(%rbp)
	movl $2, -44(%rbp)
	movl $3, -40(%rbp)
	movl $4, -36(%rbp)
	movl $5, -32(%rbp)
	movl $6, -28(%rbp)
	movl $7, -24(%rbp)
	movl $8, -20(%rbp)
	movl $9, -16(%rbp)
	leaq -48(%rbp), %r8
	movslq index.22+0(%rip), %r9
	movq %r8, %rax
	movq %r9, %rdx
	imul $12, %rdx
	leaq (%rax, %rdx, 1), %r9
	movq %r9, %rax
	movl 0(%rax), %r9d
	cmpl $7, %r9d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_add_to_subarray_pointer
	.text
test_add_to_subarray_pointer:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl $1, -48(%rbp)
	movl $2, -44(%rbp)
	movl $3, -40(%rbp)
	movl $4, -36(%rbp)
	movl $5, -32(%rbp)
	movl $6, -28(%rbp)
	movl $7, -24(%rbp)
	movl $8, -20(%rbp)
	movl $9, -16(%rbp)
	leaq -48(%rbp), %r9
	movq %r9, %rax
	leaq 12(%rax), %r8
	movslq index.25+0(%rip), %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 4), %r9
	movq %r9, %rax
	movl 0(%rax), %r9d
	cmpl $6, %r9d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_subtract_from_pointer
	.text
test_subtract_from_pointer:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movq $10, -48(%rbp)
	movq $9, -40(%rbp)
	movq $8, -32(%rbp)
	movq $7, -24(%rbp)
	movq $6, -16(%rbp)
	leaq -48(%rbp), %r9
	movq %r9, %rax
	leaq 40(%rax), %r8
	movslq index.31+0(%rip), %r9
	negq %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %r9
	movq %r9, %rax
	movq 0(%rax), %r9
	cmpq $8, %r9
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_subtract_negative_index
	.text
test_subtract_negative_index:
	pushq %rbp
	movq %rsp, %rbp
	subq $48, %rsp
	movl $100, %r9d
	movl %r9d, -32(%rbp)
	movl $101, %r9d
	movl %r9d, -28(%rbp)
	movl $102, %r9d
	movl %r9d, -24(%rbp)
	movl $103, %r9d
	movl %r9d, -20(%rbp)
	movl $104, %r9d
	movl %r9d, -16(%rbp)
	leaq -32(%rbp), %r8
	movl $3, %r9d
	negl %r9d
	movslq %r9d, %r9
	negq %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 4), %r9
	movq %r9, %rax
	movl 0(%rax), %r8d
	movl $103, %r9d
	cmpl %r9d, %r8d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.365:
	.double 6.0
	.section .rodata
	.align 8
tmp.366:
	.double 0.0
	.section .rodata
	.align 8
tmp.367:
	.double 0.0
	.section .rodata
	.align 8
tmp.368:
	.double 0.0
	.section .rodata
	.align 8
tmp.369:
	.double 0.0
	.section .rodata
	.align 8
tmp.370:
	.double 6.0
	.globl test_subtract_different_index_types
	.text
test_subtract_different_index_types:
	pushq %rbp
	movq %rsp, %rbp
	subq $112, %rsp
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -96(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -88(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -80(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -72(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -64(%rbp)
	movl $0, %r10d
	cvtsi2sdl %r10d, %xmm13
	movsd %xmm13, -56(%rbp)
	movsd tmp.365+0(%rip), %xmm14
	movsd %xmm14, -48(%rbp)
	movsd tmp.366+0(%rip), %xmm14
	movsd %xmm14, -40(%rbp)
	movsd tmp.367+0(%rip), %xmm14
	movsd %xmm14, -32(%rbp)
	movsd tmp.368+0(%rip), %xmm14
	movsd %xmm14, -24(%rbp)
	movsd tmp.369+0(%rip), %xmm14
	movsd %xmm14, -16(%rbp)
	leaq -96(%rbp), %r9
	movq %r9, %rax
	leaq 88(%rax), %rax
	movq $5, %r9
	negq %r9
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %rdi
	movq $5, %r9
	negq %r9
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %rsi
	movl $5, %r9d
	negq %r9
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %r8
	movq $5, %r9
	negq %r9
	movq %r9, %rdx
	leaq (%rax, %rdx, 8), %rax
	cmpq %rsi, %rdi
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.268
	cmpq %r8, %rdi
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.268
	movl $1, %r9d
	jmp .Ltmp.271
.Ltmp.268:
	movl $0, %r9d
.Ltmp.271:
	cmpl $0, %r9d
	jE .Ltmp.272
	cmpq %rax, %rdi
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.272
	movl $1, %r9d
	jmp .Ltmp.275
.Ltmp.272:
	movl $0, %r9d
.Ltmp.275:
	cmpl $0, %r9d
	jE .Ltmp.276
	movsd 0(%rax), %xmm13
	comisd tmp.370+0(%rip), %xmm13
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.276
	movl $1, %r9d
	jmp .Ltmp.280
.Ltmp.276:
	movl $0, %r9d
.Ltmp.280:
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_subtract_complex_expressions
	.text
test_subtract_complex_expressions:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	cmpl $0, flag.41+0(%rip)
	jE .Ltmp.282
	leaq arr.43+0(%rip), %r9
	movq %r9, %rdi
	call get_elem1_ptr
	movq %rax, %r9
	movq %r9, %r8
	jmp .Ltmp.288
.Ltmp.282:
	leaq arr.43+0(%rip), %r9
	movq %r9, %rdi
	call get_elem2_ptr
	movq %rax, %r9
	movq %r9, %r8
.Ltmp.288:
	movl $2, %r9d
	negl %r9d
	movl four.42+0(%rip), %eax
	cdq
	idivl %r9d
	movl %eax, %r9d
	movslq %r9d, %r9
	negq %r9
	movq %r8, %rax
	movq %r9, %rdx
	leaq (%rax, %rdx, 4), %r9
	movq %r9, %rax
	movl 0(%rax), %r9d
	cmpl $4, %r9d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_subtract_multi_dimensional
	.text
test_subtract_multi_dimensional:
	pushq %rbp
	movq %rsp, %rbp
	subq $64, %rsp
	movl $1, -48(%rbp)
	movl $2, -44(%rbp)
	movl $3, -40(%rbp)
	movl $4, -36(%rbp)
	movl $5, -32(%rbp)
	movl $6, -28(%rbp)
	movl $7, -24(%rbp)
	movl $8, -20(%rbp)
	movl $9, -16(%rbp)
	leaq -48(%rbp), %r9
	movq %r9, %rax
	leaq 24(%rax), %r8
	movslq index.45+0(%rip), %r9
	negq %r9
	movq %r8, %rax
	movq %r9, %rdx
	imul $12, %rdx
	leaq (%rax, %rdx, 1), %r9
	movq %r9, %rax
	movl 0(%rax), %r9d
	cmpl $4, %r9d
	movl $0, %r9d
	setE %r9b
	movl %r9d, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	call test_add_constant_to_pointer
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.317
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.317:
	call test_add_negative_index
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.321
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.321:
	call test_add_pointer_to_int
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.325
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.325:
	call test_add_different_index_types
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.329
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.329:
	call test_add_complex_expressions
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.333
	movl $5, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.333:
	call test_add_multi_dimensional
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.337
	movl $6, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.337:
	call test_add_to_subarray_pointer
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.341
	movl $7, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.341:
	call test_subtract_from_pointer
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.345
	movl $8, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.345:
	call test_subtract_negative_index
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.349
	movl $9, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.349:
	call test_subtract_different_index_types
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.353
	movl $10, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.353:
	call test_subtract_complex_expressions
	movl %eax, %r9d
	cmpl $0, %r9d
	movl $0, %r9d
	setE %r9b
	cmpl $0, %r9d
	jE .Ltmp.357
	movl $11, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.357:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.bss
	.align 4
flag.13:
	.zero 4
	.data
	.align 16
arr.18:
	.long 1
	.long 2
	.long 3
	.long 4
	.data
	.align 4
index.22:
	.long 2
	.data
	.align 4
index.25:
	.long 2
	.data
	.align 4
index.31:
	.long 3
	.data
	.align 4
flag.41:
	.long 1
	.data
	.align 4
four.42:
	.long 4
	.data
	.align 16
arr.43:
	.long 1
	.long 2
	.long 3
	.long 4
	.data
	.align 4
index.45:
	.long 1
	.section	.note.GNU-stack,"",@progbits
