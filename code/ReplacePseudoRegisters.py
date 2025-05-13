import typeChecker
import assemblyGenerator

def ReplaceFuncDef(funcDef, table, offset):
    for i in funcDef.insList:
        #print(type(i))
        match i:
            case MovInstruction(sourceO=src, destO=dst):
                match src:
                    case PseudoRegisterOperand(pseudo=id):

                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.sourceO = StackOperand(value)
                        
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.destO = StackOperand(value)
                        
            

            case UnaryInstruction(operator=o, dest=dst):
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.dest = StackOperand(value)

            case BinaryInstruction(operator=op, src=src, dest=dst):
                
                match src:
                    case PseudoRegisterOperand(pseudo=id):

                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.src = StackOperand(value)
                        
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.dest = StackOperand(value)
            
            case IDivInstruction(divisor=div):  
                match div:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.divisor = StackOperand(value)
            case SetCCInst(conc_code=code, operand=op):
                match op:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})

                        value = table[id] 

                        i.operand = StackOperand(value)
            case CompInst(operand0=op0, operand1=op1):
                match op0:
                    case PseudoRegisterOperand(pseudo=id):

                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.operand0 = StackOperand(value)
                        
                match op1:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.operand1 = StackOperand(value)
    
    return offset

def ReplaceOperand(operand, table, offset, symbolTable):
    match operand:
        case assemblyGenerator.PseudoRegisterOperand(pseudo=id):

            if table.get(id) == None:

                if id in symbolTable:
                    print(type(symbolTable[id].attrs))
                    match symbolTable[id].attrs:
                        case typeChecker.StaticAttributes():
                            return offset, assemblyGenerator.DataOperand(id)
                            
                
                offset -= 4
                table.update({id : offset})
                
            value = table[id] 
            
            return offset, assemblyGenerator.StackOperand(value)
    
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
            
            topLevel.stackOffset = offset
                    
    

# Replace Pseudos #2
def ReplacePseudoRegisters(ass, symbolTable):

    for topLevel in ass.topLevelList:
        ReplaceTopLevel(topLevel, symbolTable)
        #funcDef.stackOffset = offset
