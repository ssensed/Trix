#02.08

temperatur = (float(input("Hva er din kroppstemperatur?\n>")))

if temperatur > 36.5:
    if temperatur < 37.5:
        print("du er innenfor")
if temperatur > 37.5:
    print("du har feber")
if temperatur < 36.5:
    print("du er for kald")
