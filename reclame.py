
from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs * korting} euro."
    return uitvoer
def inkomsten_totaal(inkomsten):
    totaal = 0
    for x in inkomsten:
           totaal += x
    btw = float(inkomsten_totaal * 0.09)
    uitvoer2 = f"Het totaal van alle inkomsten van deze week is {inkomsten_totaal} euro, waarover {btw} euro btw betaald dient te worden."
    return uitvoer2
def laag_en_hoog(mijn_lijst):
    uitvoer3 = max(mijn_lijst), min(mijn_lijst)
    return uitvoer3
def gemiddelde(mijn_lijst):
     lengte = len(mijn_lijst)
     som = sum(mijn_lijst)
     uitvoer4 = f"De gemiddelde inkomsten van deze week zijn {som / lengte} euro."
     return uitvoer4
def meervoudig(invoer_lijst):
     uitvoer5= int(laag_en_hoog(invoer_lijst))
     return uitvoer5
def combinatie(invoer_lijst_2):
     korte_lijst = laag_en_hoog(invoer_lijst_2)
     uitvoer6 = mijn_functie_2(korte_lijst[0], korte_lijst[1])
     return uitvoer6