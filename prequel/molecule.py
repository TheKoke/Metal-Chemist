from __future__ import annotations

from atom import Atom, Brancher
from errors import *

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.locked = False

        self.formula = str()
        self.branchers: list[Brancher] = list()
        self.atoms: list[Atom] = list()
        self.molecular_weight = float()

    def get_formula(self) -> str:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get their formula.')
        dict_atoms = self.__count_atoms()
    
    def brancher(self, *args: list[int]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')

        return self

    def bounder(self, *args: list[tuple[int]]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        

        return self

    def mutate(self, *args: list[tuple[int]]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        

        return self

    def add(self) -> None:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        return self

    def add_chaining(self) -> None:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        return self

    def closer(self) -> None:
        if self.locked:
            raise LockedMolecule('Molecule is locked.')

        self.locked = True
        for i in range(len(self.branchers)):
            self.branchers[i].fill()

    def unlock(self) -> None:
        if not self.locked:
            raise UnlockedMolecule('Molecule already unlock.')

        self.locked = False
        for i in range(len(self.branchers)):
            self.branchers[i].erase()

    def calculate_molecular_weight(self) -> float:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get their weight')
        
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])

    def __count_atoms(self) -> dict[Atom, int]:
        return {self.atoms[i] : self.atoms.count(self.atoms[i]) for i in range(len(self.atoms))}