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

def ReplaceTopLevel(topLevel):
    
    match topLevel:
        case assemblyGenerator.StaticVariable():
            pass
        case assemblyGenerator.Function():
            offset = 0
            table = {}
    
            pass
    pass

# Replace Pseudos #2
def ReplacePseudoRegisters(ass):

    for topLevel in ass.topLevelList:
        offset = 0
        table = {}
        offset = ReplaceTopLevel(topLevel)
        #funcDef.stackOffset = offset
