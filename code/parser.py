
class ReturnStmt:
    retVal = 0
    
    def __init__(self, retVal):
        self.retVal = retVal

def takeToken(tokenList):
    tokenList
    pass

def expect(expected, tokenList):
    actual = takeToken(tokenList)
    if actual != expected:
        print("Syntax Error")
    
"""
podrias guardar el string

"""
def parseExp(tokenList):
    
    pass

def parseStatement(tokenList):
    expect("return", tokenList)
    retVal = parseExp(tokenList)
    expect(";", tokenList)
    return ReturnStmt(retVal) 

    

