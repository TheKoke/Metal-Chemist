from atom import Atom

class Atom(object):
    elements = {
        'H': (1, 1.0), 
        'B': (3, 10.8),
        'C': (4, 12.0),
        'N': (3, 14.0),
        'O': (2, 16.0),
        'F': (1, 19.0),
        'Mg': (2, 24.3),
        'P': (3, 31.0),
        'S': (2, 32.1),
        'Cl': (1, 35.5),
        'Br': (1, 80.0)
    }    
    
    def __init__ (self, elt: str, id_: int):
        self.element = elt
        self.id = id_
        self.neighrs = []
        
    def get_weight(self) -> float:
        return Atom.elements[self.element][1]

    def get_valence(self) -> int:
        return Atom.elements[self.element][0]

    def add_neighrs(self, elt: Atom) -> None:
        pass

    def __hash__(self):      
        return self.id
    
    def __eq__(self, other): 
        return self.id == other.id

    def __str__(self):
        pass