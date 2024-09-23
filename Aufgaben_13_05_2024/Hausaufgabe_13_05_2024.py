# Dieser Program Ist eine Test um sich einzulogen
print("Vorname?")
feeling = input()
print(" was ist dein Vor und Nachname? ", feeling)

print("Vor und Nachname?")
feeling = input()
print(" was ist deine Strasse ?  ", feeling)

print("strasse?")
feeling = input()
print("und die nummer von ",feeling)

print("Nummer?")
feeling = input()
print("jez noch der Wohnort ? ")

feeling = input()

print("Du bist eingelogt?")
#Aufgabe 1


#Aufgabe 3 das programm sollte ein Glücksspiel darstellen 
import random
zahl=random.randint(1, 15)

print ("wähle eine Nummer von 1 bis 15!")
feeling = input()

if feeling == zahl:
    print("Glückwunsch, sie haben die Zahl getroffen!")
else:
    print("Schade! War diesmal leider nichts! Probieren sie es noch einmal")



