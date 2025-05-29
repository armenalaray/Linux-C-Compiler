import sys
import assemblyGenerator

def FixingUpTopLevel(topLevel):
    match topLevel:
        case assemblyGenerator.StaticVariable():
            pass
        case assemblyGenerator.Function(identifier = identifier, global_ = global_, insList = insList, stackOffset = stackOffset):
            offset = stackOffset

            offset = offset - offset % 16
            print(offset)


            newList = []
            newList.insert(0,assemblyGenerator.BinaryInstruction(assemblyGenerator.BinaryOperator(assemblyGenerator.BinopType.Sub), assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.QUADWORD), assemblyGenerator.ImmediateOperand(-offset), assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.SP))))

            oldSize = len(newList)

            for index, i in enumerate(insList):
                
                match i:
                    
                    case assemblyGenerator.MovSXInstruction(sourceO = sourceO, destO = destO):

                        #Mov(Longword, Imm(10), Reg(R10))
                        
                        #Movsx(Reg(R10), Reg(R11))

                        #Mov(Quadword, Reg(R11), Stack(-16))

                        instruction0 = None
                        if type(sourceO) == assemblyGenerator.ImmediateOperand:
                            regr10 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                            instruction0 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.LONGWORD), sourceO, regr10)

                            i.sourceO = regr10


                        instruction2 = None
                        if type(destO) == assemblyGenerator.StackOperand or type(destO) == assemblyGenerator.DataOperand:
                            regr11 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))
                            
                            i.destO = regr11

                            instruction2 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.QUADWORD), regr11, destO)

                            
                        if instruction0:
                            newList.append(instruction0)

                        newList.append(i)

                        if instruction2:
                            newList.append(instruction2)

                    case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                        
                        if type(destO) == assemblyGenerator.RegisterOperand:
                            instruction0 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.LONGWORD), sourceO, destO)

                            newList.append(instruction0)
                        elif type(destO) == assemblyGenerator.StackOperand or type(destO) == assemblyGenerator.DataOperand:
                            instruction0 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.LONGWORD), sourceO, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                            instruction1 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.QUADWORD), assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), destO)

                            newList.append(instruction0)
                            newList.append(instruction1)


                                

                    case assemblyGenerator.MovInstruction(assType=assType, sourceO=src, destO=dst):
                        #stack - stack
                        #data - stack
                        #data - data
                        #stack - data

                        if (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.DataOperand):
                            
                            i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                            instruction = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)), dst)


                            #mov src, reg
                            #mov reg, dst
                            newList.append(i)
                            newList.append(instruction)
                        
                        elif type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

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
                        if type(operand) == assemblyGenerator.ImmediateOperand and operand.imm > pow(2, 31) - 1:
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
                        if type(destO) == assemblyGenerator.StackOperand or type(destO) == assemblyGenerator.DataOperand:
                            regr11 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))
                            
                            i.destO = regr11

                            instruction2 = assemblyGenerator.MovInstruction(assemblyGenerator.AssemblySize(assemblyGenerator.AssemblyType.DOUBLE), regr11, destO)

                            
                        if instruction0:
                            newList.append(instruction0)

                        newList.append(i)

                        if instruction2:
                            newList.append(instruction2)
                        pass

                    case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
                        
                        if type(destO) == assemblyGenerator.StackOperand or type(destO) == assemblyGenerator.DataOperand:
                            
                            i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                            i0 = assemblyGenerator.MovInstruction(assType, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), destO)
                            
                            newList.append(i)
                            newList.append(i0)
                    
                    
                    case assemblyGenerator.CompInst(assType=assType, operand0=op0, operand1=op1):
                        
                        match assType.type:
                            case assemblyGenerator.AssemblyType.DOUBLE:
                                #It must be a register
                                #comisd

                                if type(op1) != assemblyGenerator.RegisterOperand:
                                    print("Ale:", assType.type)
                                    
                                    instruction0 = assemblyGenerator.MovInstruction(assType, i.operand1, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15)))

                                    i.operand1 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))

                                    newList.append(instruction0)
                                    newList.append(i)


                            case _:
                                print("Ale:", assType.type)

                                if (type(op0) == assemblyGenerator.StackOperand and type(op1) == assemblyGenerator.StackOperand) or (type(op0) == assemblyGenerator.DataOperand and type(op1) == assemblyGenerator.DataOperand) or (type(op0) == assemblyGenerator.DataOperand and type(op1) == assemblyGenerator.StackOperand) or (type(op0) == assemblyGenerator.StackOperand and type(op1) == assemblyGenerator.DataOperand):
                            
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
                        match assType.type:
                            case assemblyGenerator.AssemblyType.DOUBLE:
                                
                                #print(op.operator)

                                if op.operator == assemblyGenerator.BinopType.Add or op.operator == assemblyGenerator.BinopType.Sub or op.operator == assemblyGenerator.BinopType.Mult or op.operator == assemblyGenerator.BinopType.DivDouble or op.operator == assemblyGenerator.BinopType.Xor:   

                                    if type(dst) != assemblyGenerator.RegisterOperand:
                                        print("Ale:", assType.type)
                                        
                                        instruction0 = assemblyGenerator.MovInstruction(assType, i.dest, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15)))

                                        i.dest = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.SSERegisterType.XMM15))

                                        newList.append(instruction0)
                                        newList.append(i)
                                pass

                            case _:
                                print("Ale:", assType.type)
                                match op.operator:

                                    case assemblyGenerator.BinopType.Mult:
                            
                                        instruction0 = None
                                        instruction1 = None
                                        
                                        if type(dst) == assemblyGenerator.StackOperand or type(dst) == assemblyGenerator.DataOperand:

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
                                        
                                        if (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.DataOperand):
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

                                        if (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.DataOperand):
                                            instruction = assemblyGenerator.MovInstruction(assType, i.src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instruction)
                                            newList.append(i)

                                        elif type(src) == assemblyGenerator.ImmediateOperand and src.imm > pow(2, 31) - 1:

                                            instructionImm = assemblyGenerator.MovInstruction(assType, src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                            i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                            newList.append(instructionImm)
                                            newList.append(i)
                                        pass

                        

                            

                    case assemblyGenerator.ReturnInstruction():
                        pass

                    case assemblyGenerator.CallInstruction():
                        pass

                    case assemblyGenerator.SetCCInst():
                        pass
                    
                    

                    case _:
                        print("Invalid Instruction fixup. {0}".format(type(i)))
                        sys.exit(1)                                        
                    
                                    
                if len(newList) == oldSize:
                    newList.append(i)

                oldSize = len(newList)

            topLevel.insList = newList
    

def FixingUpInstructions(ass):
    for topLevel in ass.topLevelList:
        FixingUpTopLevel(topLevel)

    
