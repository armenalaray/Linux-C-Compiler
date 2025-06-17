import sys
import typeChecker
import assemblyGenerator


def ReplaceOperand(operand, table, offset, symbolTable):
    match operand:
        
        case assemblyGenerator.PseudoRegisterOperand(pseudo=id):

            if table.get(id) == None:

                if id in symbolTable:
                    match symbolTable[id]:
                        case assemblyGenerator.FunEntry():
                            pass
                        case assemblyGenerator.ObjEntry(assType = assType, isStatic = isStatic):
                            if isStatic:
                                return offset, assemblyGenerator.DataOperand(id)
                            
                #stack allocation
                match symbolTable[id]:
                    case assemblyGenerator.ObjEntry(assType = assType, isStatic = isStatic):
                        allocateSize = 0
                        match assType:
                            
                            case assemblyGenerator.Byte():
                                allocateSize = 1
                                offset -= allocateSize

                            case assemblyGenerator.Longword():
                                allocateSize = 4
                                offset -= allocateSize
                                offset = offset - offset % 4
                                
                            case assemblyGenerator.Quadword():
                                allocateSize = 8
                                offset -= allocateSize
                                offset = offset - offset % 8

                            case assemblyGenerator.Double():
                                allocateSize = 8
                                offset -= allocateSize
                                #esto es para alinearlo a 8 
                                offset = offset - offset % 8

                            case _:
                                print("Error")
                                sys.exit(1)
                                

                        table.update({id : offset})
            
            if table.get(id) == None:
                print("Error: Symbol not in offset table.")
                sys.exit(1)

            value = table[id] 
            return offset, assemblyGenerator.MemoryOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.BP), value) 
    
        case assemblyGenerator.PseudoMem(identifier = id, offset = offset_):

            if table.get(id) == None:

                if id in symbolTable:
                    match symbolTable[id]:
                        case assemblyGenerator.FunEntry():
                            pass
                        case assemblyGenerator.ObjEntry(assType = assType, isStatic = isStatic):
                            if isStatic:
                                return offset, assemblyGenerator.DataOperand(id)
                            
                #stack allocation
                match symbolTable[id]:
                    case assemblyGenerator.ObjEntry(assType = assType, isStatic = isStatic):
                        allocateSize = 0
                        match assType:
                            case assemblyGenerator.Byte():
                                allocateSize = 1
                                offset -= allocateSize

                            case assemblyGenerator.Longword():
                                allocateSize = 4
                                offset -= allocateSize
                                offset = offset - offset % 4
                                
                            case assemblyGenerator.Quadword():
                                allocateSize = 8
                                offset -= allocateSize
                                offset = offset - offset % 8

                            case assemblyGenerator.Double():
                                allocateSize = 8
                                offset -= allocateSize
                                #esto es para alinearlo a 8 
                                offset = offset - offset % 8
                            
                            #aqui esta el error
                            case assemblyGenerator.ByteArray(size = size, alignment = alignment):
                                offset -= size
                                offset = offset - offset % alignment

                            case _:
                                print("Error. {0}".format(assType))
                                sys.exit(1)
                                

                        table.update({id : offset})
            
            if table.get(id) == None:
                print("Error: Symbol not in offset table.")
                sys.exit(1)

            value = table[id] 
            value = value + offset_
            return offset, assemblyGenerator.MemoryOperand(assemblyGenerator.Register(assemblyGenerator.RegisterType.BP), value) 
    
            pass
        
        case assemblyGenerator.ImmediateOperand():
            pass

        case assemblyGenerator.RegisterOperand():
            pass

        case assemblyGenerator.Indexed():
            pass

        case assemblyGenerator.MemoryOperand():
            pass
        
        case assemblyGenerator.DataOperand():
            pass

        case _:
            print("Error. {0}".format(operand))
            sys.exit(1)

    return offset, None

