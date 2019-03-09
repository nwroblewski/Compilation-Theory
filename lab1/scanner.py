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
        "LEQ","GEQ","NEQ","EQ","ID","FLOATNUM","INTNUM","STRING","MATRIX") + list(reserved.values())




def t_FLOATNUM(t):
     r'(([0-9]+)(\.[0-9]+))'
    t.value = float(t.value)
    return t


def t_INTNUM(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)


def p_error(p):
    print("parsing error\n")
