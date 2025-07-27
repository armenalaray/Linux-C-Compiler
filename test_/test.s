	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $368, %rsp
	movl $0, -288(%rbp)
	movl $1, -284(%rbp)
	movl $0, -280(%rbp)
	movl $0, -276(%rbp)
	movl $0, -272(%rbp)
	movl $0, -268(%rbp)
	movl $0, -264(%rbp)
	movl $0, -260(%rbp)
	movl $0, -256(%rbp)
	movl $0, -252(%rbp)
	movl $0, -248(%rbp)
	movl $0, -244(%rbp)
	movl $0, -240(%rbp)
	movl $0, -236(%rbp)
	movl $0, -232(%rbp)
	movl $0, -228(%rbp)
	movl $0, -224(%rbp)
	movl $0, -220(%rbp)
	movl $0, -216(%rbp)
	movl $0, -212(%rbp)
	movl $0, -208(%rbp)
	movl $0, -204(%rbp)
	movl $0, -200(%rbp)
	movl $2, -196(%rbp)
	movl $0, -192(%rbp)
	movl $0, -188(%rbp)
	movl $0, -184(%rbp)
	movl $0, -180(%rbp)
	movl $0, -176(%rbp)
	movl $0, -172(%rbp)
	movl $0, -168(%rbp)
	movl $0, -164(%rbp)
	movl $0, -160(%rbp)
	movl $0, -156(%rbp)
	movl $0, -152(%rbp)
	movl $0, -148(%rbp)
	movl $0, -144(%rbp)
	movl $0, -140(%rbp)
	movl $0, -136(%rbp)
	movl $0, -132(%rbp)
	movl $0, -128(%rbp)
	movl $0, -124(%rbp)
	movl $0, -120(%rbp)
	movl $0, -116(%rbp)
	movl $0, -112(%rbp)
	movl $0, -108(%rbp)
	movl $0, -104(%rbp)
	movl $0, -100(%rbp)
	movl $0, -96(%rbp)
	movl $0, -92(%rbp)
	movl $0, -88(%rbp)
	movl $0, -84(%rbp)
	movl $0, -80(%rbp)
	movl $0, -76(%rbp)
	movl $0, -72(%rbp)
	movl $0, -68(%rbp)
	movl $0, -64(%rbp)
	movl $0, -60(%rbp)
	movl $0, -56(%rbp)
	movl $0, -52(%rbp)
	movl $0, -48(%rbp)
	movl $0, -44(%rbp)
	movl $0, -40(%rbp)
	movl $0, -36(%rbp)
	movl $0, -32(%rbp)
	movl $0, -28(%rbp)
	movl $0, -24(%rbp)
	movl $0, -20(%rbp)
	movl $0, -16(%rbp)
	leaq -288(%rbp), %r11
	movq %r11, -296(%rbp)
	movq -296(%rbp), %r10
	movq %r10, -304(%rbp)
	movq $1, -312(%rbp)
	movq $1, -320(%rbp)
	movq -296(%rbp), %rax
	leaq 92(%rax), %r11
	movq %r11, -328(%rbp)
	movq -328(%rbp), %r10
	movq %r10, -336(%rbp)
	movq $0, -344(%rbp)
	movq $0, -352(%rbp)
	movq -328(%rbp), %rax
	leaq 0(%rax), %r11
	movq %r11, -360(%rbp)
	movq -360(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -364(%rbp)
	movl -364(%rbp), %eax
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
	movl %eax, -4(%rbp)
	movl -4(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
