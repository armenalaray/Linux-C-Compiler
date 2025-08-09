	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $8, %rsp
	pushq %rbx
	movl $0, %eax
	cmpl $0, flag+0(%rip)
	jE .Ltmp.37
	movl $10, %edi
	call id
.Ltmp.37:
	movl $2, %ebx
	imul %eax, %ebx
	cmpl $10, %eax
	movl $0, %r9d
	setNE %r9b
	cmpl $0, %r9d
	jE .Ltmp.43
	movl $1, %eax
	negl %eax
	popq %rbx
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.43:
	movl $32, %r9d
	subl %ebx, %r9d
	movl $23, %r8d
	subl %r9d, %r8d
	movl $21, %r9d
	subl %r8d, %r9d
	movl $19, %r8d
	subl %r9d, %r8d
	movl $17, %r9d
	subl %r8d, %r9d
	movl $15, %r8d
	subl %r9d, %r8d
	movl $13, %r9d
	subl %r8d, %r9d
	movl $11, %r8d
	subl %r9d, %r8d
	movl $24, %ecx
	subl %ebx, %ecx
	movl $23, %edx
	subl %ebx, %edx
	movl $22, %esi
	subl %ebx, %esi
	movl $21, %edi
	subl %ebx, %edi
	movl $1, %r9d
	call check_5_ints
	movl $0, %eax
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
	.globl flag
	.data
	.align 4
flag:
	.long 1
	.section	.note.GNU-stack,"",@progbits
