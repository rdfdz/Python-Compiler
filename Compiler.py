#-*- coding: utf-8 -*-
# -------------------------------------------------------------------- 
#
#	FICHERO:	Compiler.py
#
#	Main del compilador
#
# -------------------------------------------------------------------- 

import AnLexico
import ply.lex as lex
import ply.yacc as yacc
import sys
from AnSintactico import *
from Error import Error


# Construir el analizador lexico
lex.lex(AnLexico) 

# Creamos el fichero de tokens
ftok = open("tokens.txt","w+")


# Abrimos el .js, leemos y analizamos
fich = open(sys.argv[1],"r")
datos = fich.read()
lex.input(datos)


# Obtener los tokens.
while 1 :
    token = lex.token()
    if not token:
        break
    ftok.write(" < " + token.type +" , " + str(token.value) + " > \n")


parser = yacc.yacc()
parser.parse(datos)
# while 1:
# 	try:
# 		s = raw_input('enter > ')
# 	except EOFError:
# 		break
# 	if not s: continue
#    	yacc.parse(s)

# Cerramos el fichero tokens.txt
ftok.close()
# Cerramos el archivo .js
fich.close()

