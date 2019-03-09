import ply.lex as lex

literals = '+-*/=<>()[]{}:\',;'

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'for' : 'FOR',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'eye' : 'EYE',
    'zeros' : 'ZEROS',
    'ones' : 'ONES',
    'print' : 'PRINT'
}

tokens = ("DOTADD","DOTSUB","DOTMUL","DOTDIV","ADDEQ","SUBEQ","MULEQ","DIVEQ",
        "LEQ","GEQ","NEQ","EQ","ID","FLOATNUM","INTNUM","STRING") + list(reserved.values())


def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)