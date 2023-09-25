from helper import *
def presenteer (mijn_dict, totaal):
    totaal = som(mijn_dict)
    uitvoer = onderstreep(mijn_dict)
    uitvoer.append(f"Totaal {totaal} euro")
    print()
    for el in uitvoer:
        print (el)