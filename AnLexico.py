#-*- coding: utf-8 -*-
# -------------------------------------------------------------------- 
#
#	FICHERO:	AnLexico.py
#
#	Código de programa que realiza la parte Léxica para el compilador
#	
# -------------------------------------------------------------------- 


from Error import Error
import sys


# Palabras Reservadas de JavaScript
reserved = {
	'var': 'VAR_PALRES',
	'prompt':'PROMPT_PALRES',
	'function':'FUNCTION_PALRES',
	'write':'WRITE_PALRES',
	'if':'IF_PALRES',
	'return':'RETURN_PALRES',
	'int':'INT_PALRES',
	'chars':'CHARS_PALRES',
	'bool':'BOOL_PALRES',
	'for':'FOR_PALRES'
}

# Lista de tokens
tokens = [
	'ID',
	'NUMBER',
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'MOD',
	'EQUALS',
	'LESS',
	'GREATER',
	'LESSTHAN',
	'GREATERTHAN',
	'ASSIGNATION',
	'NOASSIG',
	'COMA',
	'SEMICOLON',
	'PARL',
	'PARR',
	'YLOGIC',
	'OLOGIC',
	'STRINGS',
	'BLOCKL',
	'BLOCKR',
	'AOLOGIC'
] + list(reserved.values())


"""Expresiones Regulares"""

# Operadores Aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'\%'

#Operadores Relacionales
t_GREATERTHAN = r'>='
t_LESSTHAN = r'<='
t_EQUALS = r'=='
t_NOASSIG = r'!='
t_LESS = r'<'
t_GREATER = r'>'

#Operadores Lógicos
t_YLOGIC = r'&&'
t_OLOGIC = r'\|\|'

# Implementaciones Obligatorias
t_COMA = r','
t_SEMICOLON = r';'
t_BLOCKR = r'}'
t_BLOCKL = r'{'
t_PARL = r'\('
t_PARR = r'\)'
t_ASSIGNATION = r'='

# Asignación con o lógico (Grupo 51)
t_AOLOGIC = r'\|='

# Cadena de Caractéres
t_STRINGS = r'\"([^\\\n]|(\\(.|\n)))*?\"'

# String que ignora espacios y tabuladores
t_ignore = ' \t\v'

# Ignora comentarios de tipo /* */
t_ignore_COMMENT = r'/\*(.|\n)*?\*/'
	

"""Funciones Regulares"""

# Funcion de caracteres. Compara con Palabras Reservadas
def t_ID (t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID') 
	return t

# Funcion para Numeros
def t_NUMBER (t):
	r'\d+'			
	t.value = eval(t.value)
	return t

# Salto de Lineas
def t_newline (t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Ignora comentarios de tipo //
def t_COMMENT(t):
	r'\//.*'
	pass


# Codigo de error
def t_error(t):
	log = Error()
	log.create_log()
	log.message_debug("ANALIZADOR LÉXICO")
	log.message_error("Carácter inesperado " + str(t.value[0])+ " en línea " + str(t.lineno) +", posición "+str(t.lexpos))
	log.message_warning("Pueden existir más errores léxicos, corrige primero este error: " + str(t.value[0]))
	sys.exit()


