import sys
import assemblyGenerator
from enum import Enum
import typeChecker

class OperandSize(Enum):
    BYTE_8 = 1
    BYTE_4 = 2
    BYTE_1 = 3

def matchOperand(operand, output, operandSize):

    match operand:
        case assemblyGenerator.StackOperand(offset=off):
            output += '{0}(%rbp)'.format(off)

        case assemblyGenerator.DataOperand(identifier = identifier):
            output += '{0}(%rip)'.format(identifier)
            pass
            
        case assemblyGenerator.RegisterOperand(register=reg):
            match reg:
                case assemblyGenerator.Register(register=regi):
                    match regi:
                        case assemblyGenerator.RegisterType.SP:
                            output += '%rsp'
                            
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

def printStaticInit(staticInit, output):
    match staticInit:
        case typeChecker.IntInit(int=int):
            if int == 0:
                output += '\t.zero 4\n'
            else:
                output += '\t.long {0}\n'.format(int.value)

        case typeChecker.LongInit(int=int):
            if int == 0:
                output += '\t.zero 8\n'
            else:
                output += '\t.quad {0}\n'.format(int.value)

        case typeChecker.UIntInit(int=int):
            if int == 0:
                output += '\t.zero 4\n'
            else:
                output += '\t.long {0}\n'.format(int.value)
            
        case typeChecker.ULongInit(int=int):
            if int == 0:
                output += '\t.zero 8\n'
            else:
                output += '\t.quad {0}\n'.format(int.value)

        case _:
            print("Error:")
            sys.exit(1)
    return output

def printInstructionSuffix(type, output):
    match type:
        case assemblyGenerator.AssemblyType.LONGWORD:
            output += 'l'
            
        case assemblyGenerator.AssemblyType.QUADWORD:
            output += 'q'

        case _:
            print("Invalid assembly type.")
            sys.exit(1)

    return output

def getOperandSize(type):
    operandSize = None
    match type:
        case assemblyGenerator.AssemblyType.LONGWORD:
            operandSize = OperandSize.BYTE_4
            
        case assemblyGenerator.AssemblyType.QUADWORD:
            operandSize = OperandSize.BYTE_8
        
        case _:
            print("Invalid Operand Size")
            sys.exit(1)

    return operandSize

