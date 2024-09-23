liste=[3, 7, 1, 9, 4, 6, 9, 4,]
#hier ist die Definition von der Summe wenn ich alle Zahlen zussamenzählen möchte!!
def summe(liste):
    return sum(liste)
# hier bekommt man die Summe von allen Zahlen
print("Das ergebniss von allen Zahlen ist:", summe(liste))


#Hier ist die Definition wenn ich die grösste Zahl herausfinden möchte
def groesste_zahl(liste):
    return max(liste)
# Hier können wir die grösste Zahl herauslesen in einer Liste
print("Größte Zahl:", groesste_zahl(liste))


#hier ist die definition zum eine liste Sortieren !!
def liste_sortieren(liste):
    return sorted(liste)
print("Die Zahlen wurden alle sortiert", liste_sortieren(liste))


#mit dieser Funktion kann man das doppelte in einer Liste löschen aber es macht es nicht Automatisch
liste.remove(9)
print("hier sind die Doppelten zahlen entfernt worden", (liste))


#Hier ist das Bessere code zum eine Zahl oder Wort entfernen wenn es doppelt ist, es erkennt und wirt Automatisch gelösst!!
def entferne_doppelte(liste):
    gesehen = set() # mit Set kann die Zahl nur 1 mall vorkommen!!!
    resultat = [] # hier machen wir eine neue lieste ohne doppelte elemente
    for zahl in liste:
        if zahl not in gesehen: #Fals die Zahl 1 mall vorkommt kommt es in der Liste (resultat) hinein
            resultat.append(zahl) #append ist dafür do das er dia Zahla 1 nochem andera in lista fügt und kontrolliert.
            gesehen.add(zahl)    #Fals die Zahl doppelt vorkommt kommt es in der Liste hinein!! 
    return resultat

# Das ist der Code für doppelte Elemente entfernen!!
zahlen_mit_doppeln = [3, 7, 1, 9, 4, 6, 9, 4,]
print("Liste ohne doppelte Elemente:", entferne_doppelte(zahlen_mit_doppeln)) 




