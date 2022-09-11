class ParseHer(object):
    
    # Number:         1      2      3...
    RADICALS    = ["meth", "eth", "prop", "but",   "pent",  "hex",  "hept",  "oct",  "non",  "dec",  "undec",  "dodec",  "tridec",  "tetradec",  "pentadec",  "hexadec",  "heptadec",  "octadec",  "nonadec"]
    MULTIPLIERS = [        "di",  "tri",  "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca", "undeca", "dodeca", "trideca", "tetradeca", "pentadeca", "hexadeca", "heptadeca", "octadeca", "nonadeca"]
    
    SUFFIXES    = [         "ol",      "al", "one", "oic acid", "carboxylic acid",                "oate",               "ether", "amide", "amine", "imine", "benzene", "thiol",    "phosphine", "arsine"]
    PREFIXES    = ["cyclo", "hydroxy",       "oxo",             "carboxy",         "oxycarbonyl", "anoyloxy", "formyl", "oxy",   "amido", "amino", "imino", "phenyl",  "mercapto", "phosphino", "arsino", "fluoro", "chloro", "bromo", "iodo"]
    
    # Note that alkanes, alkenes alkynes, and akyles aren"t present in these lists
    
    def __init__(self, name):
        # Do whatever you want, here....
        pass
    
    def parse(self):
        # Parse the name given as argument in the constructor and output the dict representing the raw formula
        pass