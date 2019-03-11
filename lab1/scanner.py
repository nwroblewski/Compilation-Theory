import ply.lex as lex

literals = [ '+','-','*','/','(',')' ]

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

tokens = ['ADD','SUB','MUL','DIV','DOTADD','DOTSUB',
        'DOTMUL','DOTDIV','ASSIGN','ASSIGNADD','ASSIGNSUB',
        'ASSIGNMUL','ASSIGNDIV','LT','GT','LEQ','GEQ',
        'NEQ','EQ','LPAR','RPAR','LSQBR','RSQBR','LCBRACE',
        'RCBRACE','RANGE','TRANSPOSE','COMMA','SEMIC','ID',
        'INTNUM','FLOATNUM','STRING'] + list(reserved.values())

t_ignore = ' \t'


#explicitly defined tokens regexes

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ASSIGN = r'='
t_ASSIGNADD = r'\+='
t_ASSIGNSUB = r'\-='
t_ASSIGNMUL = r'\*='
t_ASSIGNDIV = r'/='
t_LT = r'<'
t_GT = r'>'
t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='
t_EQ = r'=='
t_LPAR = r'\('
t_RPAR = r'\)'
t_LSQBR = r'\['
t_RSQBR = r'\]'
t_LCBRACE = r'\{'
t_RCBRACE = r'\}'
t_RANGE = r'\:'
t_TRANSPOSE = r'\''
t_COMMA = r'\,'
t_SEMIC = r'\;'

#reserved keywords regexes


def t_FLOATNUM(t):
    r'(([0-9]+)(\.[0-9]+))'
    t.value = float(t.value)
    return t

def t_ID(t):
    r"[a-zA-Z_]\w*"
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