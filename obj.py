#03.05
#a) få inn et ord
ord = input("gi meg et ord")
#b) skriver ut i store bokstaver
print(ord.upper())
#c) hvor langt ordet er
print("hvor mange tegn ordet har:",len(ord))
#d)
foerste = ord[0]

print("foerste tegnet i ordet:",foerste)

#)
#teller hvor mange ganger foerste forekommer i ordet med for-løkke
counter = 0

for x in ord:
    if x == foerste:
        if foerste in ord:
            counter +=1
        else:
            counter = 1

print("den forekommer",counter, "ganger i ordet", ord)
#gjør samme som den over, men med count
print("den forekommer", ord.count(foerste), "ganger i ordet", ord)
