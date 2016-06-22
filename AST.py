import pydot

class Node:

    count = 0
    type = 'Node (unspecified)'
    shape = 'ellipse'
   
    def __init__(self,children=None):
        self.ID = str(Node.count)
        Node.count+=1

        if not children: 
            self.children = []
        elif hasattr(children,'__len__'):
            self.children = children
        else:
            self.children = [children]
        self.next = []


    def addNext(self,next):
        self.next.append(next)


    def nodeTree(self, prefix=''):
        result = "%s%s\n" % (prefix, repr(self))

        for c in self.children:
            if not isinstance(c,Node):
                result += "%s Error: Child of type %r: %r\n" % (prefix,type(c),c)
                continue
            result += c.nodeTree(prefix)
        return result
 

    def makegraphicaltree(self, dot=None, edgeLabels=True):
            if not dot: dot = pydot.Dot()

            dot.add_node(pydot.Node(self.ID,label=repr(self), shape=self.shape))
            label = edgeLabels and len(self.children)-1

            for i, c in enumerate(self.children):
                c.makegraphicaltree(dot, edgeLabels)
                edge = pydot.Edge(self.ID,c.ID)
                if label:
                    edge.set_label(str(i))
                dot.add_edge(edge)
            return dot
         

    def threadTree(self, graph, seen = None, col=0):
            colors = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')

            if not seen: seen = []

            if self in seen: return

            seen.append(self)
            new = not graph.get_node(self.ID)

            if new:
                graphnode = pydot.Node(self.ID,label=repr(self), shape=self.shape)
                graphnode.set_style('dotted')
                graph.add_node(graphnode)

            label = len(self.next)-1
            for i, c in enumerate(self.next):
                if not c: return
                col = (col + 1) % len(colors)
                color = colors[col]               
                c.threadTree(graph, seen, col)
                edge = pydot.Edge(self.ID,c.ID)
                edge.set_color(color)
                edge.set_arrowsize('.5')
                edge.set_constraint('false')
                if label:
                    edge.set_taillabel(str(i))
                    edge.set_labelfontcolor(color)
                graph.add_edge(edge)
            return graph   


    def __str__(self):
        return self.nodeTree()
   
   
    def __repr__(self):
        return self.type


class TokenNode(Node):
    type = 'token'

    def __init__(self, tok):
        Node.__init__(self)
        self.tok = tok
        
    def __repr__(self):
        return repr(self.tok)


class OpNode(Node):
    type = 'op'

    def __init__(self, op, children):
        Node.__init__(self,children)
        self.op = op
        try:
            self.nbargs = len(children)
        except AttributeError:
            self.nbargs = 1
         
    def __repr__(self):
        return "%s (%s)" % (self.op, self.nbargs)
   

class EntryNode(Node):
    type = 'ENTRY'

    def __init__(self):
        Node.__init__(self, None)


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


""" ARBOL AST: CLASES """

class Sentencias(Node):
    type = 'sentencia'

class Funcion(Node):
    type = 'function'
    
class FuncionNType(Node):
    type = 'funcion'

class Argumentos(Node):
    type = 'argv'

class Return(Node):
    type = 'return'

class VarNode(Node):
    type = 'var'

class WriteNode(Node):
    type = 'write'

class PromptNode(Node):
    type = 'prompt'

class IfNode(Node):
    type = 'if'

class ForNode(Node):
    type = 'for'

class AssignNode(Node):
    type = 'assign'

class CallFunNode(Node):
    type = 'callfun'
     
class IdNode(Node):
    type = 'ids'

class ExpresionesNode(Node):
    type = 'Expresiones'

class CondicionesNode(Node):
    type = 'Condiciones'

class LambdaNode(Node):
    type = 'lambda'
  