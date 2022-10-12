#03.02

#a)

liste = ["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]

print("antall ord i listen:",len(liste))

#b)

liste_til_mengde = set(liste)

print("unike ord:",len(liste_til_mengde))

#c)

lykkelig = 0

def forekommer(lykkelig):
    for x in liste:
        if x == "lykkelig":
            if "lykkelig" in liste:
                lykkelig +=1
            else:
                lykkelig = 1
    return lykkelig

print("hvor mange ganger lykkelig forekommer:",forekommer(lykkelig))

så = 0
def forekommer2(så):
    for y in liste:
        if y == "så":
            if "så" in liste:
                så +=1
            else:
                så = 1
    return så

print("hvor mange ganger så forekommer:",forekommer2(så))

dag = 0

def forekommer3(dag):
    for z in liste:
        if z == "dag":
            if "dag" in liste:
                dag +=1
            else:
                dag = 1
    return dag

print("hvor mange ganger dag forekommer:", forekommer3(dag))

#d)

min_ordbok = {}

min_ordbok["lykkelig"] = forekommer(lykkelig)
min_ordbok["så"] = forekommer2(så)
min_ordbok["dag"] = forekommer3(dag)

print(min_ordbok)

#e)
#her får man nøkkel-verdiene i ordboken som mengder
print(set(min_ordbok))
#her får man nøkkel-verdiene i ordboken som en liste
print(list(min_ordbok))
