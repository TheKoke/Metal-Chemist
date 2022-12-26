from __future__ import annotations

from atom import Atom, Brancher
from errors import *

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.locked = False

        self.formula = str()
        self.__branchers: list[Atom] = list()
        self.atoms: list[Atom] = list()
        self.molecular_weight = float()

    def get_formula(self) -> str:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get their formula.')

        dict_atoms = self.__count_atoms()
    
    def brancher(self, *args: list[int]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')

        for i in range(len(args)):
            self.__new_brancher(args[1])

        return self

    def bounder(self, *args: list[tuple[int]]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        for i in range(len(args)):
            c1: int = args[i][0]; b1: int = args[i][1]
            c2: int = args[i][2]; b2: int = args[i][3]
            self.__merger(b1, b2, c1, c2)

        return self

    def mutate(self, *args: list[tuple[int]]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        for i in range(len(args)):
            nc: int = args[i][0]; nb: int = args[i][1]; elt: str = args[i][2]

        return self

    def add(self, nc: int, nb: int, elt: str) -> None:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        return self

    def add_chaining(self, nc: int, nb: int, *args: list[str]) -> None:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')
        
        return self

    def closer(self) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule is locked.')

        self.locked = True
        self.__fill()

        return self

    def unlock(self) -> Molecule:
        if not self.locked:
            raise UnlockedMolecule('Molecule already unlock.')

        if len(self.atoms) == 0:
            raise EmptyMolecule('WTF? Molecule has been empty')

        self.locked = False
        self.__erase()

        return self

    def calculate_molecular_weight(self) -> float:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get their weight')
        
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])

    def __new_brancher(self, carbon: int) -> None:
        pass

    def __fill(self) -> None:
        pass

    def __erase(self) -> None:
        pass

    def __merger(self, first_branch: int, second_branch: int, pos1: int, pos2: int) -> bool:
        pass

    def __count_atoms(self) -> dict[Atom, int]:
        return {self.atoms[i] : self.atoms.count(self.atoms[i]) for i in range(len(self.atoms))}