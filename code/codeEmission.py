import assemblyGenerator

def matchOperand(operand, output):
    match operand:
        case assemblyGenerator.StackOperand(offset=off):
            output += '{0}(%rbp)'.format(off)
            
        case assemblyGenerator.RegisterOperand(register=reg):
            match reg:
                case assemblyGenerator.Register(register=regi):
                    match regi:
                        case assemblyGenerator.RegisterType.AX:
                            output += '%eax'
                            
                        case assemblyGenerator.RegisterType.R10:
                            output += '%r10d'
                            
            
        case assemblyGenerator.ImmediateOperand(imm=im):
            output += '${0}'.format(im)
            #print(output)
    return output

def printFunction(function):
    output = '\t.globl {0}\n{0}:\n\tpushq %rbp\n\tmovq %rsp, %rbp'.format(function.identifier)
    for i in function.insList:
        match i:
            case assemblyGenerator.MovInstruction(sourceO=src, destO=dst):
                output += '\n\tmovl '
                
                output = matchOperand(src, output)
                
                output += ', '

                output = matchOperand(dst, output)

                

            case assemblyGenerator.ReturnInstruction():
                output += '\n\tmovq %rbp, %rsp\n\tpopq %rbp\n\tret'
                
            case assemblyGenerator.AllocateStackInstruction(offset=off):
                output += '\n\tsubq ${0}'.format(off)

                output += ', %rsp'
                
                
            case assemblyGenerator.UnaryInstruction(operator=o, dest=dst):
                #print(o)
                match o:
                    case assemblyGenerator.UnaryOperator(operator=op):
                        match op:
                            case assemblyGenerator.OperatorType.Not:
                                output += '\n\tnotl '
                                
                            case assemblyGenerator.OperatorType.Neg:
                                output += '\n\tnegl '
                                

                output = matchOperand(dst, output)

                        
                
        #output += '\n\t{0}'.format(i)
        
    output += '\n'
    return output

def outputAsmFile(ass):    
    output = printFunction(ass.function)

    output += '\t.section	.note.GNU-stack,"",@progbits\n'

    print(output)
    return output