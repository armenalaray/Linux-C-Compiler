	.globl incr_glob1
	.text
incr_glob1:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movl $1, %r10d
	cvtsi2sdl %r10d, %xmm12
	movsd glob1+0(%rip), %xmm13
	addsd %xmm12, %xmm13
	movsd %xmm13, glob1+0(%rip)
	movl $0, %eax
	movq %rbp, %rsp
	popq %rbp
	ret
	.section .rodata
	.align 8
tmp.180:
	.double 10.0
	.section .rodata
	.align 8
tmp.181:
	.double 2.0
	.section .rodata
	.align 8
tmp.182:
	.double 4.0
	.section .rodata
	.align 8
tmp.183:
	.double 2.0
	.section .rodata
	.align 8
tmp.184:
	.double 3.0
	.section .rodata
	.align 8
tmp.185:
	.double 2.0
	.section .rodata
	.align 8
tmp.186:
	.double 6.0
	.section .rodata
	.align 8
tmp.187:
	.double 2.0
	.section .rodata
	.align 8
tmp.188:
	.double 2.0
	.section .rodata
	.align 8
tmp.189:
	.double 3.0
	.section .rodata
	.align 8
tmp.190:
	.double 1.0
	.section .rodata
	.align 8
tmp.191:
	.double 2.0
	.section .rodata
	.align 8
tmp.192:
	.double 3.0
	.section .rodata
	.align 8
tmp.193:
	.double 3.0
	.section .rodata
	.align 8
tmp.194:
	.double 2.0
	.section .rodata
	.align 8
tmp.195:
	.double 1.0
	.section .rodata
	.align 8
tmp.196:
	.double 4.0
	.section .rodata
	.align 8
tmp.197:
	.double 3.0
	.section .rodata
	.align 8
tmp.198:
	.double 7.0
	.section .rodata
	.align 8
tmp.199:
	.double 7.0
	.section .rodata
	.align 8
tmp.200:
	.double 0.0
	.section .rodata
	.align 8
tmp.201:
	.double 1.0
	.section .rodata
	.align 8
tmp.202:
	.double 2.0
	.section .rodata
	.align 8
tmp.203:
	.double 3.0
	.section .rodata
	.align 8
tmp.204:
	.double 4.0
	.section .rodata
	.align 8
tmp.205:
	.double 5.0
	.section .rodata
	.align 8
tmp.206:
	.double 6.0
	.section .rodata
	.align 8
tmp.207:
	.double 7.0
	.section .rodata
	.align 8
tmp.208:
	.double 8.0
	.section .rodata
	.align 8
tmp.209:
	.double 9.0
	.section .rodata
	.align 8
tmp.210:
	.double 10.0
	.section .rodata
	.align 8
tmp.211:
	.double 11.0
	.section .rodata
	.align 8
tmp.212:
	.double 12.0
	.section .rodata
	.align 8
tmp.213:
	.double 13.0
	.section .rodata
	.align 8
tmp.214:
	.double 14.0
	.section .rodata
	.align 8
tmp.215:
	.double 2.0
	.globl target
	.text
