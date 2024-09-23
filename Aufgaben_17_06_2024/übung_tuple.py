personen = [("Max", "01.01.2000"), ("Anna", "15.03.1998"), ("Tom", "10.07.2005")]

def  aeltere_personen(personen): #Hier wird die Funktion aeltere_personen definiert, die eine Liste von Tupeln personen als Eingabe erhält
    alter= [] #Das ist eine leere liste das ist dafür da den gewünsten ergebmiss zu speichern. 

    
    
    
    
    for name, geburtstag in personen: #Eine for-Schleife iteriert über jedes Tupel in der Liste personen. Jedes Tupel enthält den Namen (name) und den Geburtstag (geburtstag) einer Person
        jahr = int(geburtstag.split(".")[-1]) #Der Geburtstag ist ein String im Format "TT.MM.JJJJ"
                                              #.geburtstag.split(".") teilt den String am Punkt in eine Liste von drei Teilen: ["TT", "MM", "JJJJ"].
                                              #[-1] gibt das letzte Element dieser Liste zurück, was das Jahr ("JJJJ") ist.int() konvertiert dieses Jahr von einem String in eine Ganzzahl
        if jahr < 2000:                       #Eine if-Bedingung prüft, ob das extrahierte Jahr kleiner als 2000 ist. Wenn die Bedingung erfüllt ist, wird der Name der Person der Liste aeltere hinzugefügt
            alter.append(name)
    return alter                              # Nachdem die Schleife alle Personen durchlaufen hat, wird die Liste aeltere zurückgegeben.
print("das ist die Person die vor dem Jahr 2000 geboren worden ist.", (aeltere_personen(personen)))



# Funktion neue_liste(personen)
def liste2 (personen):
    neue_liste = [(geburtstag, name) for name, geburtstag in personen]
    return neue_liste

# Beispielaufruf
print("Neue Liste mit vertauschten Namen und Geburtstagen:", liste2 (personen))


# Funktion doppelte_geschenke(personen)
def doppelte_geschenke(personen):
    geburtstage = {}
    for name, geburtstag in personen:
        if geburtstag in geburtstage:
            geburtstage[geburtstag].append(name)
        else:
            geburtstage[geburtstag] = [name]
    doppelte = [geburtstag for geburtstag, namen in geburtstage.items() if len(namen) > 1]
    return doppelte

# Beispielaufruf mit doppelten Geburtstagen
personen_mit_doppeln = [("Max", "01.01.2000"), ("Anna", "15.03.1998"), ("Tom", "10.07.2005"), ("Lena", "01.01.2000")]
print("Geburtstage mit mehr als einer Person:", doppelte_geschenke(personen_mit_doppeln))




