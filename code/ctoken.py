
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


class Token:
    data = ""
    tt = TokenType.NULL

    def __init__(self, string, type):
        self.data = string
        self.tt = type
