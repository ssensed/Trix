#03.03

#a) liste over alle måneder i året
maaneder = ["januar", "februar", "mars", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "desember"]
#b) ta imot et heltall fra brukeren
heltall = int(input("gi meg et tall\n>"))


# if heltall <= len(maaneder):
#     print(maaneder[heltall])

#om heltallet er mer enn lengden eller samme som lengden av listen, print ugyldig
if heltall >= len(maaneder):
    print("ugyldig")
#hvis ikke, print plassering [heltall] i listen maaneder.
else:
    print(maaneder[heltall])
