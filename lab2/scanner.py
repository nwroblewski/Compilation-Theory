import ply.lex as lex

literals = [ '+','-','*','/','(',')','=','[',']','>','<','{','}',':','\'',';',',']

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

tokens = ['DOTADD','DOTSUB',
        'DOTMUL','DOTDIV','ASSIGNADD','ASSIGNSUB',
        'ASSIGNMUL','ASSIGNDIV','LEQ','GEQ',
        'NEQ','EQ','ID',
        'INTNUM','FLOATNUM','STRING'] + list(reserved.values())

t_ignore = ' \t'


#explicitly defined tokens rules


t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\./'
t_ASSIGNADD = r'\+='
t_ASSIGNSUB = r'\-='
t_ASSIGNMUL = r'\*='
t_ASSIGNDIV = r'/='

t_LEQ = r'<='
t_GEQ = r'>='
t_NEQ = r'!='
t_EQ = r"=="

#reserved keywords rules

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_EYE(t):
    r'eye'
    return t

def t_ZEROS(t):
    r'zeros'
    return t

def t_ONES(t):
    r'ones'
    return t

def t_PRINT(t):
    r'print'
    return t

#id, string and number rules

def t_FLOATNUM(t):
    r'(([0-9]*)((\.[0-9]+) | (\.[0-9]+)[eE]?[-+][0-9]+))'
    t.value = float(t.value)
    return t

def t_ID(t):
    r"[a-zA-Z_]\w*"
    return t

def t_INTNUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t

def t_commentary(t):
    r'\#[^\n]*'

#newline rules, column number rules

def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    print("(%s): Illegal character '%s'" %(t.lineno,t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()