def ReplaceTopLevel(topLevel, symbolTable):
    
    match topLevel:
        case assemblyGenerator.StaticVariable():
            pass
        case assemblyGenerator.Function(identifier = identifier, global_ = global_, insList = insList, stackOffset = stackOffset):
            offset = 0
            table = {}
            #esto es por funcion 
            for i in insList:
                #print(type(i))
                match i:
                    case assemblyGenerator.MovSXInstruction(sourceO=src, destO=dst):
                        offset, object = ReplaceOperand(src, table, offset, symbolTable)
                        if object:
                            i.sourceO = object
                        
                        offset, object = ReplaceOperand(dst, table, offset, symbolTable)
                        if object:
                            i.destO = object
                        

                    case assemblyGenerator.MovInstruction(sourceO=src, destO=dst):
                        offset, object = ReplaceOperand(src, table, offset, symbolTable)
                        if object:
                            i.sourceO = object
                        
                        offset, object = ReplaceOperand(dst, table, offset, symbolTable)
                        if object:
                            i.destO = object
                    

                    case assemblyGenerator.UnaryInstruction(operator=o, dest=dst):

                        offset, object = ReplaceOperand(dst, table, offset, symbolTable)
                        if object:
                            i.dest = object

                    case assemblyGenerator.BinaryInstruction(operator=op, src=src, dest=dst):
                        
                        offset, object = ReplaceOperand(src, table, offset, symbolTable)
                        if object:
                            i.src = object

                        offset, object = ReplaceOperand(dst, table, offset, symbolTable)
                        if object:
                            i.dest = object
                    
                    case assemblyGenerator.IDivInstruction(divisor=div):  

                        offset, object = ReplaceOperand(div, table, offset, symbolTable)
                        if object:
                            i.divisor = object
                        
                    case assemblyGenerator.SetCCInst(conc_code=code, operand=op):
                        
                        offset, object = ReplaceOperand(op, table, offset, symbolTable)
                        if object:
                            i.operand = object

                    
                    case assemblyGenerator.CompInst(operand0=op0, operand1=op1):

                        offset, object = ReplaceOperand(op0, table, offset, symbolTable)
                        if object:
                            i.operand0 = object

                        offset, object = ReplaceOperand(op1, table, offset, symbolTable)
                        if object:
                            i.operand1 = object

                    case assemblyGenerator.PushInstruction(operand=operand):
                        offset, object = ReplaceOperand(operand, table, offset, symbolTable)
                        if object:
                            i.operand = object
                        
                    case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                        offset, object = ReplaceOperand(sourceO, table, offset, symbolTable)
                        if object:
                            i.sourceO = object

                        offset, object = ReplaceOperand(destO, table, offset, symbolTable)
                        if object:
                            i.destO = object
                        
                    case assemblyGenerator.DivInstruction(divisor = divisor):
                        offset, object = ReplaceOperand(divisor, table, offset, symbolTable)
                        if object:
                            i.divisor = object


                    case assemblyGenerator.Cvtsi2sd(assType = assType, sourceO = sourceO, destO = destO):
                        offset, object = ReplaceOperand(sourceO, table, offset, symbolTable)
                        if object:
                            i.sourceO = object

                        offset, object = ReplaceOperand(destO, table, offset, symbolTable)
                        if object:
                            i.destO = object
                        

                    case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
                        offset, object = ReplaceOperand(sourceO, table, offset, symbolTable)
                        if object:
                            i.sourceO = object

                        offset, object = ReplaceOperand(destO, table, offset, symbolTable)
                        if object:
                            i.destO = object


                    case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                        offset, object = ReplaceOperand(sourceO, table, offset, symbolTable)
                        if object:
                            i.sourceO = object

                        offset, object = ReplaceOperand(destO, table, offset, symbolTable)
                        if object:
                            i.destO = object
                        

                    #These are not changed
                    case assemblyGenerator.ReturnInstruction():
                        pass

                    case assemblyGenerator.CallInstruction():
                        pass

                    case assemblyGenerator.JumpCCInst():
                        pass

                    case assemblyGenerator.LabelInst():
                        pass
                    
                    

                    #case _:
                    #    print("Invalid Assembly Instruction. {0}".format(type(i)))
                    #    sys.exit(1)
                    

            topLevel.stackOffset = offset
                    
def ReplacePseudoRegisters(ass, symbolTable):
    for topLevel in ass.topLevelList:
        ReplaceTopLevel(topLevel, symbolTable)
