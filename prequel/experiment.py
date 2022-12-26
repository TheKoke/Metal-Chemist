from molecule import Molecule

molec = Molecule("octane").brancher(1).closer()

for i in range(len(molec.__branchers)):
    for j in range(len(molec.__branchers[i].atoms)):
        print(str(molec.__branchers[i].atoms[j]))