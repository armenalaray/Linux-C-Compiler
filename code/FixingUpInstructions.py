import sys
import ctypes

import assemblyGenerator

def areMemoryOperands(src, dst):
    #        memory data indexed

    #memory  mm    md    mi

    #data    dm    dd    di

    #indexed im    id    ii

    if (type(src) == assemblyGenerator.MemoryOperand and type(dst) == assemblyGenerator.MemoryOperand) or (type(src) == assemblyGenerator.MemoryOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.MemoryOperand and type(dst) == assemblyGenerator.Indexed) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.MemoryOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.Indexed) or (type(src) == assemblyGenerator.Indexed and type(dst) == assemblyGenerator.MemoryOperand) or (type(src) == assemblyGenerator.Indexed and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.Indexed and type(dst) == assemblyGenerator.Indexed):
        return True
    
    return False

def calculateStackAdjustment(bytesForLocals, calleSavedCount):
    calleSavedBytes = 8*calleSavedCount

    totalStackBytes = calleSavedBytes + bytesForLocals

    print("original:",totalStackBytes)

    totalStackBytes = totalStackBytes + (16 - totalStackBytes % 16)
    print("rounded:",totalStackBytes)

    adjustment = totalStackBytes - calleSavedBytes
    print("adjustment:",adjustment)
    
    return adjustment

