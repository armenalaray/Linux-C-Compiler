import sys
import assemblyGenerator
from enum import Enum

class OperandSize(Enum):
    BYTE_8 = 1
    BYTE_4 = 2
    BYTE_1 = 3

def matchOperand(operand, output, operandSize = OperandSize.BYTE_4):

    match operand:
        case assemblyGenerator.StackOperand(offset=off):
            output += '{0}(%rbp)'.format(off)
            
        case assemblyGenerator.RegisterOperand(register=reg):
            match reg:
                case assemblyGenerator.Register(register=regi):
                    match regi:
                        case assemblyGenerator.RegisterType.AX:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%rax'
                                
                                case OperandSize.BYTE_4:
                                    output += '%eax'

                                case OperandSize.BYTE_1:
                                    output += '%al'


                        case assemblyGenerator.RegisterType.CX:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%rcx'
                                
                                case OperandSize.BYTE_4:
                                    output += '%ecx'

                                case OperandSize.BYTE_1:
                                    output += '%cl'
                                                    
                        case assemblyGenerator.RegisterType.DX:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%rdx'
                                
                                case OperandSize.BYTE_4:
                                    output += '%edx'

                                case OperandSize.BYTE_1:
                                    output += '%dl'

                        case assemblyGenerator.RegisterType.DI:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%rdi'
                                
                                case OperandSize.BYTE_4:
                                    output += '%edi'

                                case OperandSize.BYTE_1:
                                    output += '%dil'

                        case assemblyGenerator.RegisterType.SI:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%rsi'
                                
                                case OperandSize.BYTE_4:
                                    output += '%esi'

                                case OperandSize.BYTE_1:
                                    output += '%sil'

                        case assemblyGenerator.RegisterType.R8:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%r8'
                                
                                case OperandSize.BYTE_4:
                                    output += '%r8d'

                                case OperandSize.BYTE_1:
                                    output += '%r8b'

                        case assemblyGenerator.RegisterType.R9:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%r9'
                                
                                case OperandSize.BYTE_4:
                                    output += '%r9d'

                                case OperandSize.BYTE_1:
                                    output += '%r9b'

                        case assemblyGenerator.RegisterType.R10:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%r10'
                                
                                case OperandSize.BYTE_4:
                                    output += '%r10d'

                                case OperandSize.BYTE_1:
                                    output += '%r10b'
                        
                        case assemblyGenerator.RegisterType.R11:
                            match operandSize:
                                case OperandSize.BYTE_8:
                                    output += '%r11'
                                
                                case OperandSize.BYTE_4:
                                    output += '%r11d'

                                case OperandSize.BYTE_1:
                                    output += '%r11b'
                        
                        
        case assemblyGenerator.ImmediateOperand(imm=im):
            output += '${0}'.format(im)
            #print(output)
    return output

def printFunction(function, output, symbolTable):
    output += '\t.globl {0}\n{0}:\n\tpushq %rbp\n\tmovq %rsp, %rbp'.format(function.identifier)
    
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
                            case assemblyGenerator.UnopType.Not:
                                output += '\n\tnotl '
                                
                            case assemblyGenerator.UnopType.Neg:
                                output += '\n\tnegl '
                                

                output = matchOperand(dst, output)

            case assemblyGenerator.BinaryInstruction(operator=op, src=src, dest=dst):
                match op:
                    case assemblyGenerator.BinaryOperator(operator=o):
                        match o:
                            case assemblyGenerator.BinopType.Add:
                                output += '\n\taddl '
                                pass
                            case assemblyGenerator.BinopType.Sub:
                                output += '\n\tsubl '
                                pass
                            case assemblyGenerator.BinopType.Mult:
                                output += '\n\timull '
                                pass
                
                output = matchOperand(src, output)
                output += ', '
                output = matchOperand(dst, output)

            case assemblyGenerator.IDivInstruction(divisor=divisor):
                output += '\n\tidivl '
                output = matchOperand(divisor, output)
                
            case assemblyGenerator.CDQInstruction():
                output += '\n\tcdq'
            
            case assemblyGenerator.CompInst(operand0=op0, operand1=op1):
                
                output += '\n\tcmpl '
                output = matchOperand(op0, output)

                output += ', '

                output = matchOperand(op1, output)
            
            case assemblyGenerator.JumpInst(identifier=id):
                output += '\n\tjmp .L{0}'.format(id)

            case assemblyGenerator.JumpCCInst(conc_code=code, identifier=id):
                output += '\n\tj{0} .L{1}'.format(code.name, id)
                
            
            case assemblyGenerator.SetCCInst(conc_code=code, operand=op):
                output += '\n\tset{0} '.format(code.name)
                output = matchOperand(op, output, OperandSize.BYTE_1)

            case assemblyGenerator.LabelInst(identifier=id):
                output += '\n.L{0}:'.format(id)
                
            case assemblyGenerator.PushInstruction(operand = operand):
                output += "\n\tpushq "

                output = matchOperand(operand, output, OperandSize.BYTE_8)
            
            case assemblyGenerator.CallInstruction(identifier = identifier):
                if identifier in symbolTable:
                    #print(symbolTable)
                    output += "\n\tcall {0}".format(identifier)
                else:
                    output += "\n\tcall {0}@PLT".format(identifier)

            case assemblyGenerator.DeallocateStackInstruction(offset = offset):
                output += "\n\taddq ${0}, %rsp".format(offset)

            case _:
                print("Instruction {0} not added into code emission!".format(i))
                sys.exit(1)
        #output += '\n\t{0}'.format(i)
        
    output += '\n'
    return output

def outputAsmFile(ass, symbolTable):    

    output = ""
    for funcDef in ass.funcDefList:

        output = printFunction(funcDef, output, symbolTable)

    output += '\t.section	.note.GNU-stack,"",@progbits\n'

    print(output)
    return output