target:
	pushq %rbp
	movq %rsp, %rbp
	subq $16, %rsp
	movsd glob0+0(%rip), %xmm13
	mulsd tmp.180+0(%rip), %xmm13
	movsd glob10+0(%rip), %xmm0
	divsd tmp.181+0(%rip), %xmm0
	subsd tmp.182+0(%rip), %xmm0
	movsd glob10+0(%rip), %xmm1
	divsd tmp.183+0(%rip), %xmm1
	subsd tmp.184+0(%rip), %xmm1
	movsd glob2+0(%rip), %xmm2
	mulsd tmp.185+0(%rip), %xmm2
	movl $1, %r10d
	cvtsi2sdl %r10d, %xmm12
	subsd %xmm12, %xmm2
	movsd tmp.186+0(%rip), %xmm3
	subsd glob2+0(%rip), %xmm3
	mulsd glob1+0(%rip), %xmm3
	movsd glob10+0(%rip), %xmm4
	divsd tmp.187+0(%rip), %xmm4
	mulsd glob1+0(%rip), %xmm4
	movsd glob10+0(%rip), %xmm5
	addsd tmp.188+0(%rip), %xmm5
	movl $2, %r10d
	cvtsi2sdl %r10d, %xmm12
	divsd %xmm12, %xmm5
	movsd tmp.189+0(%rip), %xmm6
	mulsd glob2+0(%rip), %xmm6
	addsd tmp.190+0(%rip), %xmm6
	movsd glob2+0(%rip), %xmm7
	mulsd glob2+0(%rip), %xmm7
	mulsd tmp.191+0(%rip), %xmm7
	movsd glob1+0(%rip), %xmm8
	addsd glob2+0(%rip), %xmm8
	mulsd tmp.192+0(%rip), %xmm8
	movsd glob2+0(%rip), %xmm9
	addsd tmp.193+0(%rip), %xmm9
	mulsd tmp.194+0(%rip), %xmm9
	movsd glob10+0(%rip), %xmm10
	addsd tmp.195+0(%rip), %xmm10
	mulsd glob1+0(%rip), %xmm10
	movsd glob1+0(%rip), %xmm11
	addsd glob2+0(%rip), %xmm11
	mulsd tmp.196+0(%rip), %xmm11
	movsd glob2+0(%rip), %xmm12
	mulsd tmp.197+0(%rip), %xmm12
	addsd tmp.198+0(%rip), %xmm12
	movsd %xmm13, glob_zero+0(%rip)
	movsd glob2+0(%rip), %xmm13
	mulsd tmp.199+0(%rip), %xmm13
	movsd %xmm0, glob_one+0(%rip)
	movsd %xmm1, glob_two+0(%rip)
	movsd %xmm2, glob_three+0(%rip)
	movsd %xmm3, glob_four+0(%rip)
	movsd %xmm4, glob_five+0(%rip)
	movsd %xmm5, glob_six+0(%rip)
	movsd %xmm6, glob_seven+0(%rip)
	movsd %xmm7, glob_eight+0(%rip)
	movsd %xmm8, glob_nine+0(%rip)
	movsd %xmm9, glob_ten+0(%rip)
	movsd %xmm10, glob_eleven+0(%rip)
	movsd %xmm11, glob_twelve+0(%rip)
	movsd %xmm12, glob_thirteen+0(%rip)
	movsd %xmm13, glob_fourteen+0(%rip)
	call incr_glob1
	movsd glob_zero+0(%rip), %xmm0
	movsd tmp.200+0(%rip), %xmm1
	call check_one_double
	movsd glob_one+0(%rip), %xmm0
	movsd tmp.201+0(%rip), %xmm1
	call check_one_double
	movsd glob_two+0(%rip), %xmm0
	movsd tmp.202+0(%rip), %xmm1
	call check_one_double
	movsd glob_three+0(%rip), %xmm0
	movsd tmp.203+0(%rip), %xmm1
	call check_one_double
	movsd glob_four+0(%rip), %xmm0
	movsd tmp.204+0(%rip), %xmm1
	call check_one_double
	movsd glob_five+0(%rip), %xmm0
	movsd tmp.205+0(%rip), %xmm1
	call check_one_double
	movsd glob_six+0(%rip), %xmm0
	movsd tmp.206+0(%rip), %xmm1
	call check_one_double
	movsd glob_seven+0(%rip), %xmm0
	movsd tmp.207+0(%rip), %xmm1
	call check_one_double
	movsd glob_eight+0(%rip), %xmm0
	movsd tmp.208+0(%rip), %xmm1
	call check_one_double
	movsd glob_nine+0(%rip), %xmm0
	movsd tmp.209+0(%rip), %xmm1
	call check_one_double
	movsd glob_ten+0(%rip), %xmm0
	movsd tmp.210+0(%rip), %xmm1
	call check_one_double
	movsd glob_eleven+0(%rip), %xmm0
	movsd tmp.211+0(%rip), %xmm1
	call check_one_double
	movsd glob_twelve+0(%rip), %xmm0
	movsd tmp.212+0(%rip), %xmm1
	call check_one_double
	movsd glob_thirteen+0(%rip), %xmm0
	movsd tmp.213+0(%rip), %xmm1
	call check_one_double
	movsd glob_fourteen+0(%rip), %xmm0
	movsd tmp.214+0(%rip), %xmm1
	call check_one_double
	movsd glob1+0(%rip), %xmm0
	movsd tmp.215+0(%rip), %xmm1
	call check_one_double
	movl $0, %eax
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
	.globl glob0
	.data
	.align 8
glob0:
	.double 0.0
	.globl glob1
	.data
	.align 8
glob1:
	.double 1.0
	.globl glob2
	.data
	.align 8
glob2:
	.double 2.0
	.globl glob10
	.data
	.align 8
glob10:
	.double 10.0
	.globl glob_zero
	.data
	.align 8
glob_zero:
	.double 0.0
	.globl glob_one
	.data
	.align 8
glob_one:
	.double 0.0
	.globl glob_two
	.data
	.align 8
glob_two:
	.double 0.0
	.globl glob_three
	.data
	.align 8
glob_three:
	.double 0.0
	.globl glob_four
	.data
	.align 8
glob_four:
	.double 0.0
	.globl glob_five
	.data
	.align 8
glob_five:
	.double 0.0
	.globl glob_six
	.data
	.align 8
glob_six:
	.double 0.0
	.globl glob_seven
	.data
	.align 8
glob_seven:
	.double 0.0
	.globl glob_eight
	.data
	.align 8
glob_eight:
	.double 0.0
	.globl glob_nine
	.data
	.align 8
glob_nine:
	.double 0.0
	.globl glob_ten
	.data
	.align 8
glob_ten:
	.double 0.0
	.globl glob_eleven
	.data
	.align 8
glob_eleven:
	.double 0.0
	.globl glob_twelve
	.data
	.align 8
glob_twelve:
	.double 0.0
	.globl glob_thirteen
	.data
	.align 8
glob_thirteen:
	.double 0.0
	.globl glob_fourteen
	.data
	.align 8
glob_fourteen:
	.double 0.0
	.section	.note.GNU-stack,"",@progbits
