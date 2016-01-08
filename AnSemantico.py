#-*- coding: utf-8 -*-
# -------------------------------------------------------------------- 
#
#	FICHERO:	AnSemántico.py
#
#	Codigo de programa que realiza la parte Semántica para el compilador
#
# -------------------------------------------------------------------- 
from Error import Error


class Semantico:

	def __init__(self):
		self.log = Error()
		self.log.create_log()


	# declarada misma variable
	def redeclaracion (self,p,list):
		x = 0

		if not list.has_key(p[1]):

			if p[-1] == ',':

				while not p[x] == 'bool' and not p[x] == 'chars' and not p[x] == 'int':
					x = x - 1
				list[p[1]] = p[x]
			else:
				list[p[1]] = p[-1]

		else:
			self.log.message_debug("ANALIZADOR SEMÁNTICO")
			self.log.message_error("Redeclaracion " + " en línea " + str(p.lineno(1)))
	
	# declarada misma variable con previa asignacion
	def redeclaracion_assig(self,p,list):

		if not list.has_key(p[2]):
			list[p[2]] = p[1]
		else:
			self.log.message_debug("ANALIZADOR SEMÁNTICO")
			self.log.message_error("Redeclaracion " + " en línea " + str(p.lineno(1)))


	# Si no está declarada
	def existe(self,p,list):

		if not list.has_key(p[1]):
			self.log.message_debug("ANALIZADOR SEMÁNTICO")
			self.log.message_error("No está declarada la variable " + " en línea " + str(p.lineno(1)))


	def existe_prompt(self,p,list):

		if not list.has_key(p[3]):
			self.log.message_debug("ANALIZADOR SEMÁNTICO")
			self.log.message_error("No está declarada la variable " + " en línea " + str(p.lineno(1)))


	def existe_ologic(self,p,list):
		if not list.has_key(p[3]) or not list.has_key(p[1]):
			self.log.message_debug("ANALIZADOR SEMÁNTICO")
			self.log.message_error("No está declarada la variable " + " en línea " + str(p.lineno(1)))

