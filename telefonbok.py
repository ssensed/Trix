telefonbok = {"Arne": 22334455, "Lisa":95959595, "Jonas":97959795, "Peder":12345678}

navn = input("skriv inn et navn")

if navn in telefonbok:
    print(telefonbok[navn])
else:
    nummer = int(input("what is your number?"))
    telefonbok[nytt_navn] = nummer
    print(telefonbok)
