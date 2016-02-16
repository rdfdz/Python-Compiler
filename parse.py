from lexer import tokens
from AST import addToClass
import ply.yacc as yacc
import sys
import AST


precedence = (
    ('right','AOLOGIC'),
    ('left','OLOGIC'),
    ('left', 'YLOGIC'),
    ('left','ASSIGN','NOASSIG'),
    ('left','GREATERTHAN','LESSTHAN','LESS','GREATER'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MOD'),
    ('right', 'EXCLA'),
)

""" SENTENCIAS RECURSIVAS : FUNCIONES Y DECLARACIONES """

def p_sentencias(p):
    'S : sentencias'
    p[0] = p[1]
    parse.write("1 ")

def p_rec_sentencias(p):
    '''S : sentencias S
         | sentencias END_LINE S'''
    if len(p) == 3:
        p[0] = AST.Sentencias([p[1], p[2]])
        parse.write("2 ")
    else:
        p[0] = AST.Sentencias([p[1], p[3]])
        parse.write("3 ")

def p_funciones(p):
    'sentencias : funciones'
    p[0] = p[1]
    parse.write("4 ")

def p_declaraciones(p):
    'sentencias : declaraciones'
    p[0] = p[1]
    parse.write("5 ")



""" 1 : FUNCIONES """

def p_funcion_tipo(p):
    'funciones : FUNCTION tipos ID LPAREN argv RPAREN LBLOCK bloque_tipo RBLOCK'
    p[0] = AST.Funcion([p[2], AST.TokenNode(p[3]), p[5], p[8]])
    parse.write("6 ")

def p_funcion_sin_tipo(p):
    'funciones : FUNCTION ID LPAREN argv RPAREN LBLOCK bloque_sin_tipo RBLOCK'
    p[0] = AST.Funcion([AST.TokenNode(p[2]), p[4], p[7]])
    parse.write("7 ")

def p_argv(p):
    '''argv : argv_rec
            | '''
    if len(p) == 2: 
        p[0] = p[1]
        parse.write("8 ")
    else:
        p[0] = AST.Argumentos()
        parse.write("9 ")

def p_argv_rec(p):
    '''argv_rec : tipos ID
                | tipos ID COMA argv_rec'''
    if len(p) == 5:
        p[0] = AST.Argumentos([p[1], AST.TokenNode(p[2]), p[4]])
        parse.write("9 ")
    else:
        p[0] = AST.Argumentos([p[1], AST.TokenNode(p[2])])
        parse.write("10 ")

def p_bloque_sin_tipo(p):
    '''bloque_sin_tipo : declaraciones bloque_sin_tipo
                       | return_dec'''
    if len(p) == 3:
        p[0] = AST.Sentencias([p[1], p[2]])
        parse.write("11 ")
    else:
        p[0] = p[1]
        parse.write("12 ")

def p_bloque_tipo(p):
    '''bloque_tipo : declaraciones bloque_tipo
                   | RETURN expresiones_mul'''
    if not p[1] == 'return':
        p[0] = AST.Sentencias([p[1], p[2]])
        parse.write("13 ")
    else:
        p[0] = AST.Return(p[2])
        parse.write("14 ")



""" 2 : DECLARACIONES """

def p_variables(p):
    'declaraciones : VAR tipos ids'
    p[0] = AST.VarNode([p[2], p[3]])
    parse.write("15 ")

def p_write(p):
    'declaraciones : WRITE LPAREN expresiones RPAREN'
    p[0] = AST.WriteNode(p[3])
    parse.write("16 ")

def p_prompt(p):
    'declaraciones : PROMPT LPAREN ID RPAREN'
    p[0] = AST.PromptNode(AST.TokenNode(p[3]))
    parse.write("17 ")

def p_if(p):
    'declaraciones : IF LPAREN condiciones RPAREN return_dec'
    p[0] = AST.IfNode([p[3], p[5]])
    parse.write("18 ")

def p_for(p):
    'declaraciones : FOR LPAREN ID ASSIGN comun END_LINE condiciones END_LINE ID ASSIGN expresiones RPAREN LBLOCK bloque_sin_tipo RBLOCK'
    p[0] = AST.ForNode([AST.OpNode(p[4],[AST.TokenNode(p[3]),p[5]]),p[7],AST.OpNode(p[10],[AST.TokenNode(p[9]),p[11]]),p[14]])
    parse.write("19 ")

def p_asignacion(p):
    'declaraciones : ID ASSIGN expresiones_mul'
    p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])
    parse.write("20 ")

def p_ologico(p):
    'declaraciones : ID AOLOGIC ID'
    p[0] = AST.OpNode(p[2], [AST.TokenNode(p[1]), AST.TokenNode(p[3])])
    parse.write("21 ")

def p_llamada_funcion(p):
    'declaraciones : ID LPAREN idsfun RPAREN'
    p[0] = AST.CallFunNode([AST.TokenNode(p[1]), p[3]])
    parse.write("22 ")



""" EXPRESIONES """

def p_if_declaraciones(p):
    '''return_dec : declaraciones
                  | RETURN'''
    if not p[1] == 'return':
        p[0] = AST.Sentencias(p[1])
        parse.write("23 ")
    else:
        p[0] = AST.TokenNode(p[1])
        parse.write("24 ")

