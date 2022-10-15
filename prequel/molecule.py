from __future__ import annotations

from atom import Atom, Brancher
from errors import EmptyMolecule, LockedMolecule, UnlockedMolecule, InvalidBond

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.__locked = False
        self.__branchers = list()

        self.formula = str()
        self.atoms = list()
        self.molecular_weight = float()
    
    def brancher(self, *args: list[int]) -> Molecule:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')

        for i in range(len(args)):
            self.__branchers.append(Brancher(args[i]))
        return self

    def bounder(self, *args: list[tuple[int]]) -> Molecule:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')
        return self

    def mutate(self, *args: list[tuple[int]]) -> Molecule:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')
        return self

    def add(self) -> None:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')

    def add_chaining(self) -> None:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')

    def closer(self) -> None:
        if self.__locked:
            raise LockedMolecule('Molecule is locked.')

        self.locked = True
        for i in range(len(self.bounds)):
            self.__branchers[i].fill()

    def unlock(self) -> None:
        if not self.__locked:
            raise UnlockedMolecule('Molecule already unlock.')

        self.locked = False
        for i in range(len(self.bounds)):
            self.__branchers[i].erase()

        self.atoms = self.__count_atoms()
        if len(self.atoms) == 0:
            raise EmptyMolecule('Molecule is empty.')

        self.formula = self.__get_formula()
        self.molecular_weight = self.__calculate_molecular_weight()

    def __calculate_molecular_weight(self) -> float:
        if not self.__locked:
            raise UnlockedMolecule('Molecule must be locked before get their weight.')
        
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])

    def __get_formula(self) -> str:
        if not self.__locked:
            raise UnlockedMolecule('Molecule must be locked before get their formula.')

    def __count_atoms(self) -> None:
        pass