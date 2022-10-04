class Alkane:
    def __init__(self, carbons: int, cyclic: bool, alkyl: bool) -> None:
        self.carbon_count = carbons
        self.cyclic = cyclic if carbons > 2 else False
        self.alkyl = alkyl
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
        return MoleculeParser.parse('-'.join(self.chains))

class Alkene:
    def __init__(self, carbons: int, isomer: int) -> None:
        self.carbon_count = carbons
        self.isomer = isomer
        self.chains = self.get_chains()

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
        return MoleculeParser.parse('-'.join(self.chains))

class Alkyne:
    def __init__(self, carbons: int, isomer: int) -> None:
        self.carbon_count = carbons
        self.isomer = isomer
        self.chains = self.get_chains()

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
        return MoleculeParser.parse('-'.join(self.chains))

# class for parsing molecules to atoms
class MoleculeParser:
    brackets = {'(' : ')', '{' : '}', '[' : ']'}

    @staticmethod
    def parse(molecule: str) -> dict[str, int]:
        atoms = dict()
        i = 0

        while i < len(molecule):
            if molecule[i] in MoleculeParser.brackets:
                inBracket = MoleculeParser.handling_brackets(molecule, i)
                i = inBracket[1]

                MoleculeParser.merge_dicts(atoms, inBracket[0])

            if molecule[i].isupper():
                pretend = MoleculeParser.next_atom(molecule, i)
                pretendTuple = (pretend, MoleculeParser.find_factor(molecule, i + len(pretend) - 1))

                MoleculeParser.add_to_dict(atoms, pretendTuple)
            i += 1
            
        return atoms

    @staticmethod
    def next_atom(molecule: str, index: int) -> str:
        pretend = molecule[index]
        index += 1

        while index < len(molecule) and molecule[index].islower():
            pretend += molecule[index]
            index += 1
        return pretend

    @staticmethod
    def handling_brackets(molecule: str, index: int) -> dict[str, int]:
        closeIndex = MoleculeParser.find_close_bracket(molecule, index)
        if closeIndex == -1:
            raise ValueError('Problems with brackets')
        
        inBracket = molecule[index + 1: closeIndex:]
        factor = MoleculeParser.find_factor(molecule, closeIndex)

        return MoleculeParser.multiply_dict(MoleculeParser.parse(inBracket), factor), closeIndex

    @staticmethod
    def find_close_bracket(molecule: str, openIndex) -> int:
        temp = 0
        for i in range(openIndex + 1, len(molecule)):
            if molecule[i] == molecule[openIndex]:
                temp += 1
                continue

            if molecule[i] == MoleculeParser.brackets[molecule[openIndex]] and temp != 0:
                temp -= 1
                continue

            if molecule[i] == MoleculeParser.brackets[molecule[openIndex]] and temp == 0:
                return i
        return -1

    @staticmethod
    def multiply_dict(destination: dict[str, int], factor: int)  -> dict[str, int]:
        for i in destination:
            destination[i] *= factor
        return destination

    @staticmethod
    def find_factor(molecule: str, endIndex: int) -> int:
        if endIndex + 1 < len(molecule) and molecule[endIndex + 1].isnumeric():
            res = molecule[endIndex + 1]

            for i in range(endIndex + 2, len(molecule)):
                if molecule[i].isnumeric():
                    res += molecule[i]
                else:
                    break
            return int(res)
        return 1

    @staticmethod
    def add_to_dict(destination: dict[str, int], atom: tuple[str, int]):
        if atom[0] != '':
            if atom[0] in destination:
                destination[atom[0]] += atom[1]
            else:
                destination[atom[0]] = atom[1]

    @staticmethod
    def merge_dicts(first: dict[str, int], second: dict[str, int]):
        for i in second:
            if i in first:
                first[i] += second[i]
            else:
                first[i] = second[i]