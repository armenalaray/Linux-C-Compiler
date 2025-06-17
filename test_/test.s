	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $368, %rsp
	movb $97, -4(%rbp)
	movb $98, -3(%rbp)
	movb $99, -2(%rbp)
	movb $0, -1(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movq -24(%rbp), %rdi
	call puts
	movl %eax, -28(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %r10
	movq %r10, -48(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -56(%rbp)
	movq -56(%rbp), %r10
	movq %r10, -64(%rbp)
	movq -48(%rbp), %rax
	movq -64(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -72(%rbp)
	movb $120, -73(%rbp)
	movq -72(%rbp), %rax
	movb -73(%rbp), %r10b
	movb %r10b, 0(%rax)
	leaq -4(%rbp), %r11
	movq %r11, -88(%rbp)
	movq -88(%rbp), %r10
	movq %r10, -96(%rbp)
	movq -96(%rbp), %rdi
	call puts
	movl %eax, -100(%rbp)
	movb $72, -112(%rbp)
	movb $101, -111(%rbp)
	movb $108, -110(%rbp)
	movb $108, -109(%rbp)
	movb $111, -108(%rbp)
	movb $0, -107(%rbp)
	movb $87, -106(%rbp)
	movb $111, -105(%rbp)
	movb $114, -104(%rbp)
	movb $108, -103(%rbp)
	movb $100, -102(%rbp)
	movb $0, -101(%rbp)
	leaq -112(%rbp), %r11
	movq %r11, -120(%rbp)
	movq -120(%rbp), %r10
	movq %r10, -128(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -136(%rbp)
	movq -136(%rbp), %r10
	movq %r10, -144(%rbp)
	movq -128(%rbp), %rax
	movq -144(%rbp), %rdx
	imul $6, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -152(%rbp)
	movq -152(%rbp), %r10
	movq %r10, -160(%rbp)
	movq -160(%rbp), %rdi
	call puts
	movl %eax, -164(%rbp)
	leaq -112(%rbp), %r11
	movq %r11, -176(%rbp)
	movq -176(%rbp), %r10
	movq %r10, -184(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -192(%rbp)
	movq -192(%rbp), %r10
	movq %r10, -200(%rbp)
	movq -184(%rbp), %rax
	movq -200(%rbp), %rdx
	imul $6, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -208(%rbp)
	movq -208(%rbp), %r10
	movq %r10, -216(%rbp)
	movq -216(%rbp), %rdi
	call puts
	movl %eax, -220(%rbp)
	leaq -112(%rbp), %r11
	movq %r11, -232(%rbp)
	movq -232(%rbp), %r10
	movq %r10, -240(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -248(%rbp)
	movq -248(%rbp), %r10
	movq %r10, -256(%rbp)
	movq -240(%rbp), %rax
	movq -256(%rbp), %rdx
	imul $6, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -264(%rbp)
	movq -264(%rbp), %r10
	movq %r10, -272(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -280(%rbp)
	movq -280(%rbp), %r10
	movq %r10, -288(%rbp)
	movq -272(%rbp), %rax
	movq -288(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -296(%rbp)
	movb $74, -297(%rbp)
	movq -296(%rbp), %rax
	movb -297(%rbp), %r10b
	movb %r10b, 0(%rax)
	leaq -112(%rbp), %r11
	movq %r11, -312(%rbp)
	movq -312(%rbp), %r10
	movq %r10, -320(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -328(%rbp)
	movq -328(%rbp), %r10
	movq %r10, -336(%rbp)
	movq -320(%rbp), %rax
	movq -336(%rbp), %rdx
	imul $6, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -344(%rbp)
	movq -344(%rbp), %r10
	movq %r10, -352(%rbp)
	movq -352(%rbp), %rdi
	call puts
	movl %eax, -356(%rbp)
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
