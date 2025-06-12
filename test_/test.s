	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $320, %rsp
	leaq -12(%rbp), %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movq -32(%rbp), %rax
	movq -48(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	movq %r10, -64(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -72(%rbp)
	movq -72(%rbp), %r10
	movq %r10, -80(%rbp)
	movq -64(%rbp), %rax
	movq -80(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -88(%rbp)
	movq -88(%rbp), %rax
	movl $1, 0(%rax)
	leaq -12(%rbp), %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %r10
	movq %r10, -104(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -112(%rbp)
	movq -112(%rbp), %r10
	movq %r10, -120(%rbp)
	movq -104(%rbp), %rax
	movq -120(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -128(%rbp)
	movq -128(%rbp), %r10
	movq %r10, -136(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -144(%rbp)
	movq -144(%rbp), %r10
	movq %r10, -152(%rbp)
	movq -136(%rbp), %rax
	movq -152(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -160(%rbp)
	movq -160(%rbp), %rax
	movl $2, 0(%rax)
	leaq -12(%rbp), %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -184(%rbp)
	movq -184(%rbp), %r10
	movq %r10, -192(%rbp)
	movq -176(%rbp), %rax
	movq -192(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -200(%rbp)
	movq -200(%rbp), %r10
	movq %r10, -208(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -216(%rbp)
	movq -216(%rbp), %r10
	movq %r10, -224(%rbp)
	movq -208(%rbp), %rax
	movq -224(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -232(%rbp)
	movq -232(%rbp), %rax
	movl $3, 0(%rax)
	leaq -12(%rbp), %r11
	movq %r11, -240(%rbp)
	movq -240(%rbp), %r10
	movq %r10, -248(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -256(%rbp)
	movq -256(%rbp), %r10
	movq %r10, -264(%rbp)
	movq -248(%rbp), %rax
	movq -264(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -272(%rbp)
	movq -272(%rbp), %r10
	movq %r10, -280(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -288(%rbp)
	movq -288(%rbp), %r10
	movq %r10, -296(%rbp)
	movq -280(%rbp), %rax
	movq -296(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -304(%rbp)
	movq -304(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -308(%rbp)
	movl -308(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
