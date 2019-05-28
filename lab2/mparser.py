import sys
import scanner
import ply.yacc as yacc

tokens = scanner.tokens

# przypisania += itd 
# plus relacyjne


precedence = (
    ("right", '=', 'ASSIGNADD', 'ASSIGNSUB', 'ASSIGNMUL', 'ASSIGNDIV'),
    ("left", '<' , '>', 'EQ', 'NEQ', 'LEQ', 'GEQ'),
    ("left", '+', '-'),
    ("left", 'DOTADD', 'DOTSUB'),
    ("left", '*', '/'),
    ("left", 'DOTMUL', 'DOTDIV'),
    ("right", '\'')
)

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, scanner.find_column("", p), p.type, p.value))
    else:
        print("Unexpected end of input")


def p_m_expr(_p):
    """m_expr : expression
              | expression m_expr"""

def p_expression(_p):
    """expression : c_block
                  | base_expr
                  | base_expr ';'
                  | if_st
                  | loop_st"""

def p_base_expr(_p):
    """ base_expr : assignment
              | return
              | print"""

def p_operation(_p):
    """ operation : number
                 | unary_operation
                 | function"""
                 
def p_c_block(_p):
    """c_block : '{' m_expr '}'"""

def p_PRINT(_p):
    """print : PRINT print_b """

def p_print_b(_p):
    """print_b : STRING
               | operation
               | print_b ',' operation"""

def p_RETURN(_p):
    """return : RETURN condition
              | RETURN operation
              | RETURN"""

def p_array(_p):
    """array : '[' array_b ']'"""

def p_array_b(_p):
    """array_b : number
               | array_b ',' number
               | eps"""
def p_matrix(_p):
    """matrix : '[' matrix_b ']'"""

def p_matrix_b(_p):
    """matrix_b : array
                | matrix_b ',' array
                | eps"""

def p_number(_p):
    """number : INTNUM
              | FLOATNUM
              | ID"""

def p_range(_p):
    """range : ID '[' int_variable ',' int_variable ']'"""

def p_int_variable(_p):
    """int_variable : INTNUM
                    | ID"""

def p_function(_p):
    """function : function_n '(' number ')'"""

def p_function_n(_p):
    """function_n : ONES
                | EYE
                | ZEROS"""

def p_condition(_p):
    """condition : compare"""

def p_loop_st(_p):
    """loop_st : while
              | for"""

def p_while(_p):
    """while : WHILE '(' condition ')' loop_b"""

def p_for(_p):
    """for : FOR ID '=' int_variable ':' int_variable loop_b"""

def p_loop_b(_p):
    """loop_b : loop_expr
              | loop_expr ';'
              | '{' m_loop_expr '}'"""

def p_loop_expr(_p):
    """loop_expr : base_expr
                 | loop_st
                 | if_loop_st
                 | BREAK
                 | CONTINUE"""

def p_m_loop_expr(_p):
    """m_loop_expr : m_loop_expr loop_b
                   | loop_b"""

def p_if_st(_p):
    """if_st : IF '(' condition ')' expression else_st"""

def p_else_st(_p):
    """else_st : ELSE expression
               | eps"""

def p_if_loop_st(_p):
    """if_loop_st : IF '(' condition ')' loop_b else_loop_st"""

def p_else_loop_st(_p):
    """else_loop_st : ELSE loop_b
                    | eps"""

def p_eps(_p):
    """eps : """

def p_assign_expr(_p):
    """assign_expr : ID
                   | range"""

def p_assignment(_p):
    """assignment : assign_expr '=' matrix
                  | assign_expr '=' STRING
                  | assign_expr '=' operation
                  | assign_expr ASSIGNADD operation
                  | assign_expr ASSIGNSUB operation
                  | assign_expr ASSIGNMUL operation
                  | assign_expr ASSIGNDIV operation"""

def p_unary_operation(_p):
    """unary_operation : negation
                      | transpose"""

def p_negation(_p):
    """negation : '-' number"""

def p_transpose(_p):
    """transpose : ID '\\'' """

def p_operation_binary(_p):
    """operation : operation '+' operation
                 | operation '-' operation
                 | operation DOTADD operation
                 | operation DOTSUB operation
                 | operation '*' operation
                 | operation '/' operation
                 | operation DOTMUL operation
                 | operation DOTDIV operation
                 | '(' operation ')'"""

def p_compare(_p):
    """compare : operation '<' operation
               | operation '>' operation
               | operation EQ operation
               | operation NEQ operation
               | operation GEQ operation
               | operation LEQ operation"""

parser = yacc.yacc()