def p_mul_id(p):
    '''ids : ID COMA ids 
           | ID'''
    if len(p) == 4:
        p[0] = AST.IdNode([AST.TokenNode(p[1]),p[3]])
        parse.write("25 ")
    else:
        p[0] = AST.TokenNode(p[1])
        parse.write("26 ")
         
def p_idsFuncionVacio(p):
    '''idsfun : ids
              | '''
    if len(p) == 2: 
        p[0] = p[1]
        parse.write("27 ")
    else:
        p[0] = AST.IdNode()
        parse.write("28 ")

def p_tipos(p):
    '''tipos : INT
             | CHARS
             | BOOL'''
    if p[1] == 'int':
        parse.write("29 ")
    elif p[1] == 'chars':
        parse.write("30 ")
    elif p[1] == 'bool':
        parse.write("31 ")
    p[0] = AST.TokenNode(p[1])

def p_expresiones(p):
    '''expresiones : comun
                   | comun exp2'''
    if len(p) == 2:
        p[0] = p[1]
        parse.write("32 ")
    else:
        p[0] = AST.ExpresionesNode([p[1],p[2]])
        parse.write("33 ")

def p_expresiones_string(p):
    'expresiones : STRINGS'
    p[0] = AST.TokenNode(p[1])
    parse.write("34 ")
   
def p_expresiones2(p):
    '''exp2 : PLUS expresiones
            | MINUS expresiones
            | TIMES expresiones
            | DIVIDE expresiones
            | MOD expresiones'''
    if p[1] == '+':
        parse.write("35 ")
    elif p[1] =='-':
        parse.write("36 ")
    elif p[1] == '*':
        parse.write("37 ")
    elif p[1] == '/':
        parse.write("38 ")
    elif p[1] == '%':
        parse.write("39 ")
    p[0] = AST.OpNode(p[1],p[2])

def p_condiciones(p): 
    '''condiciones : comun 
                   | comun cond2'''
    if len(p) == 2:
        p[0] = p[1]
        parse.write("40 ")
    else:
        p[0] = AST.CondicionesNode([p[1],p[2]])
        parse.write("41 ")

def p_exclamacion(p):
    'condiciones : EXCLA comun'
    p[0] = AST.OpNode(p[1],p[2])
    parse.write("42 ")
   
def p_condiciones2(p):
    '''cond2 : GREATERTHAN condiciones
             | LESSTHAN condiciones
             | EQUALS condiciones
             | NOASSIG condiciones
             | LESS condiciones
             | GREATER condiciones
             | OLOGIC condiciones
             | YLOGIC condiciones'''
    if p[1] == '>=':
        parse.write("43 ")
    elif p[1] =='<=':
        parse.write("44 ")
    elif p[1] == '==':
        parse.write("45 ")
    elif p[1] == '!=':
        parse.write("46 ")
    elif p[1] == '<':
        parse.write("47 ")  
    elif p[1] == '>':
        parse.write("48 ")  
    elif p[1] == '||':
        parse.write("49 ") 
    elif p[1] == '&&':
        parse.write("50 ") 
    p[0] = AST.OpNode(p[1],p[2]) 


def p_expresiones_mul_exp(p):
    '''expresiones_mul : EXCLA comun
                       | comun expMul2 '''
    if p[1] =='!':
        p[0] = AST.OpNode(p[1],p[2])
        parse.write("51 ")
    else:
        p[0] = AST.ExpresionesNode([p[1],p[2]])
        parse.write("52 ")

def p_expresiones_mul_con_1(p):
    'expMul2 : cond2 '
    p[0] = p[1]
    parse.write("53 ")
    
def p_expresiones_mul_con_2(p):
    'expMul2 : exp2 '
    p[0] = p[1]
    parse.write("54 ")
    
def p_expresiones_mul_con_3(p):
    'expMul2 : '
    p[0] = AST.ExpresionesNode()
    parse.write("55 ")

def p_condiciones3(p):
    'expresiones_mul : STRINGS'
    p[0] = AST.TokenNode(p[1])
    parse.write("56 ")

def p_comun(p):
    'comun : NUMBER'
    p[0] = AST.TokenNode(p[1])
    parse.write("57 ")

def p_comun_dos(p):
    'comun : ID'
    p[0] = AST.TokenNode(p[1])
    parse.write("58 ")

def p_error(p):
    print("Sintantic: syntax error '%s' in line %d" % (p.value, p.lineno))
    sys.exit()
 
def file_parse():
    parse = open("parse.txt","w")
    parse.write("A ")
    return parse

@addToClass(AST.Node)
def thread(self, lastNode):
    for c in self.children:
        lastNode = c.thread(lastNode)
    lastNode.addNext(self)
    return self

def thread(tree):
    entry=AST.EntryNode()
    tree.thread(entry)
    return entry


yacc.yacc()
 
if __name__ == "__main__":
    parse = file_parse()
    f = open(sys.argv[1], 'r')
    data = f.read()
    f.close()
    
    result = yacc.parse(data)
    entry = thread(result)
    #print(result)
    
    graph = result.makegraphicaltree()
    entry.threadTree(graph) 
    graph.write_pdf('grafo.pdf')
    result.imprimir_symTable()
    parse.close()