import streamlit as st

# Titel und Beschreibung des Dashboards
st.title("Gebäudeautomatisierungs-Dashboard")
st.write("Steuere die Beleuchtung und Raumtemperatur in verschiedenen Räumen.")

# Definition der Räume
rooms = ["Wohnzimmer", "Küche", "Schlafzimmer", "Badezimmer"]

# Erstelle eine Spalte für jeden Raum
for room in rooms:
    st.header(room)
    # Beleuchtungssteuerung
    light_on = st.checkbox(f"Beleuchtung im {room} einschalten")
    if light_on:
        st.success(f"Beleuchtung im {room} ist eingeschaltet.")
    else:
        st.warning(f"Beleuchtung im {room} ist ausgeschaltet.")
    
    # Raumtemperatursteuerung
    temperature = st.slider(f"Raumtemperatur im {room} einstellen (°C)", min_value=16, max_value=30, value=22)
    st.info(f"Raumtemperatur im {room} ist auf {temperature}°C eingestellt.")

# Startet das Streamlit Dashboard
# Hinweis: Diesen Befehl im Terminal ausführen, nicht im Skript
# streamlit run dashboard.py