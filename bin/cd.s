	.file	"cd.c"
	.text
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"ls"
	.text
	.globl	main
	.type	main, @function
main:
	subq	$8, %rsp
	leaq	.LC0(%rip), %rdi
	call	system@PLT
	movl	$0, %eax
	addq	$8, %rsp
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
