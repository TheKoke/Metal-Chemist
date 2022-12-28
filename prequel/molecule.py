from __future__ import annotations

from atom import Atom
from errors import *

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name

        self.locked = False
        self.__branchers: list[list[Atom]] = list()

    @property
    def formula(self) -> str:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get them formula')

        dict_atoms = self.__count_atoms()

        picture = ''

        for element in Atom.elements:
            if element in dict_atoms:
                count = dict_atoms[element]
                if count == 1: picture += element
                else: picture += element + f'{count}'

        return picture
    
    @property
    def atoms(self) -> list[Atom]:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get their atoms')

        result = []

        id_counter = 1
        for i in range(len(self.__branchers)):
            for atom in self.__branchers[i]:
                if atom.element != 'C':
                    atom.id = 1
                else:
                    atom.id = id_counter
                    id_counter += 1
                result.append(atom)

        return result

    @property
    def molecular_weight(self) -> float:
        if not self.locked:
            raise UnlockedMolecule('Molecule must be locked before get them mass')

        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])
    
    def brancher(self, *args: list[int]) -> Molecule:
        if self.locked:
            raise LockedMolecule('Molecule must be unlocked before change them')

        for i in range(len(args)):
            self.__new_brancher(args[i])

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
            raise LockedMolecule('Molecule is already locked.')

        self.locked = True

        self.__fill()

        return self

    def unlock(self) -> Molecule:
        if not self.locked:
            raise UnlockedMolecule('Molecule is already unlock.')

        if len(self.atoms) == 0:
            raise EmptyMolecule('WTF? Molecule has been empty')

        self.locked = False
        self.__erase()

        return self

    def __new_brancher(self, carbon: int) -> None:
        self.__branchers.append([Atom('C', i + 1) for i in range(carbon)])

        if len(self.__branchers[-1]) == 1:
            return

        for i in range(len(self.__branchers[-1])):
            if i == 0:
                self.__branchers[-1][i].add_neighrs(self.__branchers[-1][i + 1])
            
            if i == len(self.__branchers[-1]) - 1:
                self.__branchers[-1][i].add_neighrs(self.__branchers[-1][i - 1])

            if i not in [0, len(self.__branchers[-1]) - 1]:
                self.__branchers[-1][i].add_neighrs(self.__branchers[-1][i + 1])
                self.__branchers[-1][i].add_neighrs(self.__branchers[-1][i - 1])

    def __fill(self) -> None:
        hydrogen = Atom('H', 1)
        for i in range(len(self.__branchers)):
            for j in range(len(self.__branchers[i])):
                temp = True
                while temp:
                    temp = self.__branchers[i][j].add_neighrs(hydrogen)
                    if temp:
                        self.__branchers[i].append(hydrogen)

    def __erase(self) -> None:
        hydrogen = Atom('H', 1)
        for i in range(len(self.__branchers)):
            for j in range(len(self.__branchers[i])):
                while hydrogen in self.__branchers[i][j].neighrs:
                    self.__branchers[i][j].neighrs.remove(hydrogen)
                    self.__branchers[i].remove(hydrogen)

    def __merger(self, first_branch: int, second_branch: int, pos1: int, pos2: int) -> bool:
        # if elt1 >= len(self.atoms) or elt2 >= len(another.atoms):
        #    return False

        # if len(self.atoms[elt1].neighrs) == self.atoms[elt1].get_valence() \
        # or len(another.atoms[elt2].neighrs) == another.atoms[elt2].get_valence():
        #    return False

        # self.atoms[elt1].add_neighrs(Atom(another.atoms[elt2], len(another.atoms) + 1))
        # another.atoms[elt2].add_neighrs(Atom(self.atoms[elt1], len(self.atoms) + 1))
        pass

    def __count_atoms(self) -> dict[str, int]:
        res = dict()

        for atom in self.atoms:
            if atom.element in res:
                res[atom.element] += 1
            else:
                res[atom.element] = 1
        
        return res