from __future__ import annotations

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
        self.neighrs = list()
        
    def get_weight(self) -> float:
        return Atom.elements[self.element][1]

    def get_valence(self) -> int:
        return Atom.elements[self.element][0]

    def add_neighrs(self, elt: Atom) -> bool:
        if len(self.neighrs) == self.get_valence():
            return False

        self.neighrs.append(elt)
        return True

    def __hash__(self) -> int:      
        return self.id
    
    def __eq__(self, other: Atom) -> bool: 
        return self.id == other.id

    def __str__(self) -> str:
        format = f'Atom({self.element}.{self.id}'
        if len(self.neighrs) == 0:
            return format + ')'

        format += ': '
        return format + ', '.join([f'{self.neighrs[i]}' for i in range(len(self.neighrs))]) + ')'
        

# class Brancher:
#     def __init__(self, carbon: int, id: int) -> None:
#         self.carbon = carbon
#         self.atoms = [Atom('C', i + 1) for i in range(carbon)]
#         self.id = id
#         self.locked = False

#     def fill(self) -> None:
#         for atom in self.atoms:
#             temp = atom.add_neighrs(Atom('H', 1))
#             while temp:
#                 self.atoms.append(Atom('H', 1))
#                 temp = atom.add_neighrs(Atom('H', 1))

#     def erase(self) -> None:
#         for atom in self.atoms:
#             while "H" in atom.neighrs:
#                 atom.neighrs.remove("H")

#     def merger(self, another: Brancher, elt1: int, elt2: int) -> bool:
#         if elt1 >= len(self.atoms) or elt2 >= len(another.atoms):
#             return False

#         if len(self.atoms[elt1].neighrs) == self.atoms[elt1].get_valence() \
#         or len(another.atoms[elt2].neighrs) == another.atoms[elt2].get_valence():
#             return False

#         self.atoms[elt1].add_neighrs(Atom(another.atoms[elt2], len(another.atoms) + 1))
#         another.atoms[elt2].add_neighrs(Atom(self.atoms[elt1], len(self.atoms) + 1))

#         return True
