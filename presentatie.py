from helper import *
import csv
def presenteer (mijn_dict, totaal):
    mijn_dict = {
        'vis' : 10, 
        'vlees' : 25, 
        'overig' : 15
        }
    totaal = som(key, value)
    uitvoer = onderstreep(mijn_dict)
    uitvoer.append("Totaal {totaal} euro")
    print()
    for el in uitvoer:
        print (el)
with open ('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])