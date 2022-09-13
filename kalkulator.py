#02.17

def kalkulator():
    inp_tall1 = input("Skriv inn et tall.\n>")
    tall = int(inp_tall1)
    print("Tallet er:", tall)

    inp_tall2 = input("Skriv inn et tall til.\n>")
    tall2 = int(inp_tall2)
    print("Tallet er:", tall2)

    inp_operasjon = input("Skriv inn en operasjon.\n>")
    operasjon = inp_operasjon
    print("Operasjonen er:", operasjon)

    if operasjon == "+":
        print("Resultatet er:",tall + tall2)
    elif operasjon == "-":
        print("Resultatet er:",tall - tall2)
    elif operasjon == "*":
        print("Resultatet er:",tall*tall2)
    elif operasjon == "/":
        print("Resultatet er:",tall/tall2)

kalkulator()
