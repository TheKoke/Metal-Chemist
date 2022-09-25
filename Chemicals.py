class Alkane:
    def __init__(self, carbons: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.cyclic = cyclic if carbons > 2 else False
        self.chains = self.get_chains()

    def get_chains(self) -> list[str]:
        if self.carbon_count == 1:
            return ['CH4']

        picture = ['C' for i in range(self.carbon_count)]
        for i in range(self.carbon_count):
            if i in [0, len(picture) - 1]:
                picture[i] += 'H3'
            else:
                picture[i] += 'H2'

        return picture

    def erase(self, chain_index: int) -> None:
        if self.chains[chain_index][-1].isdigit():
            h_count = int(self.chains[chain_index][-1])
            self.chains[chain_index] = f'CH{h_count}'
        else:
            self.chains[chain_index] = 'C'

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2 + 2}

class Alkene:
    def __init__(self, carbons: int, isomer: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.isomer = isomer
        self.chains = self.get_chains()

        self.cyclic = cyclic if carbons > 2 else False

        if carbons < 2:
            self.carbon_count = 2

    def get_chains(self) -> list[str]:
        picture = ['C' for i in range(self.carbon_count)]

        for i in range(self.carbon_count):
            if i in [self.isomer, self.isomer - 1] and i not in [0, len(picture) - 1]:
                picture[i] += 'H'
                continue
                
            if i in [self.isomer, self.isomer - 1] and i in [0, len(picture) - 1]:
                picture[i] += 'H2'
                continue

            if i in [0, len(picture) - 1]:
                picture[i] += 'H3'
                continue

            if i not in [0, len(picture) - 1]:
                picture[i] += 'H2'
                continue
        
        picture[self.isomer - 1] += '=' + picture[self.isomer]
        picture.pop(self.isomer)

        return picture

    def erase(self, chain_index: int) -> None:
        if self.chains[chain_index][-1].isdigit():
            h_count = int(self.chains[chain_index][-1])
            self.chains[chain_index] = f'CH{h_count}'
        else:
            self.chains[chain_index] = 'C'

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2}

class Alkyne:
    def __init__(self, carbons: int, isomer: int, cyclic: bool) -> None:
        self.carbon_count = carbons
        self.isomer = isomer
        self.chains = self.get_chains()
        
        self.cyclic = cyclic if carbons > 2 else False

        if carbons < 2:
            self.carbon_count = 2
            
    def get_chains(self) -> list[str]:
        picture = ['C' for i in range(self.carbon_count)]

        for i in range(self.carbon_count):
            if i in [self.isomer, self.isomer - 1] and i not in [0, len(picture) - 1]:
                continue
                
            if i in [self.isomer, self.isomer - 1] and i in [0, len(picture) - 1]:
                picture[i] += 'H'
                continue

            if i in [0, len(picture) - 1]:
                picture[i] += 'H3'
                continue

            if i not in [0, len(picture) - 1]:
                picture[i] += 'H2'
                continue
        
        picture[self.isomer - 1] += '{=}' + picture[self.isomer]
        picture.pop(self.isomer)

        return picture

    def erase(self, chain_index: int) -> None:
        if self.chains[chain_index][-1].isdigit():
            h_count = int(self.chains[chain_index][-1])
            self.chains[chain_index] = f'CH{h_count}'
        else:
            self.chains[chain_index] = 'C'

    def parse_to_atoms(self) -> dict[str, int]:
        return {'C': self.carbon_count, 'H': self.carbon_count * 2 - 2}


class Alkyl:
    def __init__(self, carbon_count: int) -> None:
        self.carbon_count = carbon_count
    
    def get_chains(self) -> list[str]:
        picture = []

        return picture