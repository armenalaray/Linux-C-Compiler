	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $8, %rsp
	pushq %rbx
	pushq %r15
	pushq %r12
	pushq %r14
	pushq %r13
	movl glob_three+0(%rip), %r10d
	movl %r10d, -4(%rbp)
	addl $3, -4(%rbp)
	movl glob_three+0(%rip), %edi
	subl $2, %edi
	movl %edi, %esi
	addl %edi, %esi
	movl $2, %edx
	addl %edi, %edx
	movl %esi, %ecx
	imul %esi, %ecx
	movl $6, %r8d
	subl %edi, %r8d
	movl %esi, %r9d
	imul %edx, %r9d
	movl %edi, %r15d
	addl $6, %r15d
	movl %esi, %r14d
	imul $4, %r14d
	movl %edx, %r13d
	imul %edx, %r13d
	movl %ecx, %r12d
	addl %r9d, %r12d
	movl $16, %ebx
	subl %r8d, %ebx
	movl %r9d, %eax
	addl %r9d, %eax
	subq $8, %rsp
	pushq $1
	pushq %rax
	movl %ebx, %eax
	pushq %rax
	movl %r12d, %eax
	pushq %rax
	movl %r13d, %eax
	pushq %rax
	movl %r14d, %eax
	pushq %rax
	movl %r15d, %eax
	pushq %rax
	call check_12_ints
	addq $64, %rsp
	movl $10, %edi
	addl glob_three+0(%rip), %edi
	movl %edi, %esi
	addl $1, %esi
	movl $28, %edx
	subl %edi, %edx
	movl %esi, %ecx
	addl $2, %ecx
	movl $4, %r8d
	addl %edi, %r8d
	movl $32, %r9d
	subl %esi, %r9d
	movl $35, %r15d
	subl %ecx, %r15d
	movl %edx, %r14d
	addl $5, %r14d
	movl %edi, %ebx
	imul $2, %ebx
	movl %ebx, %r13d
	subl $5, %r13d
	movl %edx, %r12d
	addl $7, %r12d
	movl $6, %ebx
	addl %r8d, %ebx
	movl %edi, %eax
	addl $11, %eax
	subq $8, %rsp
	pushq $13
	pushq %rax
	movl %ebx, %eax
	pushq %rax
	movl %r12d, %eax
	pushq %rax
	movl %r13d, %eax
	pushq %rax
	movl %r14d, %eax
	pushq %rax
	movl %r15d, %eax
	pushq %rax
	call check_12_ints
	addq $64, %rsp
	cmpl $6, -4(%rbp)
	movl $0, %ebx
	setNE %bl
	cmpl $0, %ebx
	jE .Ltmp.103
	movl $1, %eax
	negl %eax
	popq %r13
	popq %r14
	popq %r12
	popq %r15
	popq %rbx
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.103:
	movl $0, %eax
	popq %r13
	popq %r14
	popq %r12
	popq %r15
	popq %rbx
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	call target
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl glob_three
	.data
	.align 4
glob_three:
	.long 3
	.section	.note.GNU-stack,"",@progbits
