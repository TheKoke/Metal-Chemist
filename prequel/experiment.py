from molecule import Molecule

molec = Molecule("octane").brancher(5).closer()

print(molec.formula)