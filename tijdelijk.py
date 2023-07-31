prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
a = int(prijzen["aardbei"])
b = int("0.8")
aanbieding = int(a*b)
reclame_tekst = "Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts €{aanbieding}"
reclame_tekst2 = "reclame_tekst[:63]"
reclame_tekst3 = ("reclame_tekst2".upper())
reclame_tekst4 = ("reclame_tekst3".split(" "))
for el in reclame_tekst4:
    print(el)
if len(el)>=5:
    print (el.upper())
else:
    print (el.lower())