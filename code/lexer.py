import sys
import os
import re
from enum import Enum
#from cd import printDebugInfo

class TokenType(Enum):
    NULL = 1
    IDENTIFIER = 2
    INT_CONSTANT = 3
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
    QUESTION_MARK = 29
    COLON = 30
    IF_KW = 31
    ELSE_KW = 32
    DO_KW = 33
    WHILE_KW = 34
    FOR_KW = 35
    BREAK_KW = 36
    CONTINUE_KW = 37
    COMMA = 38
    STATIC_KW = 39
    EXTERN_KW = 40
    LONG_KW = 41
    LONG_CONSTANT = 42
    SIGNED_KW = 43
    UNSIGNED_KW = 44
    UINT_CONSTANT = 45
    ULONG_CONSTANT = 46
    DOUBLE_CONSTANT = 47
    DOUBLE_KW = 48
    AMPERSAND = 49
    OPEN_BRACKET = 50
    CLOSE_BRACKET = 51
    CHAR_KW = 52
    CHAR_CONST = 53
    STRING_LITERAL = 54

def Lex(buffer, iFile):
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
        
        is_floatingPoint = r"(([0-9]*\.[0-9]+|[0-9]+\.?)[Ee][+-]?[0-9]+|[0-9]*\.[0-9]+|[0-9]+\.)[^\w.]"
        floatingPoint = re.match(is_floatingPoint, buffer)
        if floatingPoint:
            is_floatingPoint = r"(([0-9]*\.[0-9]+|[0-9]+\.?)[Ee][+-]?[0-9]+|[0-9]*\.[0-9]+|[0-9]+\.)"
            floatingPoint = re.match(is_floatingPoint, buffer)
            if floatingPoint:
                #print(floatingPoint.group())
                tokenList.append((floatingPoint.group(), TokenType.DOUBLE_CONSTANT, LineNumber))
                buffer = floatingPoint.string[floatingPoint.span()[1]:]
                continue
        
        is_unsignedLong = r"([0-9]+([uU][lL]|[lL][uU]))[^\w.]"
        unsignedLong = re.match(is_unsignedLong, buffer)
        if unsignedLong:

            is_unsignedLong = r"([0-9]+([uU][lL]|[lL][uU]))"
            unsignedLong = re.match(is_unsignedLong, buffer)
            if unsignedLong:
                tokenList.append((unsignedLong.group(), TokenType.ULONG_CONSTANT, LineNumber))

                buffer = unsignedLong.string[unsignedLong.span()[1]:]
                continue
        
        is_unsigned = r"([0-9]+[uU])[^\w.]"
        unsigned = re.match(is_unsigned, buffer)
        if unsigned:
            is_unsigned = r"([0-9]+[uU])"
            unsigned = re.match(is_unsigned, buffer)
            if unsigned:
                tokenList.append((unsigned.group(), TokenType.UINT_CONSTANT, LineNumber))

                buffer = unsigned.string[unsigned.span()[1]:]
                continue
        

        is_long = r"([0-9]+[lL])[^\w.]"
        long = re.match(is_long, buffer)
        if long:
            is_long = r"([0-9]+[lL])"
            long = re.match(is_long, buffer)
            if long:
                tokenList.append((long.group(), TokenType.LONG_CONSTANT, LineNumber))
                buffer = long.string[long.span()[1]:]
                continue

        is_int = r"([0-9]+)[^\w.]"
        int = re.match(is_int, buffer)
        if int:
            is_int = r"([0-9]+)"
            int = re.match(is_int, buffer)
            if int:
                tokenList.append((int.group(), TokenType.INT_CONSTANT, LineNumber))

                buffer = int.string[int.span()[1]:]
                continue
        

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
                    
        if dd:
            continue

        isStringLiteral = r"\"([^\"\\\n]|\\[\'\"\\\?abfnrtv])*\""
        sl = re.match(isStringLiteral, buffer)
        if sl:
            """
            """
            sliced = sl.group()[1:len(sl.group())-1]
            lSliced = list(sliced)
            
            unScapedL = []
            print(lSliced)

            while lSliced != []:
                value = None
                char = lSliced.pop(0)
                match char:
                    case '\\':
                        char = lSliced.pop(0) 
                        match char:
                            case '\'':
                                value = '\''
                            case '\"':
                                value = '\"'
                            case '?':
                                value = '?'
                            case '\\':
                                value = '\\'
                            case 'a':
                                value = '\a'
                            case 'b':
                                value = '\b'
                            case 'f':
                                value = '\f'
                            case 'n':
                                value = '\n'
                            case 'r':
                                value = '\r'
                            case 't':
                                value = '\t'
                            case 'v':
                                value = '\v' 
                    case _:
                        value = char
                
                unScapedL.append(value)
            
            print(unScapedL)

            a = "".join(unScapedL)
            print(a)
            tokenList.append((a, TokenType.STRING_LITERAL, LineNumber))
            buffer = sl.string[sl.span()[1]:]
            continue

        isCharacterConstant = r"\'([^\'\\\n]|\\[\'\"\?\\abfnrtv])\'"
        cc = re.match(isCharacterConstant, buffer)
        if cc:
            sliced = cc.group()[1:len(cc.group())-1]
            #print(sliced)
            asciiValue = None
            #ale = "Ale\n"
            #print(ale)
            match sliced[0]:
                case '\\':
                    match sliced[1]:
                        case '\'':
                            asciiValue = ord('\'')
                        case '\"':
                            asciiValue = ord('\"')
                        case '?':
                            asciiValue = ord('?')
                        case '\\':
                            asciiValue = ord('\\')
                        case 'a':
                            asciiValue = ord('\a')
                        case 'b':
                            asciiValue = ord('\b')
                        case 'f':
                            asciiValue = ord('\f')
                        case 'n':
                            asciiValue = ord('\n')
                        case 'r':
                            asciiValue = ord('\r')
                        case 't':
                            asciiValue = ord('\t')
                        case 'v':
                            asciiValue = ord('\v')

                case _:
                    asciiValue = ord(sliced[0])

            if asciiValue == None:
                print("Error invalid token: {0} at Line: {1}".format(buffer, LineNumber))
                os.remove(iFile)
                sys.exit(1)

            tokenList.append((asciiValue, TokenType.INT_CONSTANT, LineNumber))
            buffer = cc.string[cc.span()[1]:]
            continue



        is_alphanumeric = r"[a-zA-Z_]\w*\b"
        alphanumeric = re.match(is_alphanumeric, buffer)
        if alphanumeric:
            
            match alphanumeric.group():
                
                case "char":
                    tokenList.append(("char", TokenType.CHAR_KW, LineNumber))

                case "double":
                    tokenList.append(("double", TokenType.DOUBLE_KW, LineNumber))

                case "unsigned":
                    tokenList.append(("unsigned", TokenType.UNSIGNED_KW, LineNumber))

                case "signed":
                    tokenList.append(("signed", TokenType.SIGNED_KW, LineNumber))

                case "long":
                    tokenList.append(("long", TokenType.LONG_KW, LineNumber))

                case "extern":
                    tokenList.append(("extern", TokenType.EXTERN_KW, LineNumber))

                case "static":
                    tokenList.append(("static", TokenType.STATIC_KW, LineNumber))

                case "if":
                    tokenList.append(("if", TokenType.IF_KW, LineNumber))

                case "else":
                    tokenList.append(("else", TokenType.ELSE_KW, LineNumber))

                case "do":
                    tokenList.append(("do", TokenType.DO_KW, LineNumber))

                case "while":
                    tokenList.append(("while", TokenType.WHILE_KW, LineNumber))

                case "for":
                    tokenList.append(("for", TokenType.FOR_KW, LineNumber))

                case "break":
                    tokenList.append(("break", TokenType.BREAK_KW, LineNumber))

                case "continue":
                    tokenList.append(("continue", TokenType.CONTINUE_KW, LineNumber))

                case "int":
                    tokenList.append(("int", TokenType.INT_KW, LineNumber))
                    
                case "void":
                    tokenList.append(("void", TokenType.VOID_KW, LineNumber))
                    
                case "return":
                    tokenList.append(("return", TokenType.RETURN_KW, LineNumber))
                
                
                case _:
                    tokenList.append((alphanumeric.group(), TokenType.IDENTIFIER, LineNumber))

            buffer = alphanumeric.string[alphanumeric.span()[1]:]
            continue
            #print(buffer)
        
        is_char = r"[\[\]&,?:=><!%/*+(){};~-]"
        char = re.match(is_char, buffer)
        if char:
            #print(char)
            match char.group():
                
                case "[":
                    tokenList.append(("[", TokenType.OPEN_BRACKET, LineNumber))

                case "]":
                    tokenList.append(("]", TokenType.CLOSE_BRACKET, LineNumber))

                case "&":
                    tokenList.append(("&", TokenType.AMPERSAND, LineNumber))

                case ",":
                    tokenList.append((",", TokenType.COMMA, LineNumber))
                case "?":
                    tokenList.append(("?", TokenType.QUESTION_MARK, LineNumber))
                case ":":
                    tokenList.append((":", TokenType.COLON, LineNumber))
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
            continue
            #print(buffer)
        
        if buffer != '':
            #raise Exception("Error invalid token: {0}".format(buffer))
            print("Error invalid token: {0} at Line: {1}".format(buffer, LineNumber))
            os.remove(iFile)
            sys.exit(1)

    #aqui termina el while con la lista
    #if printDebugInfo: 
    #    print(tokenList)

    return tokenList
