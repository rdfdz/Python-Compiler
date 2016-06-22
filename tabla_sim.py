from collections import defaultdict

class Val():

    S_TIPO_INT = "'int'"
    S_TIPO_CHARS = "'chars'"
    S_TIPO_BOOL = "'bool'"
    S_TIPO_FUNCION = 'funcion'
    S_TIPO_VAR = 'variable'


class TablaSim():

    def __init__(self):

        lista = lambda:defaultdict(lista)
        self.tabla = lista()
        self.declaraciones = {}
        self.ambito_actual = None
        self.nextId = 1
        self.desplazamiento = 0
        self.despfun = 0


    def declarar_variable(self, tipo, nombre):

        simbolo = Simbolo()
        simbolo.ambito = self.ambito_actual
        simbolo.nombre = nombre.replace("'","")
        simbolo.tipo = tipo
        simbolo.val = Val.S_TIPO_VAR
        simbolo.desp = self.desplazamiento
        simbolo.despfun = self.despfun

        if tipo == Val.S_TIPO_INT and simbolo.ambito == 'main':
            self.desplazamiento += 2
        elif simbolo.ambito == 'main':
            self.desplazamiento += 4
        elif tipo == Val.S_TIPO_INT:
            self.despfun -= 2
        else: 
            self.despfun -= 4

        if self.ambito_actual == 'main':
            if simbolo.nombre in self.tabla['main']:
                print ("Error: '%s' ya esta declarada" % simbolo.nombre)
            else:
                self.insertar_en_tabla(simbolo)
        else:
            if simbolo.nombre in self.declaraciones:
                print ("Error: '%s' ya esta declarada" % simbolo.nombre)
            else:
                self.declaraciones[simbolo.nombre] = simbolo
        return simbolo

 

    def declarar_funcion(self, nombre, tipo, listArgv):

        simbolo = Simbolo()
        simbolo.id = self.nextId
        simbolo.ambito = 'main' 
        simbolo.nombre = nombre
        simbolo.tipo = tipo
        simbolo.val = Val.S_TIPO_FUNCION
        simbolo.nArgv = len([x for x in listArgv if x == 'argv'])
        simbolo.listArgv = listArgv
        simbolo.varNone = self.declaraciones

        self.nextId += 1
        self.despfun = 0
        self.insertar_en_tabla(simbolo)

        for _, item in self.declaraciones.items():
            item.ambito = nombre
            self.insertar_en_tabla(item)
        self.declaraciones = {}        
        return simbolo


    def verificar_funcion(self, nombre):
        if not nombre in self.tabla['main']:
            print ("Error: '%s' No es una funcion valida." % nombre)


    def obtener_variable(self, nombre):
        if nombre in self.declaraciones:
            return self.declaraciones[nombre]
        if 'main' in self.tabla and nombre in self.tabla['main']:
            return self.tabla['main'][nombre]
        print ("Error: Variable '%s' no declarada en ambito actual." % nombre)


    def insertar_en_tabla(self, simbolo):
        self.tabla[simbolo.ambito][simbolo.nombre] = simbolo


    def verificar_llamada(self, nombre, list):
        fun = self.tabla['main'][nombre].nArgv
        tipos = self.tabla['main'][nombre].listArgv
        argvs = 0
        lista = []
        lista2 = []

        for x in tipos:
           if x == "'int'" or x == "'chars'" or x == "'bool'":
            lista.append(x)
            
        for x in list:
            if x != 'ids' and x != 'lambda':
                self.obtener_variable(x.replace("'",""))
                lista2.append(self.tabla['main'][x.replace("'","")].tipo)
                argvs += 1

        if lista != lista2:
            print ("Error: Argumentos con tipos incorrectos")

        if argvs != fun:
            print ("Error: Numero de parametros incorrecto")



    def __iter__(self):
        for _, simbolo in self.tabla.items():
            if isinstance(simbolo, Simbolo):
                yield simbolo
            else:
                for _, simbolo2 in simbolo.items():
                    yield simbolo2


    def __str__(self):
        string = "------------ TABLA GLOBAL ------------\n"
        for simbolo in self:
            string = string + repr(simbolo) + "\n"
        return string


class Simbolo():

    def __init__(self):

        self.id = None
        self.ambito = None
        self.nombre = None
        self.tipo = None
        self.val = None 
        self.desp = None 
        self.nArgv = None
        self.listArgv = None 
        self.varNone = None
        self.despfun = None
    

    def __repr__(self):

        stringtabs = "   + "
        tabs = "    "
        string = ""
        count = 1

        if self.ambito == 'main':

            string = "\n" + "* LEXEMA : " + "'" + str(self.nombre) + "'" + "\n"
            string = string + "  ATRIBUTOS:"+ "\n"
            string = string + stringtabs + "(esto es una " + str(self.val) + ") "

            if self.tipo != None :
                string = string + "tipo : " + str(self.tipo) +"\n"
            if self.desp != None :
                string = string + stringtabs +"desplazamiento : " + str(self.desp) + "\n"
            if self.nArgv != None :
                string = string + stringtabs +"numero de argumentos : " + str(self.nArgv) +"\n"
            if self.listArgv != None:
                for x in self.listArgv:
                    if x == "'int'" or x == "'chars'" or x == "'bool'":
                        string = string + tabs + stringtabs +"tipo parametro" + str(count) + ": " + str(x) +"\n"
                        count += 1
            if self.id != None:
                string = string + stringtabs +"id tabla : " + str(self.id) +"\n"

            if self.val == Val.S_TIPO_FUNCION:

                if self.listArgv != ['lambda'] or self.varNone != {}:
                    string = string + "\n\n" + tabs + "-------------------------------\n"
                    string = string + tabs + "TABLA DE LA FUNCION " + str(self.nombre) + " #" + str(self.id) + "\n" 

                    for _, item in self.varNone.items():
                            string = string + str(self.varNone[_])
                    string = string + tabs + "-------------------------------\n"

        return string
      
        
    def __str__(self):
        stringtabs = "   + "
        tabs = "    "
        string = tabs + "* LEXEMA : " + str(self.nombre) + "\n"
        string = string + tabs + stringtabs + "tipo : " + str(self.tipo) +"\n"
        string = string + tabs + stringtabs + "desplazamiento : " + str(self.despfun) +"\n"
        return string
        

