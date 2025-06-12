	.globl main
	.text
main:
	pushq %rbp
	movq %rsp, %rbp
	subq $4224, %rsp
	leaq -4000(%rbp), %r11
	movq %r11, -4008(%rbp)
	movq -4008(%rbp), %r10
	movq %r10, -4016(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -4024(%rbp)
	movq -4024(%rbp), %r10
	movq %r10, -4032(%rbp)
	movq -4016(%rbp), %rax
	movq -4032(%rbp), %rdx
	imul $400, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -4040(%rbp)
	movq -4040(%rbp), %r10
	movq %r10, -4048(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -4056(%rbp)
	movq -4056(%rbp), %r10
	movq %r10, -4064(%rbp)
	movq -4048(%rbp), %rax
	movq -4064(%rbp), %rdx
	imul $40, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -4072(%rbp)
	movq -4072(%rbp), %r10
	movq %r10, -4080(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -4088(%rbp)
	movq -4088(%rbp), %r10
	movq %r10, -4096(%rbp)
	movq -4080(%rbp), %rax
	movq -4096(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -4104(%rbp)
	movq -4104(%rbp), %rax
	movl $1, 0(%rax)
	leaq -4000(%rbp), %r11
	movq %r11, -4112(%rbp)
	movq -4112(%rbp), %r10
	movq %r10, -4120(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -4128(%rbp)
	movq -4128(%rbp), %r10
	movq %r10, -4136(%rbp)
	movq -4120(%rbp), %rax
	movq -4136(%rbp), %rdx
	imul $400, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -4144(%rbp)
	movq -4144(%rbp), %r10
	movq %r10, -4152(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -4160(%rbp)
	movq -4160(%rbp), %r10
	movq %r10, -4168(%rbp)
	movq -4152(%rbp), %rax
	movq -4168(%rbp), %rdx
	imul $40, %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -4176(%rbp)
	movq -4176(%rbp), %r10
	movq %r10, -4184(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -4192(%rbp)
	movq -4192(%rbp), %r10
	movq %r10, -4200(%rbp)
	movq -4184(%rbp), %rax
	movq -4200(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -4208(%rbp)
	movq -4208(%rbp), %rax
	movl 0(%rax), %r10d
	movl %r10d, -4212(%rbp)
	movl -4212(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section	.note.GNU-stack,"",@progbits
