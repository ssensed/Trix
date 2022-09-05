string = input("skriv en tekst\n>")
heltall = int(input("Skriv et tall\n>"))
flyttall = float(input("Skriv et desimaltall.\n>"))

#a)

print(type(string))
print(type(heltall))
print(type(flyttall))

#b)

'''
det jeg trodde skulle skje:
- kjøre
- kræsje
- kræsje
- kræsje

det som skjedde:
- kjørte
- kjørte
- kjørte
- kræsjet
'''

#c)
print(string*heltall)
print(heltall*flyttall)
#print(string*flyttall)

'''
det jeg tror kommer til å skje:
- stringen blir multiplisert 3 ganger, så om stringen er 3 og heltall er 3,
kommer det ut 333

- to tall blir ganget med hverandre

- error'''

#d)

print(int(flyttall))
#det blir rundet ned til nærmeste heltall
