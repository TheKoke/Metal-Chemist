from __future__ import annotations

from atom import Atom, Bound
from errors import *

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.__locked = False
        self.__branchers = list()

        self.formula = str()
        self.bounds: list[Bound] = list()
        self.atoms: list[Atom] = list()
        self.molecular_weight = float()

    def get_formula(self):
        dict_atoms = dict()
        pass
    
    def brancher(self, *args: list[int]) -> Molecule:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be unlocked before change them')
        m = Molecule()
        pass

    def bounder(self, *args: list[tuple[int]]) -> Molecule:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be unlocked before change them')
        pass

    def mutate(self, *args: list[tuple[int]]) -> Molecule:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be unlocked before change them')
        pass

    def add(self) -> None:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be unlocked before change them')
        pass

    def add_chaining(self) -> None:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be unlocked before change them')
        pass

    def closer(self) -> None:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')

        self.locked = True
        for i in range(len(self.bounds)):
            self.bounds[i].fill()

    def unlock(self) -> None:
        if not self.__locked:
            raise UnlockedMolecule('Molecule already unlock.')

        self.locked = False
        for i in range(len(self.bounds)):
            self.__branchers[i].erase()

    def calculate_molecular_weight(self) -> float:
        if not self.locked:
            raise LockedMolecule('Molecule must be locked before get their weight')
        
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])

    def __get_formula(self) -> str:
        if not self.__locked:
            raise UnlockedMolecule('Molecule must be locked before get their formula.')

    def __count_atoms(self) -> None:
        pass