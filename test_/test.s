	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	call check_12_ints
	call check_12_ints
	jE .Ltmp.103
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.103:
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl glob_three
	.data
	.align 4
glob_three:
	.long 3
	.section	.note.GNU-stack,"",@progbits
