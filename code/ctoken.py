import os
import re
from enum import Enum

class TokenType(Enum):
    NULL = 1
    IDENTIFIER = 2
    CONSTANT = 3
    INT_KW = 4
    VOID_KW = 5
    RETURN_KW = 6
    OPEN_PAREN = 7
    CLOSE_PAREN = 8
    OPEN_BRACE = 9
    CLOSE_BRACE = 10
    SEMICOLON = 11
    TILDE = 12
    HYPHEN = 13
    TWOHYPHENS = 14

def Lex(buffer):
    tokenList = []

    while buffer != r'':
        #breakpoint()

        #print(buffer)

        is_wspace = r"\s+"
        wspace = re.match(is_wspace, buffer)
        if wspace:
            buffer = wspace.string[wspace.span()[1]:]

        #print(buffer)

        is_not = r"\d+[a-zA-Z]"
        is_not_valid = re.match(is_not, buffer)
        if is_not_valid:
            #raise Exception("Error invalid token: {0}".format(buffer))
            print("Error invalid token: {0}".format(buffer))
            #aqui se remueve pero yo lo tengo abierto
            os.remove(iFile)
            sys.exit(1)


        is_numeric = r"\d+"
        numeric = re.match(is_numeric, buffer)
        if numeric:
            
            tokenList.append((numeric.group(), TokenType.CONSTANT))

            buffer = numeric.string[numeric.span()[1]:]
            #print(buffer)
        else:
            is_dd = r"--"
            dd = re.match(is_dd, buffer)
            if dd:
                tokenList.append(("--", TokenType.TWOHYPHENS))
                buffer = dd.string[dd.span()[1]:]
                #print(buffer)
        
            else:
                is_alphanumeric = r"[a-zA-Z_]\w*"
                alphanumeric = re.match(is_alphanumeric, buffer)
                if alphanumeric:
                    
                    match alphanumeric.group():
                        case "int":
                            tokenList.append(("int", TokenType.INT_KW))
                            
                        case "void":
                            tokenList.append(("void", TokenType.VOID_KW))
                            
                        case "return":
                            tokenList.append(("return", TokenType.RETURN_KW))

                        case _:
                            tokenList.append((alphanumeric.group(), TokenType.IDENTIFIER))

                    buffer = alphanumeric.string[alphanumeric.span()[1]:]
                    #print(buffer)
                else:
                    is_char = r"[(){};~-]"
                    char = re.match(is_char, buffer)
                    if char:
                        #print(char)
                        match char.group():
                            case "(":
                                tokenList.append(("(", TokenType.OPEN_PAREN))
                                
                            case ")":
                                tokenList.append((")", TokenType.CLOSE_PAREN))

                            case "{":
                                tokenList.append(("{", TokenType.OPEN_BRACE))
                                
                            case "}":
                                tokenList.append(("}", TokenType.CLOSE_BRACE))
                                
                            case ";":
                                tokenList.append((";", TokenType.SEMICOLON))
                            case "~":
                                tokenList.append(("~", TokenType.TILDE))
                            case "-":
                                tokenList.append(("-", TokenType.HYPHEN))
                                

                        #aqui tiene que ser keyword
                        buffer = char.string[char.span()[1]:]
                        #print(buffer)
                    else:
                        if buffer != '':
                            #raise Exception("Error invalid token: {0}".format(buffer))
                            print("Error invalid token: {0}".format(buffer))
                            os.remove(iFile)
                            sys.exit(1)

    #aqui termina el while con la lista
    print(tokenList)

    return tokenList