def printTopLevel(topLevel, output, symbolTable):
    match topLevel:
        case assemblyGenerator.StaticVariable(identifier = identifier, global_ = global_, alignment = alignment, staticInit = staticInit):
            print(type(staticInit))
            
            if staticInit.int == 0:
                if global_ == True:
                    output += '\t.globl {0}\n'.format(identifier)

                output += '\t.bss\n\t.align {0}\n{1}:\n'.format(alignment, identifier)

                output = printStaticInit(staticInit, output)

            else:
                if global_ == True:
                    output += '\t.globl {0}\n'.format(identifier)

                output += '\t.data\n\t.align {0}\n{1}:\n'.format(alignment, identifier)

                output = printStaticInit(staticInit, output)

        
        case assemblyGenerator.Function(identifier = identifier, global_ = global_, insList = insList, stackOffset = stackOffset):
            if global_ == True:
                output += '\t.globl {0}\n'.format(identifier)

            output += '\t.text\n{0}:\n\tpushq %rbp\n\tmovq %rsp, %rbp'.format(identifier)
            
            for i in insList:
                match i:
                    #esq esta es un sign extend
                    case assemblyGenerator.MovSXInstruction(sourceO = sourceO, destO = destO):
                        output += '\n\tmovslq '

                        output = matchOperand(sourceO, output, OperandSize.BYTE_4)
                        
                        output += ', '

                        output = matchOperand(destO, output, OperandSize.BYTE_8) 

                        

                    case assemblyGenerator.MovInstruction(assType=assType, sourceO=src, destO=dst):
                        output += '\n\tmov'

                        #print(type(assType.type))

                        output = printInstructionSuffix(assType.type, output)
                                
                        output += ' '
                                
                        operandSize = getOperandSize(assType.type)

                        output = matchOperand(src, output, operandSize)
                        
                        output += ', '

                        output = matchOperand(dst, output, operandSize)

                        

                    case assemblyGenerator.ReturnInstruction():
                        output += '\n\tmovq %rbp, %rsp\n\tpopq %rbp\n\tret'


                    #case assemblyGenerator.AllocateStackInstruction(offset=off):
                    #    output += '\n\tsubq ${0}'.format(off)
                    #    output += ', %rsp'
                        
                        
                    case assemblyGenerator.UnaryInstruction(operator=o, assType = assType, dest=dst):
                        
                        match o:
                            case assemblyGenerator.UnaryOperator(operator=op):
                                match op:
                                    case assemblyGenerator.UnopType.Not:
                                        output += '\n\tnot'

                                    case assemblyGenerator.UnopType.Neg:
                                        output += '\n\tneg'

                        output = printInstructionSuffix(assType.type, output)

                        output += ' '                

                        operandSize = getOperandSize(assType.type)
                        output = matchOperand(dst, output, operandSize)

                    case assemblyGenerator.BinaryInstruction(operator=op, assType = assType, src=src, dest=dst):
                        match op:
                            case assemblyGenerator.BinaryOperator(operator=o):
                                match o:
                                    case assemblyGenerator.BinopType.Add:
                                        output += '\n\tadd'
                                        pass
                                    case assemblyGenerator.BinopType.Sub:
                                        output += '\n\tsub'
                                        pass
                                    case assemblyGenerator.BinopType.Mult:
                                        output += '\n\timul'
                                        pass
                        
                        output = printInstructionSuffix(assType.type, output)

                        output += ' '                

                        operandSize = getOperandSize(assType.type)

                        output = matchOperand(src, output, operandSize)
                        output += ', '
                        output = matchOperand(dst, output, operandSize)

                    case assemblyGenerator.IDivInstruction(assType = assType, divisor=divisor):
                        output += '\n\tidiv'

                        output = printInstructionSuffix(assType.type, output)

                        output += ' '                
                        
                        operandSize = getOperandSize(assType.type)
                        output = matchOperand(divisor, output, operandSize)

                    case assemblyGenerator.DivInstruction(assType = assType, divisor=divisor):
                        output += '\n\tdiv'

                        output = printInstructionSuffix(assType.type, output)

                        output += ' '                
                        
                        operandSize = getOperandSize(assType.type)
                        output = matchOperand(divisor, output, operandSize)
                    
                        
                    case assemblyGenerator.CDQInstruction(assType = assType):
                        match assType.type:
                            case assemblyGenerator.AssemblyType.LONGWORD:
                                output += '\n\tcdq'
                            case assemblyGenerator.AssemblyType.QUADWORD:
                                output += '\n\tcqo'
                            
                    
                    case assemblyGenerator.CompInst(assType = assType, operand0=op0, operand1=op1):
                        
                        #print("Ale")

                        output += '\n\tcmp'

                        output = printInstructionSuffix(assType.type, output)

                        output += ' '                

                        operandSize = getOperandSize(assType.type)

                        output = matchOperand(op0, output, operandSize)

                        output += ', '

                        output = matchOperand(op1, output, operandSize)
                    
                    case assemblyGenerator.JumpInst(identifier=id):
                        output += '\n\tjmp .L{0}'.format(id)

                    case assemblyGenerator.JumpCCInst(conc_code=code, identifier=id):
                        output += '\n\tj{0} .L{1}'.format(code.name, id)
                        
                    
                    case assemblyGenerator.SetCCInst(conc_code=code, operand=op):
                        print(type(code))
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

                    #case assemblyGenerator.DeallocateStackInstruction(offset = offset):
                    #    output += "\n\taddq ${0}, %rsp".format(offset)

                    case _:
                        print("Instruction {0} not added into code emission!".format(i))
                        sys.exit(1)

                #output += '\n\t{0}'.format(i)
                
            output += '\n'
        
        case _:
            print("Invalid Top Level {0}".format(topLevel))
            sys.exit(1)

    return output
    

def outputAsmFile(ass, symbolTable):    

    output = ""
    for topLevel in ass.topLevelList:

        output = printTopLevel(topLevel, output, symbolTable)

    output += '\t.section	.note.GNU-stack,"",@progbits\n'

    #print(output)
    return output