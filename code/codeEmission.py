
def printFunction(function):
    output = '\t.globl {0}\n{0}:'.format(function.identifier)
    for i in function.insList:
        output += '\n\t{0}'.format(i)
        
    output += '\n'
    return output

def outputAsmFile(ass):    
    output = printFunction(ass.function)

    output += '\t.section	.note.GNU-stack,"",@progbits\n'

    print(output)
    return output