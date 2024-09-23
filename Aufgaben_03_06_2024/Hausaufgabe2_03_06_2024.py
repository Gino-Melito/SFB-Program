def berechne_bmi(gewicht, groesse):
    # Berechnung des BMI
    bmi = gewicht / (groesse ** 2)
    return bmi

def main():
    # Benutzereingaben für Gewicht und Größe
    gewicht = float(input("Bitte geben Sie Ihr Gewicht in kg ein: "))
    groesse = float(input("Bitte geben Sie Ihre Größe in m ein: "))
    
    # Berechnung des BMI
    bmi = berechne_bmi(gewicht, groesse)
    
    # Ausgabe des BMI
    print(f"Ihr Body-Mass-Index (BMI) beträgt: {bmi:.2f}")
    
    # Bestimmung der Gewichtskategorie
    if bmi < 18.5:
        print("Sie haben Untergewicht.")
    elif 18.5 <= bmi < 25:
        print("Sie haben Normalgewicht.")
    elif 25 <= bmi < 30:
        print("Sie haben Übergewicht.")
    else:
        print("Sie haben starkes Übergewicht (Adipositas).")

# Hauptprogramm starten
if __name__ == "__main__":
    main()
