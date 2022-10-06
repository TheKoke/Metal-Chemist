from atom import Atom

class Molecule(object):
    def __init__(self, name: str = str()) -> None:
        self.name = name
        self.formula = str()
        self.atoms = list()
        self.molecular_weight = float()
    
    def brancher(self, *args) -> None:
        pass

    def bounder(self) -> None:
        pass

    def mutate(self) -> None:
        pass

    def add(self) -> None:
        pass

    def add_chaining(self) -> None:
        pass

    def closer(self) -> None:
        self.atoms = tuple(self.atoms)

    def unlock(self) -> None:
        pass

    def calculate_molecular_weight(self) -> float:
        return sum([list(self.atoms)[i].get_weight() for i in range(len(list(self.atoms)))])