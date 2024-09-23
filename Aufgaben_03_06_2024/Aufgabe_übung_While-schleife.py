#gluckspiel du musst die richtige zahl herausfinden.
import random
zahl=random.randint(1, 10) # random ist damit man verschiedene zahlen bekommt
print(zahl)
i=0

while True: # while ist dafür da das man mehrere durchlaufe hat. 
        try: #ist dafür da das der programm nicht abstürtzt
            print("Zahl eingabe?")
            feeling = int(input()) #int ist dafür damit man das geschriebene in zahl umwandelt
            if feeling == zahl:
                print("Glückwunsch du hast die richtie Zahl gefunden")
                break
            else:
                print("Schade versuche es noch einma!")
        except:
            print("Du hast keine zahl eingebenen")





 
