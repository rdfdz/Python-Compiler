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
from AnSemantico import Semantico

# Precedencia de Operadores
precedence = (
	('right','AOLOGIC'),
	('left','OLOGIC'),
	('left', 'YLOGIC'),
	('left','ASSIGNATION','NOASSIG'),
	('left','GREATERTHAN','LESSTHAN','LESS','GREATER'),
	('left','PLUS','MINUS'),
	('left','TIMES','DIVIDE','MOD'),
)

# Analizador Semántico
semantic = Semantico()

# Biblioteca de variables
__var_names = {}

# Fichero con el parse Ascendente
parse = open("parse.txt","w+")
parse.write("A ")



""" SENTENCIAS Y RECURSIVIDAD """

def p_sentencias(p):
	'sentencias : sentencias declaraciones'
	p[0] = p[1]
	parse.write("1 ")

def p_rec_sentencias_pc(p):
	'sentencias : sentencias SEMICOLON declaraciones'
	parse.write("2 ")

def p_declaraciones(p):
	'sentencias : declaraciones'
	p[0] = p[1]
	parse.write("3 ")



""" DECLARACIONES """

def p_variables(p):
	'declaraciones : VAR_PALRES constantes'
	p[0] = p[1]
	parse.write("4 ")

def p_write(p):
	'declaraciones : WRITE_PALRES PARL expresiones PARR'
	parse.write("5 ")

def p_prompt(p):
	'declaraciones : PROMPT_PALRES PARL ID PARR'
	semantic.existe_prompt(p,__var_names)
	parse.write("6 ")
	
# # ? condicion
# def p_if(p):
# 	'declaraciones : IF_PALRES PARL condicion PARR declaraciones'
# 	parse.write("7 ")

# # ? init condicion actualizacion
# def p_for(p):
# 	'declaraciones : FOR_PALRES PARL init SEMICOLON condicion SEMICOLON actualizacion PARR BLOCKL declaraciones BLOCKR'
# 	parse.write("8 ")

def p_asignacion(p):
	'declaraciones : ID ASSIGNATION expresiones'
	semantic.existe(p,__var_names)
	parse.write("9 ")

def p_ologico(p):
	'declaraciones : ID AOLOGIC ID'
	semantic.existe_ologic(p,__var_names)
	parse.write("10 ")

# def p_llamada_funcion(p):
# 	'declaraciones : ID PARL argumento PARR'
# 	parse.write("11 ")

# # Recursivo impl
# def p_funcion(p):
# 	'declaraciones : FUNCTION_PALRES id_fun PARL argv PARR BLOCKL declaraciones BLOCKR'
# 	parse.write("12 ")

# def p_freturn(p):
# 	'declaraciones : RETURN_PALRES exp'
# 	parse.write("13 ")



""" EXPRESIONES """

def p_constante_chars(p):
	'''constantes : CHARS_PALRES ids
				  | CHARS_PALRES ID ASSIGNATION STRINGS'''
	if (len(p) == 3):
		parse.write("14 ")
	else:
		parse.write("15 ")
		semantic.redeclaracion_assig(p,__var_names)

def p_constante_int(p):
	'''constantes : INT_PALRES ids
				  | INT_PALRES ID ASSIGNATION NUMBER'''
	if (len(p) == 3):
		parse.write("16 ")
	else:
		parse.write("17 ")
		semantic.redeclaracion_assig(p,__var_names)

def p_constante_bool(p):
	'constantes : BOOL_PALRES ids'
	parse.write("17 ")
	
def p_multiples_id(p):
	'''ids : ID COMA ids 
		   | ID'''
	semantic.redeclaracion(p,__var_names)
	parse.write("18 ") if (len(p) == 5) else parse.write("19 ")


def p_expresiones(p):
   	'''expresiones : expresiones PLUS expresiones
    	           | expresiones MINUS expresiones
              	   | expresiones TIMES expresiones
            	   | expresiones DIVIDE expresiones
             	   | expresiones MOD expresiones'''
	if p[2] == '+':
		parse.write("19 ")
	elif p[2] =='-':
		parse.write("20 ")
	elif p[2] == '*':
		parse.write("21 ")
	elif p[2] == '/':
		p[0] = p[1] / p[3]
	elif p[2] == '%':
		p[0] = p[1] % p[3]

def p_expresiones_string(p):
	'expresiones : STRINGS'

# falta errores semanticos y error declaracion solo con id
def p_opciones_exp(p):
	'''expresiones : NUMBER
                   | ID'''


	# print __var_names.get(p[1])
	# print p[1]
	# print __var_names
	# print "---------------"

def p_error(p):
	log = Error()
	log.create_log()
	log.message_debug("ANALIZADOR SINTÁCTICO")
	log.message_error("Error Sintáctico" + " en línea " + str(p.lineno))
	