def FixingUpTopLevel(topLevel, backendSymbolTable):
    match topLevel:
        case assemblyGenerator.StaticVariable():
            pass
        case assemblyGenerator.Function(identifier = identifier, global_ = global_, insList = insList, stackOffset = stackOffset):
            offset = stackOffset
            
            funEntry = backendSymbolTable[identifier]
            callee = list(funEntry.calleeSavedRegs)

            adjustment = calculateStackAdjustment(-offset, len(callee))

            newList = []
            newList.insert(0,
                           assemblyGenerator.BinaryInstruction(assemblyGenerator.BinaryOperator(assemblyGenerator.BinopType.Sub), 
                                                               assemblyGenerator.Quadword(), 
                                                               assemblyGenerator.ImmediateOperand(adjustment), 
                                                               assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.SP))))
            
            for operand in callee:
                newList.append(assemblyGenerator.PushInstruction(operand))
            
            callee.reverse()

            oldSize = len(newList)

            for index, i in enumerate(insList):
                
                match i:
                    
                    case assemblyGenerator.MovSXInstruction(srcType = srcType, dstType = dstType, sourceO = sourceO, destO = destO):

                        #Mov(Longword, Imm(10), Reg(R10))
                        
                        #Movsx(Reg(R10), Reg(R11))

                        #Mov(Quadword, Reg(R11), Stack(-16))

                        #No puede ser un immediate

                        instruction0 = None
                        if type(sourceO) == assemblyGenerator.ImmediateOperand:
                            regr10 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))
                            instruction0 = assemblyGenerator.MovInstruction(srcType, sourceO, regr10)
                            i.sourceO = regr10


                        instruction2 = None
                        if type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:
                            regr11 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))
                            i.destO = regr11
                            instruction2 = assemblyGenerator.MovInstruction(dstType, regr11, destO)


                        if instruction0:
                            newList.append(instruction0)

                        newList.append(i)

                        if instruction2:
                            newList.append(instruction2)

                    case assemblyGenerator.MovZeroExtendIns(srcType = srcType, dstType = dstType, sourceO = sourceO, destO = destO):
                        
                        #if sourceO is immediate 
                        match srcType:
                            case assemblyGenerator.Byte():    
                                instruction0 = None
                                if type(sourceO) == assemblyGenerator.ImmediateOperand:
                                    regr10 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))
                                    instruction0 = assemblyGenerator.MovInstruction(srcType, sourceO, regr10)
                                    i.sourceO = regr10


                                instruction2 = None
                                if type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:
                                    regr11 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))
                                    i.destO = regr11
                                    instruction2 = assemblyGenerator.MovInstruction(dstType, regr11, destO)


                                if instruction0:
                                    newList.append(instruction0)

                                newList.append(i)

                                if instruction2:
                                    newList.append(instruction2)
                            
                            case assemblyGenerator.Longword():
                                if type(destO) == assemblyGenerator.RegisterOperand:
                                    instruction0 = assemblyGenerator.MovInstruction(assemblyGenerator.Longword(), sourceO, destO)
                                    newList.append(instruction0)

                                elif type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:

                                    instruction0 = assemblyGenerator.MovInstruction(assemblyGenerator.Longword(), sourceO, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                                    instruction1 = assemblyGenerator.MovInstruction(assemblyGenerator.Quadword(), assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), destO)

                                    newList.append(instruction0)
                                    newList.append(instruction1)

                    case assemblyGenerator.MovInstruction(assType=assType, sourceO=src, destO=dst):

                        def fixMemoryOpBothInt(src, dst):
                            if areMemoryOperands(src, dst):               
                                i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                instruction = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)), dst)

                                newList.append(i)
                                newList.append(instruction)

                        match assType:
                            case assemblyGenerator.Double():
                                if areMemoryOperands(src, dst):                            
                                    i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14))

                                    instruction = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14)), dst)

                                    newList.append(i)
                                    newList.append(instruction)
                            
                            case assemblyGenerator.Byte():
                                fixMemoryOpBothInt(src, dst)
                            
                            case assemblyGenerator.Longword():
                                fixMemoryOpBothInt(src, dst)

                            case assemblyGenerator.Quadword():

                                fixMemoryOpBothInt(src, dst)

                                if type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:
                                    #breakpoint()
                                    instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                    i.sourceO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                    newList.append(instructionImm)
                                    newList.append(i)
                                

                    case assemblyGenerator.IDivInstruction(assType=assType, divisor=div):
                        match div:
                            case assemblyGenerator.ImmediateOperand():
                                i.divisor = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                instruction = assemblyGenerator.MovInstruction(assType, div, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                newList.append(instruction)
                                newList.append(i)
                    
                    case assemblyGenerator.DivInstruction(assType=assType, divisor=div):
                        #mov imm(2), r10
                        #div r10
                        match div:
                            case assemblyGenerator.ImmediateOperand():
                                i.divisor = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                instruction = assemblyGenerator.MovInstruction(assType, div, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                newList.append(instruction)
                                newList.append(i)
                        

                    case assemblyGenerator.PushInstruction(operand = operand):
                        
                        if type(operand) == assemblyGenerator.RegisterOperand:

                            if type(operand.register.register) == assemblyGenerator.SSERegisterType:

                                instruction0 = assemblyGenerator.BinaryInstruction(assemblyGenerator.BinaryOperator(assemblyGenerator.BinopType.Sub), assemblyGenerator.Quadword(), assemblyGenerator.ImmediateOperand(8), assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.SP)))

                                instruction1 = assemblyGenerator.MovInstruction(assemblyGenerator.Double(), operand, assemblyGenerator.MemoryOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.SP), 0))

                                newList.append(instruction0)
                                newList.append(instruction1)


                        elif type(operand) == assemblyGenerator.ImmediateOperand and operand.imm > pow(2, 31) - 1:
                            #print(op0.imm)
                            instructionImm = assemblyGenerator.MovInstruction(assType, operand, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                            i.operand = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                            newList.append(instructionImm)
                            newList.append(i)

                    case assemblyGenerator.Cvtsi2sd(assType = assType, sourceO = sourceO, destO = destO):
                        #the source cant be a constant and the destination must be a register

                        instruction0 = None
                        if type(sourceO) == assemblyGenerator.ImmediateOperand:
                            regr10 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))
                            instruction0 = assemblyGenerator.MovInstruction(assType, sourceO, regr10)
                            i.sourceO = regr10


                        instruction2 = None

                        if type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:
                            regr11 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))
                            i.destO = regr11
                            instruction2 = assemblyGenerator.MovInstruction(assemblyGenerator.Double(), regr11, destO)

                            
                        if instruction0:
                            newList.append(instruction0)

                        newList.append(i)

                        if instruction2:
                            newList.append(instruction2)
                        pass

                    case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
                        
                        if type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:
                            
                            i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                            i0 = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), destO)
                            
                            newList.append(i)
                            newList.append(i0)

                    case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                        
                        if type(destO) == assemblyGenerator.MemoryOperand or type(destO) == assemblyGenerator.DataOperand or type(destO) == assemblyGenerator.Indexed:
                            
                            #lea src, r11
                            #mov r11, dst

                            i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                            i0 = assemblyGenerator.MovInstruction(assemblyGenerator.Quadword(), assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), destO)
                            
                            newList.append(i)
                            newList.append(i0)
                    
                    
                    case assemblyGenerator.CompInst(assType=assType, operand0=op0, operand1=op1):
                        
                        match assType:
                            case assemblyGenerator.Double():
                                #It must be a register
                                #comisd

                                if type(op1) != assemblyGenerator.RegisterOperand:
                                    
                                    instruction0 = assemblyGenerator.MovInstruction(assType, i.operand1, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15)))

                                    i.operand1 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))

                                    newList.append(instruction0)
                                    newList.append(i)


                            case _:
                                
                                if areMemoryOperands(op0, op1):
                                    instruction = assemblyGenerator.MovInstruction(assType, i.operand0, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                    i.operand0 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                    newList.append(instruction)
                                    newList.append(i)

                                else:

                                    #aqui se checa si los dos son immediates
                                    instruction0 = None
                                    if type(op1) == assemblyGenerator.ImmediateOperand:
                                        #mov dst, reg11
                                        #mov src, reg10
                                        #cmp r10, reg11

                                        instruction0 = assemblyGenerator.MovInstruction(assType, i.operand1, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                                        i.operand1 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                                        #newList.append(instruction)
                                        #newList.append(i)

                                    instructionImm = None
                                    
                                    if type(op0) == assemblyGenerator.ImmediateOperand and op0.imm > pow(2, 31) - 1:
                                        print(op0.imm)
                                        instructionImm = assemblyGenerator.MovInstruction(assType, op0, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                        i.operand0 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))



                                    if instruction0:
                                        newList.append(instruction0)

                                    if instructionImm:
                                        newList.append(instructionImm)

                                    newList.append(i)                                


                    case assemblyGenerator.BinaryInstruction(assType=assType, operator=op, src=src, dest=dst):

                        match assType:
                            case assemblyGenerator.Double():
                                
                                if op.operator == assemblyGenerator.BinopType.Add or op.operator == assemblyGenerator.BinopType.Sub or op.operator == assemblyGenerator.BinopType.Mult or op.operator == assemblyGenerator.BinopType.DivDouble or op.operator == assemblyGenerator.BinopType.Xor:   

                                    if type(dst) != assemblyGenerator.RegisterOperand:
                                        #print("Ale:", assType.type)
                                        
                                        instruction0 = assemblyGenerator.MovInstruction(assType, i.dest, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15)))

                                        i.dest = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))

                                        instruction1 = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15)), dst)


                                        newList.append(instruction0)
                                        newList.append(i)
                                        newList.append(instruction1)

                                elif op.operator == assemblyGenerator.BinopType.And or op.operator == assemblyGenerator.BinopType.Or:

                                    if areMemoryOperands(src, dst):
                                        #Mov src, reg
                                        #and  reg, dst
                                        
                                        instruction = assemblyGenerator.MovInstruction(assType, i.src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14)))

                                        i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14))

                                        newList.append(instruction)
                                        newList.append(i)

                                    elif type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

                                        instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14)))

                                        i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM14))

                                        newList.append(instructionImm)
                                        newList.append(i)
                                

                            case _:
                                match op.operator:

                                    case assemblyGenerator.BinopType.Mult:
                            
                                        instruction0 = None
                                        instruction1 = None
                                        
                                        if type(dst) == assemblyGenerator.MemoryOperand or type(dst) == assemblyGenerator.DataOperand or type(dst) == assemblyGenerator.Indexed:

                                            instruction0 = assemblyGenerator.MovInstruction(assType, i.dest, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                                            instruction1 = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), i.dest)

                                            i.dest = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                                        #newList.append(instruction0)
                                        #newList.append(i)
                                        #newList.append(instruction1)

                                        instructionImm = None
                                        if type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

                                            instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                        if instruction0:
                                            newList.append(instruction0)

                                        if instructionImm:
                                            newList.append(instructionImm)

                                        newList.append(i)

                                        if instruction1:
                                            newList.append(instruction1)

                                    case assemblyGenerator.BinopType.Add:
                                        
                                        #the operands cant be both memory addresses 

                                        if areMemoryOperands(src, dst):
                                            instruction = assemblyGenerator.MovInstruction(assType, i.src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instruction)
                                            newList.append(i)

                                        elif type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

                                            instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instructionImm)
                                            newList.append(i)

                                    case assemblyGenerator.BinopType.Sub:
                                        
                                        if areMemoryOperands(src, dst):
                                            instruction = assemblyGenerator.MovInstruction(assType, i.src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instruction)
                                            newList.append(i)

                                        elif type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

                                            instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instructionImm)
                                            newList.append(i)

                        
                    case assemblyGenerator.ReturnInstruction():

                        for operand in callee:
                            newList.append(assemblyGenerator.Pop(operand))

                        newList.append(i)

                    case assemblyGenerator.CallInstruction():
                        pass

                    case assemblyGenerator.SetCCInst():
                        pass

                    
                    
                    #case _:
                    #    print("Invalid Instruction fixup. {0}".format(type(i)))
                    #    sys.exit(1)                                        
                    
                                    
                if len(newList) == oldSize:
                    newList.append(i)

                oldSize = len(newList)

            topLevel.insList = newList
    

def FixingUpInstructions(ass, backendSymbolTable):
    for topLevel in ass.topLevelList:
        FixingUpTopLevel(topLevel, backendSymbolTable)

    
