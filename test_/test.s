	.globl test_static
	.text
test_static:
	pushq %rbp
	movq %rsp, %rbp
	subq $272, %rsp
	leaq static_arr(%rip), %r11
	movq %r11, -8(%rbp)
	movq -8(%rbp), %r10
	movq %r10, -16(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -24(%rbp)
	movq -24(%rbp), %r10
	movq %r10, -32(%rbp)
	movq -16(%rbp), %rax
	movq -32(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -40(%rbp)
	movq -40(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -41(%rbp)
	movsbl -41(%rbp), %r11d
	movl %r11d, -48(%rbp)
	cmpl $104, -48(%rbp)
	movl $0, -52(%rbp)
	setE -52(%rbp)
	cmpl $0, -52(%rbp)
	jE .Ltmp.24
	leaq static_arr(%rip), %r11
	movq %r11, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -72(%rbp), %rax
	movq -88(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -97(%rbp)
	movsbl -97(%rbp), %r11d
	movl %r11d, -104(%rbp)
	cmpl $105, -104(%rbp)
	movl $0, -108(%rbp)
	setE -108(%rbp)
	cmpl $0, -108(%rbp)
	jE .Ltmp.24
	movl $1, -112(%rbp)
	jmp .Ltmp.34
.Ltmp.24:
	movl $0, -112(%rbp)
.Ltmp.34:
	cmpl $0, -112(%rbp)
	jE .Ltmp.35
	leaq static_arr(%rip), %r11
	movq %r11, -120(%rbp)
	movq -120(%rbp), %r10
	movq %r10, -128(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -136(%rbp)
	movq -136(%rbp), %r10
	movq %r10, -144(%rbp)
	movq -128(%rbp), %rax
	movq -144(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -152(%rbp)
	movq -152(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -153(%rbp)
	cmpb $0, -153(%rbp)
	jNE .Ltmp.42
	leaq static_arr(%rip), %r11
	movq %r11, -168(%rbp)
	movq -168(%rbp), %r10
	movq %r10, -176(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -184(%rbp)
	movq -184(%rbp), %r10
	movq %r10, -192(%rbp)
	movq -176(%rbp), %rax
	movq -192(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -200(%rbp)
	movq -200(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -201(%rbp)
	cmpb $0, -201(%rbp)
	jNE .Ltmp.42
	movl $0, -208(%rbp)
	jmp .Ltmp.50
.Ltmp.42:
	movl $1, -208(%rbp)
.Ltmp.50:
	cmpl $0, -208(%rbp)
	jNE .Ltmp.51
	leaq static_arr(%rip), %r11
	movq %r11, -216(%rbp)
	movq -216(%rbp), %r10
	movq %r10, -224(%rbp)
	movl $4, %r10d
	movslq %r10d, %r11
	movq %r11, -232(%rbp)
	movq -232(%rbp), %r10
	movq %r10, -240(%rbp)
	movq -224(%rbp), %rax
	movq -240(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -248(%rbp)
	movq -248(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -249(%rbp)
	cmpb $0, -249(%rbp)
	jNE .Ltmp.51
	movl $0, -256(%rbp)
	jmp .Ltmp.59
.Ltmp.51:
	movl $1, -256(%rbp)
.Ltmp.59:
	cmpl $0, -256(%rbp)
	movl $0, -260(%rbp)
	setE -260(%rbp)
	cmpl $0, -260(%rbp)
	jE .Ltmp.35
	movl $1, -264(%rbp)
	jmp .Ltmp.62
.Ltmp.35:
	movl $0, -264(%rbp)
.Ltmp.62:
	movl -264(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_static_nested
	.text
test_static_nested:
	pushq %rbp
	movq %rsp, %rbp
	subq $176, %rsp
	movl $0, -4(%rbp)
.Ltmp.63:
	cmpl $3, -4(%rbp)
	movl $0, -8(%rbp)
	setL -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Lbreak_tmp.11
	movl $0, -16(%rbp)
.Ltmp.66:
	cmpl $4, -16(%rbp)
	movl $0, -20(%rbp)
	setL -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Lbreak_tmp.12
	leaq nested_static_arr(%rip), %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movslq -4(%rbp), %r11
	movq %r11, -48(%rbp)
	movq -48(%rbp), %r10
	movq %r10, -56(%rbp)
	movq -40(%rbp), %rax
	movq -56(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movslq -16(%rbp), %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -72(%rbp), %rax
	movq -88(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -97(%rbp)
	movb -97(%rbp), %r10b
	movb %r10b, -98(%rbp)
	movb $0, -99(%rbp)
	movb -99(%rbp), %r10b
	movb %r10b, -100(%rbp)
	cmpl $1, -4(%rbp)
	movl $0, -104(%rbp)
	setE -104(%rbp)
	cmpl $0, -104(%rbp)
	jE .Ltmp.81
	cmpl $0, -16(%rbp)
	movl $0, -108(%rbp)
	setE -108(%rbp)
	cmpl $0, -108(%rbp)
	jE .Ltmp.81
	movl $1, -112(%rbp)
	jmp .Ltmp.84
.Ltmp.81:
	movl $0, -112(%rbp)
.Ltmp.84:
	movl -112(%rbp), %r10d
	movl %r10d, -116(%rbp)
	cmpl $0, -116(%rbp)
	jE .Ltmp.87
	movb $98, -117(%rbp)
	movb -117(%rbp), %r10b
	movb %r10b, -100(%rbp)
	jmp .Ltmp.86
.Ltmp.87:
	cmpl $1, -4(%rbp)
	movl $0, -124(%rbp)
	setE -124(%rbp)
	cmpl $0, -124(%rbp)
	jE .Ltmp.90
	cmpl $1, -16(%rbp)
	movl $0, -128(%rbp)
	setE -128(%rbp)
	cmpl $0, -128(%rbp)
	jE .Ltmp.90
	movl $1, -132(%rbp)
	jmp .Ltmp.93
.Ltmp.90:
	movl $0, -132(%rbp)
.Ltmp.93:
	movl -132(%rbp), %r10d
	movl %r10d, -136(%rbp)
	cmpl $0, -136(%rbp)
	jE .Ltmp.86
	movb $99, -137(%rbp)
	movb -137(%rbp), %r10b
	movb %r10b, -100(%rbp)
.Ltmp.86:
	movsbl -98(%rbp), %r11d
	movl %r11d, -144(%rbp)
	movsbl -100(%rbp), %r11d
	movl %r11d, -148(%rbp)
	movl -148(%rbp), %r10d
	cmpl %r10d, -144(%rbp)
	movl $0, -152(%rbp)
	setNE -152(%rbp)
	movl -152(%rbp), %r10d
	movl %r10d, -156(%rbp)
	cmpl $0, -156(%rbp)
	jE .Ltmp.100
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.100:
.Lcontinue_tmp.12:
	movl -16(%rbp), %r10d
	movl %r10d, -160(%rbp)
	addl $1, -160(%rbp)
	movl -160(%rbp), %r10d
	movl %r10d, -16(%rbp)
	jmp .Ltmp.66
.Lbreak_tmp.12:
.Lcontinue_tmp.11:
	movl -4(%rbp), %r10d
	movl %r10d, -164(%rbp)
	addl $1, -164(%rbp)
	movl -164(%rbp), %r10d
	movl %r10d, -4(%rbp)
	jmp .Ltmp.63
.Lbreak_tmp.11:
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_automatic
	.text
test_automatic:
	pushq %rbp
	movq %rsp, %rbp
	subq $224, %rsp
	movb $97, -4(%rbp)
	movb $98, -3(%rbp)
	movb $0, -2(%rbp)
	movb $0, -1(%rbp)
	leaq -4(%rbp), %r11
	movq %r11, -16(%rbp)
	movq -16(%rbp), %r10
	movq %r10, -24(%rbp)
	movl $0, %r10d
	movslq %r10d, %r11
	movq %r11, -32(%rbp)
	movq -32(%rbp), %r10
	movq %r10, -40(%rbp)
	movq -24(%rbp), %rax
	movq -40(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -48(%rbp)
	movq -48(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -49(%rbp)
	movzbl -49(%rbp), %r11d
	movl %r11d, -56(%rbp)
	cmpl $97, -56(%rbp)
	movl $0, -60(%rbp)
	setE -60(%rbp)
	cmpl $0, -60(%rbp)
	jE .Ltmp.111
	leaq -4(%rbp), %r11
	movq %r11, -72(%rbp)
	movq -72(%rbp), %r10
	movq %r10, -80(%rbp)
	movl $1, %r10d
	movslq %r10d, %r11
	movq %r11, -88(%rbp)
	movq -88(%rbp), %r10
	movq %r10, -96(%rbp)
	movq -80(%rbp), %rax
	movq -96(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -104(%rbp)
	movq -104(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -105(%rbp)
	movzbl -105(%rbp), %r11d
	movl %r11d, -112(%rbp)
	cmpl $98, -112(%rbp)
	movl $0, -116(%rbp)
	setE -116(%rbp)
	cmpl $0, -116(%rbp)
	jE .Ltmp.111
	movl $1, -120(%rbp)
	jmp .Ltmp.121
.Ltmp.111:
	movl $0, -120(%rbp)
.Ltmp.121:
	cmpl $0, -120(%rbp)
	jE .Ltmp.122
	leaq -4(%rbp), %r11
	movq %r11, -128(%rbp)
	movq -128(%rbp), %r10
	movq %r10, -136(%rbp)
	movl $2, %r10d
	movslq %r10d, %r11
	movq %r11, -144(%rbp)
	movq -144(%rbp), %r10
	movq %r10, -152(%rbp)
	movq -136(%rbp), %rax
	movq -152(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -160(%rbp)
	movq -160(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -161(%rbp)
	cmpb $0, -161(%rbp)
	jNE .Ltmp.129
	leaq -4(%rbp), %r11
	movq %r11, -176(%rbp)
	movq -176(%rbp), %r10
	movq %r10, -184(%rbp)
	movl $3, %r10d
	movslq %r10d, %r11
	movq %r11, -192(%rbp)
	movq -192(%rbp), %r10
	movq %r10, -200(%rbp)
	movq -184(%rbp), %rax
	movq -200(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -208(%rbp)
	movq -208(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -209(%rbp)
	cmpb $0, -209(%rbp)
	jNE .Ltmp.129
	movl $0, -216(%rbp)
	jmp .Ltmp.137
.Ltmp.129:
	movl $1, -216(%rbp)
.Ltmp.137:
	cmpl $0, -216(%rbp)
	movl $0, -220(%rbp)
	setE -220(%rbp)
	cmpl $0, -220(%rbp)
	jE .Ltmp.122
	movl $1, -224(%rbp)
	jmp .Ltmp.140
.Ltmp.122:
	movl $0, -224(%rbp)
.Ltmp.140:
	movl -224(%rbp), %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.globl test_automatic_nested
	.text
test_automatic_nested:
	pushq %rbp
	movq %rsp, %rbp
	subq $336, %rsp
	movb $102, -16(%rbp)
	movb $111, -15(%rbp)
	movb $111, -14(%rbp)
	movb $0, -13(%rbp)
	movb $0, -12(%rbp)
	movb $0, -11(%rbp)
	movb $0, -10(%rbp)
	movb $0, -9(%rbp)
	movb $120, -8(%rbp)
	movb $0, -7(%rbp)
	movb $0, -6(%rbp)
	movb $0, -5(%rbp)
	movb $121, -4(%rbp)
	movb $122, -3(%rbp)
	movb $0, -2(%rbp)
	movb $0, -1(%rbp)
	movl $0, -20(%rbp)
.Ltmp.141:
	cmpl $2, -20(%rbp)
	movl $0, -24(%rbp)
	setL -24(%rbp)
	movl -24(%rbp), %r10d
	movl %r10d, -28(%rbp)
	cmpl $0, -28(%rbp)
	jE .Lbreak_tmp.13
	movl $0, -32(%rbp)
.Ltmp.144:
	cmpl $2, -32(%rbp)
	movl $0, -36(%rbp)
	setL -36(%rbp)
	movl -36(%rbp), %r10d
	movl %r10d, -40(%rbp)
	cmpl $0, -40(%rbp)
	jE .Lbreak_tmp.14
	movl $0, -44(%rbp)
.Ltmp.147:
	cmpl $4, -44(%rbp)
	movl $0, -48(%rbp)
	setL -48(%rbp)
	movl -48(%rbp), %r10d
	movl %r10d, -52(%rbp)
	cmpl $0, -52(%rbp)
	jE .Lbreak_tmp.15
	leaq -16(%rbp), %r11
	movq %r11, -64(%rbp)
	movq -64(%rbp), %r10
	movq %r10, -72(%rbp)
	movslq -20(%rbp), %r11
	movq %r11, -80(%rbp)
	movq -80(%rbp), %r10
	movq %r10, -88(%rbp)
	movq -72(%rbp), %rax
	movq -88(%rbp), %rdx
	leaq (%rax, %rdx, 8), %r11
	movq %r11, -96(%rbp)
	movq -96(%rbp), %r10
	movq %r10, -104(%rbp)
	movslq -32(%rbp), %r11
	movq %r11, -112(%rbp)
	movq -112(%rbp), %r10
	movq %r10, -120(%rbp)
	movq -104(%rbp), %rax
	movq -120(%rbp), %rdx
	leaq (%rax, %rdx, 4), %r11
	movq %r11, -128(%rbp)
	movq -128(%rbp), %r10
	movq %r10, -136(%rbp)
	movslq -44(%rbp), %r11
	movq %r11, -144(%rbp)
	movq -144(%rbp), %r10
	movq %r10, -152(%rbp)
	movq -136(%rbp), %rax
	movq -152(%rbp), %rdx
	leaq (%rax, %rdx, 1), %r11
	movq %r11, -160(%rbp)
	movq -160(%rbp), %rax
	movb 0(%rax), %r10b
	movb %r10b, -161(%rbp)
	movb -161(%rbp), %r10b
	movb %r10b, -162(%rbp)
	movb $0, -163(%rbp)
	movb -163(%rbp), %r10b
	movb %r10b, -164(%rbp)
	cmpl $0, -20(%rbp)
	movl $0, -168(%rbp)
	setE -168(%rbp)
	cmpl $0, -168(%rbp)
	jE .Ltmp.166
	cmpl $0, -32(%rbp)
	movl $0, -172(%rbp)
	setE -172(%rbp)
	cmpl $0, -172(%rbp)
	jE .Ltmp.166
	movl $1, -176(%rbp)
	jmp .Ltmp.169
.Ltmp.166:
	movl $0, -176(%rbp)
.Ltmp.169:
	movl -176(%rbp), %r10d
	movl %r10d, -180(%rbp)
	cmpl $0, -180(%rbp)
	jE .Ltmp.172
	cmpl $0, -44(%rbp)
	movl $0, -184(%rbp)
	setE -184(%rbp)
	movl -184(%rbp), %r10d
	movl %r10d, -188(%rbp)
	cmpl $0, -188(%rbp)
	jE .Ltmp.176
	movb $102, -189(%rbp)
	movb -189(%rbp), %r10b
	movb %r10b, -164(%rbp)
	jmp .Ltmp.175
.Ltmp.176:
	cmpl $1, -44(%rbp)
	movl $0, -196(%rbp)
	setE -196(%rbp)
	cmpl $0, -196(%rbp)
	jNE .Ltmp.179
	cmpl $2, -44(%rbp)
	movl $0, -200(%rbp)
	setE -200(%rbp)
	cmpl $0, -200(%rbp)
	jNE .Ltmp.179
	movl $0, -204(%rbp)
	jmp .Ltmp.182
.Ltmp.179:
	movl $1, -204(%rbp)
.Ltmp.182:
	movl -204(%rbp), %r10d
	movl %r10d, -208(%rbp)
	cmpl $0, -208(%rbp)
	jE .Ltmp.175
	movb $111, -209(%rbp)
	movb -209(%rbp), %r10b
	movb %r10b, -164(%rbp)
.Ltmp.175:
	jmp .Ltmp.171
.Ltmp.172:
	cmpl $1, -20(%rbp)
	movl $0, -216(%rbp)
	setE -216(%rbp)
	cmpl $0, -216(%rbp)
	jE .Ltmp.186
	cmpl $0, -32(%rbp)
	movl $0, -220(%rbp)
	setE -220(%rbp)
	cmpl $0, -220(%rbp)
	jE .Ltmp.186
	movl $1, -224(%rbp)
	jmp .Ltmp.189
.Ltmp.186:
	movl $0, -224(%rbp)
.Ltmp.189:
	cmpl $0, -224(%rbp)
	jE .Ltmp.190
	cmpl $0, -44(%rbp)
	movl $0, -228(%rbp)
	setE -228(%rbp)
	cmpl $0, -228(%rbp)
	jE .Ltmp.190
	movl $1, -232(%rbp)
	jmp .Ltmp.193
.Ltmp.190:
	movl $0, -232(%rbp)
.Ltmp.193:
	movl -232(%rbp), %r10d
	movl %r10d, -236(%rbp)
	cmpl $0, -236(%rbp)
	jE .Ltmp.195
	movb $120, -237(%rbp)
	movb -237(%rbp), %r10b
	movb %r10b, -164(%rbp)
	jmp .Ltmp.171
.Ltmp.195:
	cmpl $1, -20(%rbp)
	movl $0, -244(%rbp)
	setE -244(%rbp)
	cmpl $0, -244(%rbp)
	jE .Ltmp.198
	cmpl $1, -32(%rbp)
	movl $0, -248(%rbp)
	setE -248(%rbp)
	cmpl $0, -248(%rbp)
	jE .Ltmp.198
	movl $1, -252(%rbp)
	jmp .Ltmp.201
.Ltmp.198:
	movl $0, -252(%rbp)
.Ltmp.201:
	cmpl $0, -252(%rbp)
	jE .Ltmp.202
	cmpl $0, -44(%rbp)
	movl $0, -256(%rbp)
	setE -256(%rbp)
	cmpl $0, -256(%rbp)
	jE .Ltmp.202
	movl $1, -260(%rbp)
	jmp .Ltmp.205
.Ltmp.202:
	movl $0, -260(%rbp)
.Ltmp.205:
	movl -260(%rbp), %r10d
	movl %r10d, -264(%rbp)
	cmpl $0, -264(%rbp)
	jE .Ltmp.207
	movb $121, -265(%rbp)
	movb -265(%rbp), %r10b
	movb %r10b, -164(%rbp)
	jmp .Ltmp.171
.Ltmp.207:
	cmpl $1, -20(%rbp)
	movl $0, -272(%rbp)
	setE -272(%rbp)
	cmpl $0, -272(%rbp)
	jE .Ltmp.210
	cmpl $1, -32(%rbp)
	movl $0, -276(%rbp)
	setE -276(%rbp)
	cmpl $0, -276(%rbp)
	jE .Ltmp.210
	movl $1, -280(%rbp)
	jmp .Ltmp.213
.Ltmp.210:
	movl $0, -280(%rbp)
.Ltmp.213:
	cmpl $0, -280(%rbp)
	jE .Ltmp.214
	cmpl $1, -44(%rbp)
	movl $0, -284(%rbp)
	setE -284(%rbp)
	cmpl $0, -284(%rbp)
	jE .Ltmp.214
	movl $1, -288(%rbp)
	jmp .Ltmp.217
.Ltmp.214:
	movl $0, -288(%rbp)
.Ltmp.217:
	movl -288(%rbp), %r10d
	movl %r10d, -292(%rbp)
	cmpl $0, -292(%rbp)
	jE .Ltmp.171
	movb $122, -293(%rbp)
	movb -293(%rbp), %r10b
	movb %r10b, -164(%rbp)
.Ltmp.171:
	movsbl -162(%rbp), %r11d
	movl %r11d, -300(%rbp)
	movsbl -164(%rbp), %r11d
	movl %r11d, -304(%rbp)
	movl -304(%rbp), %r10d
	cmpl %r10d, -300(%rbp)
	movl $0, -308(%rbp)
	setNE -308(%rbp)
	movl -308(%rbp), %r10d
	movl %r10d, -312(%rbp)
	cmpl $0, -312(%rbp)
	jE .Ltmp.224
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.224:
.Lcontinue_tmp.15:
	movl -44(%rbp), %r10d
	movl %r10d, -316(%rbp)
	addl $1, -316(%rbp)
	movl -316(%rbp), %r10d
	movl %r10d, -44(%rbp)
	jmp .Ltmp.147
.Lbreak_tmp.15:
.Lcontinue_tmp.14:
	movl -32(%rbp), %r10d
	movl %r10d, -320(%rbp)
	addl $1, -320(%rbp)
	movl -320(%rbp), %r10d
	movl %r10d, -32(%rbp)
	jmp .Ltmp.144
.Lbreak_tmp.14:
.Lcontinue_tmp.13:
	movl -20(%rbp), %r10d
	movl %r10d, -324(%rbp)
	addl $1, -324(%rbp)
	movl -324(%rbp), %r10d
	movl %r10d, -20(%rbp)
	jmp .Ltmp.141
.Lbreak_tmp.13:
	movl $1, %eax
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
	subq $48, %rsp
	call test_static
	movl %eax, -4(%rbp)
	cmpl $0, -4(%rbp)
	movl $0, -8(%rbp)
	setE -8(%rbp)
	movl -8(%rbp), %r10d
	movl %r10d, -12(%rbp)
	cmpl $0, -12(%rbp)
	jE .Ltmp.231
	movl $1, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.231:
	call test_static_nested
	movl %eax, -16(%rbp)
	cmpl $0, -16(%rbp)
	movl $0, -20(%rbp)
	setE -20(%rbp)
	movl -20(%rbp), %r10d
	movl %r10d, -24(%rbp)
	cmpl $0, -24(%rbp)
	jE .Ltmp.235
	movl $2, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.235:
	call test_automatic
	movl %eax, -28(%rbp)
	cmpl $0, -28(%rbp)
	movl $0, -32(%rbp)
	setE -32(%rbp)
	movl -32(%rbp), %r10d
	movl %r10d, -36(%rbp)
	cmpl $0, -36(%rbp)
	jE .Ltmp.239
	movl $3, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.239:
	call test_automatic_nested
	movl %eax, -40(%rbp)
	cmpl $0, -40(%rbp)
	movl $0, -44(%rbp)
	setE -44(%rbp)
	movl -44(%rbp), %r10d
	movl %r10d, -48(%rbp)
	cmpl $0, -48(%rbp)
	jE .Ltmp.243
	movl $4, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
.Ltmp.243:
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.data
	.align 1
static_arr:
	.asciz "hi"
	.zero 2
	.data
	.align 1
nested_static_arr:
	.asciz ""
	.zero 3
	.asciz "bc"
	.zero 1
	.zero 4
	.section	.note.GNU-stack,"",@progbits
