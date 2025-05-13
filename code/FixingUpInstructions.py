import assemblyGenerator

def FixUpFuncDef(funcDef):

    offset = funcDef.stackOffset

    offset = offset - offset % 16
    print(offset)

    funcDef.insList.insert(0,AllocateStackInstruction(-offset))

    newList = []
    oldSize = len(newList)

    for index, i in enumerate(funcDef.insList):
        
        match i:
            case MovInstruction(sourceO=src, destO=dst):
                if type(src) == StackOperand and type(dst) == StackOperand:
                    
                    i.destO = RegisterOperand(Register(RegisterType.R10))

                    instruction = MovInstruction(RegisterOperand(Register(RegisterType.R10)),dst)

                    newList.append(i)
                    newList.append(instruction)
                
            
            case IDivInstruction(divisor=div):
                match div:
                    case ImmediateOperand():
                        i.divisor = RegisterOperand(Register(RegisterType.R10))
                        instruction = MovInstruction(div, RegisterOperand(Register(RegisterType.R10)))

                        newList.append(instruction)
                        newList.append(i)
            
            case CompInst(operand0=op0, operand1=op1):
                if type(op0) == StackOperand and type(op1) == StackOperand:
                    
                    instruction = MovInstruction(i.operand0, RegisterOperand(Register(RegisterType.R10)))

                    i.operand0 = RegisterOperand(Register(RegisterType.R10))

                    newList.append(instruction)
                    newList.append(i)
                elif type(op1) == ImmediateOperand:
                    instruction = MovInstruction(i.operand1, RegisterOperand(Register(RegisterType.R11)))

                    i.operand1 = RegisterOperand(Register(RegisterType.R11))

                    newList.append(instruction)
                    newList.append(i)
                    

            case BinaryInstruction(operator=op, src=src, dest=dst):
                
                if type(dst) == StackOperand:
                    match op:
                            case BinaryOperator(operator=o):
                                #print(o)
                                if o == BinopType.Mult:
                                    instruction0 = MovInstruction(i.dest, RegisterOperand(Register(RegisterType.R11)))

                                    instruction1 = MovInstruction(RegisterOperand(Register(RegisterType.R11)), i.dest)

                                    i.dest = RegisterOperand(Register(RegisterType.R11))



                                    newList.append(instruction0)
                                    newList.append(i)
                                    newList.append(instruction1)


                if type(src) == StackOperand and type(dst) == StackOperand:
                    match op:
                        case BinaryOperator(operator=o):
                            #print(o)
                            if o == BinopType.Sub or o == BinopType.Add:

                                instruction = MovInstruction(i.src, RegisterOperand(Register(RegisterType.R10)))

                                i.src = RegisterOperand(Register(RegisterType.R10))

                                newList.append(instruction)
                                newList.append(i)
                                
                            
        if len(newList) == oldSize:
            newList.append(i)

        oldSize = len(newList)

    funcDef.insList = newList


def FixingUpTopLevel(topLevel):
    match topLevel:
        case assemblyGenerator.StaticVariable():
            pass
        case assemblyGenerator.Function(identifier = identifier, global_ = global_, insList = insList, stackOffset = stackOffset):
            offset = stackOffset

            offset = offset - offset % 16
            print(offset)


            newList = []
            newList.insert(0,assemblyGenerator.AllocateStackInstruction(-offset))

            oldSize = len(newList)

            for index, i in enumerate(insList):
                
                match i:
                    case assemblyGenerator.MovInstruction(sourceO=src, destO=dst):
                        #stack - stack
                        #data - stack
                        #data - data
                        #stack - data

                        if (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.DataOperand):
                            
                            i.destO = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                            instruction = assemblyGenerator.MovInstruction(assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)),dst)

                            newList.append(i)
                            newList.append(instruction)
                        
                    
                    case assemblyGenerator.IDivInstruction(divisor=div):
                        match div:
                            case assemblyGenerator.ImmediateOperand():
                                i.divisor = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                instruction = assemblyGenerator.MovInstruction(div, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                newList.append(instruction)
                                newList.append(i)
                    
                    case assemblyGenerator.CompInst(operand0=op0, operand1=op1):
                        if (type(op0) == assemblyGenerator.StackOperand and type(op1) == assemblyGenerator.StackOperand) or (type(op0) == assemblyGenerator.DataOperand and type(op1) == assemblyGenerator.DataOperand) or (type(op0) == assemblyGenerator.DataOperand and type(op1) == assemblyGenerator.StackOperand) or (type(op0) == assemblyGenerator.StackOperand and type(op1) == assemblyGenerator.DataOperand):
                            
                            instruction = assemblyGenerator.MovInstruction(i.operand0, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                            i.operand0 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                            newList.append(instruction)
                            newList.append(i)

                        elif type(op1) == assemblyGenerator.ImmediateOperand:
                            instruction = assemblyGenerator.MovInstruction(i.operand1, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                            i.operand1 = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                            newList.append(instruction)
                            newList.append(i)
                            

                    case assemblyGenerator.BinaryInstruction(operator=op, src=src, dest=dst):
                        
                        if type(dst) == assemblyGenerator.StackOperand or type(dst) == assemblyGenerator.DataOperand:
                            match op:
                                    case assemblyGenerator.BinaryOperator(operator=o):
                                        #print(o)
                                        if o == assemblyGenerator.BinopType.Mult:

                                            instruction0 = assemblyGenerator.MovInstruction(i.dest, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)))

                                            instruction1 = assemblyGenerator.MovInstruction(assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11)), i.dest)

                                            i.dest = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R11))

                                            newList.append(instruction0)
                                            newList.append(i)
                                            newList.append(instruction1)


                        if (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.DataOperand) or (type(src) == assemblyGenerator.DataOperand and type(dst) == assemblyGenerator.StackOperand) or (type(src) == assemblyGenerator.StackOperand and type(dst) == assemblyGenerator.DataOperand):
                            
                            match op:
                                case assemblyGenerator.BinaryOperator(operator=o):
                                    #print(o)
                                    if o == assemblyGenerator.BinopType.Sub or o == assemblyGenerator.BinopType.Add:

                                        instruction = assemblyGenerator.MovInstruction(i.src, assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10)))

                                        i.src = assemblyGenerator.RegisterOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.R10))

                                        newList.append(instruction)
                                        newList.append(i)
                                        
                                    
                if len(newList) == oldSize:
                    newList.append(i)

                oldSize = len(newList)

            topLevel.insList = newList
    

def FixingUpInstructions(ass):
    for topLevel in ass.topLevelList:
        FixingUpTopLevel(topLevel)

    
