flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"],
            "sverige" : ["blått", "gult"],
            "danmark" : ["rødt", "hvitt"],
            "finland" : ["hvitt", "blått"],
            "japan" : ["rødt", "hvitt"],
            "gabon" : ["grønt", "gult", "blått"],
            "storbritannia" : ["rødt", "blått", "hvitt"],
            "chile" : ["blått", "hvitt", "rødt"]}

print(flaggOrdbok)

[flaggOrdbok["filippinene"]] = ["rødt"]
[flaggOrdbok["filippinene"]] = ["blått"]
[flaggOrdbok["filippinene"]] = ["hvitt"]
[flaggOrdbok["filippinene"]] = ["gult"]


print(flaggOrdbok)

def prosedyre():
    navn = input("give me a name").lower() or input("give me a name").upper()
    if navn in flaggOrdbok:
        [flaggOrdbok[navn]]

    farge = input("give me a color")
    
    if farge in flaggOrdbok[navn]:
        print("ja, den fargen er der")

prosedyre()
