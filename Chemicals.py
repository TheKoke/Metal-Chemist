class Alkane:
    def __init__(self, carbons: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.cyclic = cyclic if carbons > 2 else False

    def draw(self) -> str:
        if self.carbon_count == 1:
            return 'CH4'

        chains = ['C' for i in range(self.carbon_count)]
        for i in range(self.carbon_count):
            if i in [0, len(chains) - 1]:
                chains[i] += 'H3'
            else:
                chains[i] += 'H2'

        return '-'.join(chains)

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2 + 2}

class Alkene:
    def __init__(self, carbons: int, isomer: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.isomer = isomer

        self.cyclic = cyclic if carbons > 2 else False

        if carbons < 2:
            self.carbon_count = 2

    def draw(self) -> str:
        chains = ['C' for i in range(self.carbon_count)]

        for i in range(self.carbon_count):
            if i in [self.isomer, self.isomer - 1] and i not in [0, len(chains) - 1]:
                chains[i] += 'H'
                continue
                
            if i in [self.isomer, self.isomer - 1] and i in [0, len(chains) - 1]:
                chains[i] += 'H2'
                continue

            if i in [0, len(chains) - 1]:
                chains[i] += 'H3'
                continue

            if i not in [0, len(chains) - 1]:
                chains[i] += 'H2'
                continue
        
        chains[self.isomer - 1] += '=' + chains[self.isomer]
        chains.pop(self.isomer)

        return '-'.join(chains)    

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2}

class Alkyne:
    def __init__(self, carbons: int, isomer: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.isomer = isomer
        
        self.cyclic = cyclic if carbons > 2 else False

        if carbons < 2:
            self.carbon_count = 2
            
    def draw(self) -> str:
        chains = ['C' for i in range(self.carbon_count)]

        for i in range(self.carbon_count):
            if i in [self.isomer, self.isomer - 1] and i not in [0, len(chains) - 1]:
                continue
                
            if i in [self.isomer, self.isomer - 1] and i in [0, len(chains) - 1]:
                chains[i] += 'H'
                continue

            if i in [0, len(chains) - 1]:
                chains[i] += 'H3'
                continue

            if i not in [0, len(chains) - 1]:
                chains[i] += 'H2'
                continue
        
        chains[self.isomer - 1] += '{=}' + chains[self.isomer]
        chains.pop(self.isomer)

        return '-'.join(chains)

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2 - 2}