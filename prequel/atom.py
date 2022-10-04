class Atom(object):
    
    def __init__ (self, elt, id_):
        self.element = elt
        self.id = id_
        
    def __hash__(self):      return self.id
    def __eq__(self, other): return self.id == other.id