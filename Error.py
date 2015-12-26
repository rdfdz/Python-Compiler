#-*- coding: utf-8 -*-
# -------------------------------------------------------------------- 
#
#	FICHERO:	Error.py
#
#	Control de errores del Compilador. Por shell y log
#
# -------------------------------------------------------------------- 

import os, platform, logging
import coloredlogs


class Error():

	def create_log(self): 
		
		if platform.platform().startswith('Windows'):
	 		fichero_log = os.path.join(os.getenv('HOMEDRIVE'), os.getenv("HOMEPATH"),'error.log')
		else:
	 		fichero_log = os.path.join('error.log')
	 	
		logging.basicConfig(
	 		level = logging.DEBUG,
	 		format = '%(asctime)s : %(levelname)s : %(message)s',
	 		filename = fichero_log,
	 		filemode = 'a+',)

		coloredlogs.install(level='debug')

	def message_debug(self,message):
		return logging.debug(message) 

	def message_error(self,message):
		return logging.error(message)

	def message_warning(self,message):
		return logging.warning(message)

	