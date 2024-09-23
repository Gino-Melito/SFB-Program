#Hier ersätzt man die liste mit ein andere wert
Stadt=["Luzern","Zürich","Basel"]
Stadt[2]= "Genf"
print("Hier wurde Basel mi Genf ersätzt", (Stadt))

#Hier wurde die Aktuele lieste erweitert. !!
Stadt2=["Bern", "Lausanne", "Winterthur", "St. Gallen"]
Neue_liste= Stadt+Stadt2
print("Das ist die Aktuelle liste mit erweiterung!",(Neue_liste))


#Hier werden die verschiedene funktionen gezeigt mit () mit [] oder auch {}!!
datentypen = (1, 3.14, True, "Text", None, [1, 2, 3], {"Schlüssel": "Wert"}, (1, 2), {1, 2, 3})
print("Tupel mit verschiedenen Datentypen:", (datentypen))

Zahlen = 2, 4, 5, 6, 2, 3, 4, 4, 7
Mehrfach=Zahlen.count(4)
print("Anzahl des Vorkommens der Nummer 4:", (Mehrfach))