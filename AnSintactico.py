#-*- coding: utf-8 -*-
# -------------------------------------------------------------------- 
#
#	FICHERO:	AnSintácico.py
#
#	Codigo de programa que realiza la parte Sintáctica para el compilador
#
# -------------------------------------------------------------------- 

from Error import Error
from AnLexico import tokens


# Precedencia de Operadores
precedence = (
	('right','AOLOGIC'),
	('left','OLOGIC'),
	('left', 'YLOGIC'),
	('left','ASSIGNATION','NOASSIG'),
	('left','GREATERTHAN','LESSTHAN','LESS','GREATER'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MOD'),
    ('right','EXCLA'),
)

def p_sentencias(p):
	'S : sentencias'
	p[0] = p[1]

def p_rec_sentencias(p):
	'sentencias : sentencias declaraciones'

def p_declaraciones(p):
	'sentencias : declaraciones'
	p[0] = p[1]

def p_write(p):
	'declaraciones : WRITE_PALRES PARL expresiones PARR'

def p_prompt(p):
	'declaraciones : PROMPT_PALRES PARL ID PARR'

def p_variables(p):
	'declaraciones : VAR_PALRES constantes'
	p[0] = p[1]

def p_expresiones(p):
	'''expresiones : STRINGS
				   | options'''
	p[0] = p[1]

def p_options(p):
    '''options : options PLUS options
    		   | options MINUS options
    		   | options TIMES options
    		   | options DIVIDE options
    	       | options MOD options'''
    if p[2] == '+':
    	p[0] = p[1] + p[3]
    elif p[2] =='-':
    	p[0] = p[1] - p[3]
    elif p[2] == '*':
    	p[0] = p[1] * p[3]
    elif p[2] == '/':
    	p[0] = p[1] / p[3]
    elif p[2] == '%':
    	p[0] = p[1] % p[3]

def p_identificadores(p):
    '''options : NUMBER
    		   | ID'''
    p[0] = p[1]

def p_constante_chars(p):
	'''constantes : CHARS_PALRES constantes
				  | CHARS_PALRES ID EQUALS STRINGS constantes'''

def p_constante_int(p):
	'''constantes : INT_PALRES constantes
				  | INT_PALRES ID EQUALS NUMBER constantes'''

def p_constante_bool(p):
	'constantes : BOOL_PALRES constantes'
	
def p_constante_global(p):
	'''constantes : COMA constantes
				  | ID constantes
				  | '''

def p_error(p):
    print("Syntax error in input!")
