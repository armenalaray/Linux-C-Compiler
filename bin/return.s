.globl	main

/*
este es el address de movl solo tiene que ser simbolico, no tiene que ser real!:
ATT

mov longwords 32 bits eax
quadwords 64 bits rax
*/

main:

movl	$2, %eax

/*
retq because it returns into 64 bit address
*/

ret
	
