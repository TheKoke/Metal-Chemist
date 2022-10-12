from __future__ import annotations

from atom import Atom, Bound
from errors import EmptyMolecule, LockedMolecule, UnlockedMolecule, InvalidBond

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.locked = False
        self.formula = str()
        self.bounds = list()
        self.atoms = list()
        self.molecular_weight = float()

    def refresh(self) -> None:
        pass

    def get_formula(self):
        dict_atoms = dict()
        pass
    
    def brancher(self, *args: list[int]) -> Molecule:
        m = Molecule()
        pass

    def bounder(self, *args: list[tuple[int]]) -> Molecule:
        pass

    def mutate(self, *args: list[tuple[int]]) -> Molecule:
        pass

    def add(self) -> None:
        pass

    def add_chaining(self) -> None:
        pass

    def closer(self) -> None:
        self.locked = True
        for i in range(len(self.bounds)):
            self.bounds[i].fill()

        self.refresh()

    def unlock(self) -> None:
        self.locked = False
        for i in range(len(self.bounds)):
            self.bounds[i].erase()

        self.refresh()

    def calculate_molecular_weight(self) -> float:
        if not self.locked:
            raise LockedMolecule('Molecule must be locked before get their weight')
        
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])