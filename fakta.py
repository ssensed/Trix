#03.04

hovedstad = {"Norge": "Oslo", "Nederland": "Amsterdam", "Spania": "Madrid"}
spraak = {"Norge":"Norsk", "Nederland": "Nederlandsk", "Spania":"Spansk"}
innbyggere = {"Norge":5391369, "Nederland":17282163, "Spania":46733038}

inp = input("gi meg et land\n>")

if inp == "Norge":
    print(hovedstad["Norge"],spraak["Norge"],innbyggere["Norge"])
elif inp == "Nederland":
    print(hovedstad["Nederland"], spraak["Nederland"], innbyggere["Nederland"])
elif inp == "Spania":
    print(hovedstad["Spania"], spraak["Spania"], innbyggere["Spania"])
else:
    print("finnes ikke i registeret")

#c)
