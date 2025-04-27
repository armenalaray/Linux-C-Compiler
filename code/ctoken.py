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
    FORWARD_SLASH = 15
    PERCENT = 16
    ASTERISK = 17
    PLUS = 18
    EXCLAMATION = 19
    GREATERT = 20
    LESST = 21
    TAMPERSANDS = 22
    TVERTICALB = 23
    TEQUALS = 24
    EXCLAMATIONEQUAL = 25
    LESSTEQUALT = 26
    GREATERTEQUALT = 27
    EQUAL = 28

def Lex(buffer):
    tokenList = []
    LineNumber = 1

    while buffer != r'':
        #breakpoint()

        #print(buffer)

        is_wspace = r"\s+"
        wspace = re.match(is_wspace, buffer)
        if wspace:
            
            is_newline = re.match(r"[\s]*\n[\s]*",wspace.group())
            if is_newline:
                LineNumber += 1
            
            #print(LineNumber)
            buffer = wspace.string[wspace.span()[1]:]

        #print(buffer)

        is_not = r"\d+[a-zA-Z]"
        is_not_valid = re.match(is_not, buffer)
        if is_not_valid:
            #raise Exception("Error invalid token: {0}".format(buffer))
            print("Error invalid token: {0} at Line: {1}".format(buffer, LineNumber))
            #aqui se remueve pero yo lo tengo abierto
            os.remove(iFile)
            sys.exit(1)


        is_numeric = r"\d+"
        numeric = re.match(is_numeric, buffer)
        if numeric:
            
            tokenList.append((numeric.group(), TokenType.CONSTANT, LineNumber))

            buffer = numeric.string[numeric.span()[1]:]
            #print(buffer)
        else:
            mList = [
                (r"--", TokenType.TWOHYPHENS), 
                (r"&&", TokenType.TAMPERSANDS), 
                (r"\|\|", TokenType.TVERTICALB), 
                (r"==", TokenType.TEQUALS), 
                (r"!=", TokenType.EXCLAMATIONEQUAL), 
                (r"<=", TokenType.LESSTEQUALT), 
                (r">=", TokenType.GREATERTEQUALT)
                ]

            dd = None

            for i in mList:
                dd = re.match(i[0], buffer)
                if dd:
                    
                    tokenList.append((dd.group(), i[1], LineNumber))
                    buffer = dd.string[dd.span()[1]:]
                
                    break
                    

            if dd == None:        
                is_alphanumeric = r"[a-zA-Z_]\w*"
                alphanumeric = re.match(is_alphanumeric, buffer)
                if alphanumeric:
                    
                    match alphanumeric.group():
                        case "int":
                            tokenList.append(("int", TokenType.INT_KW, LineNumber))
                            
                        case "void":
                            tokenList.append(("void", TokenType.VOID_KW, LineNumber))
                            
                        case "return":
                            tokenList.append(("return", TokenType.RETURN_KW, LineNumber))

                        case _:
                            tokenList.append((alphanumeric.group(), TokenType.IDENTIFIER, LineNumber))

                    buffer = alphanumeric.string[alphanumeric.span()[1]:]
                    #print(buffer)
                else:
                    is_char = r"[=><!%/*+(){};~-]"
                    char = re.match(is_char, buffer)
                    if char:
                        #print(char)
                        match char.group():
                            case "(":
                                tokenList.append(("(", TokenType.OPEN_PAREN, LineNumber))
                                
                            case ")":
                                tokenList.append((")", TokenType.CLOSE_PAREN, LineNumber))

                            case "{":
                                tokenList.append(("{", TokenType.OPEN_BRACE, LineNumber))
                                
                            case "}":
                                tokenList.append(("}", TokenType.CLOSE_BRACE, LineNumber))
                                
                            case ";":
                                tokenList.append((";", TokenType.SEMICOLON, LineNumber))

                            case "~":
                                tokenList.append(("~", TokenType.TILDE, LineNumber))

                            case "-":
                                tokenList.append(("-", TokenType.HYPHEN, LineNumber))
                                
                            case "/":
                                tokenList.append(("/", TokenType.FORWARD_SLASH, LineNumber))
                            
                            case "*":
                                tokenList.append(("*", TokenType.ASTERISK, LineNumber))
                            
                            case "%":
                                tokenList.append(("%", TokenType.PERCENT, LineNumber))

                            case "+":
                                tokenList.append(("+", TokenType.PLUS, LineNumber))
                            
                            case "!":
                                tokenList.append(("!", TokenType.EXCLAMATION, LineNumber))

                            case ">":
                                tokenList.append((">", TokenType.GREATERT, LineNumber))
                            
                            case "<":
                                tokenList.append(("<", TokenType.LESST, LineNumber))

                            case "=":
                                tokenList.append(("=", TokenType.EQUAL, LineNumber))

                        #aqui tiene que ser keyword
                        buffer = char.string[char.span()[1]:]
                        #print(buffer)
                    else:
                        if buffer != '':
                            #raise Exception("Error invalid token: {0}".format(buffer))
                            print("Error invalid token: {0} at Line: {1}".format(buffer, LineNumber))
                            os.remove(iFile)
                            sys.exit(1)

    #aqui termina el while con la lista
    print(tokenList)

    return tokenList
