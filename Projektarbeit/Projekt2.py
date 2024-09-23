import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Titel und Beschreibung des Dashboards
st.title("Gebäudeautomatisierungs-Dashboard")
st.write("Steuere die Beleuchtung und Raumtemperatur in verschiedenen Räumen.")

# Definition der Räume
Wohnzimmer = "Wohnzimmer"
Küche = "Küche"
Schlafzimmer = "Schlafzimmer"
Badzimmer = "Badzimmer"
gluehbirne_an = "💡"
gluehbirne_aus = "⭕"

Heizung_an = "Der Heizkessel ist ausgeschaltet ❄️!"
Heizung_aus = "Der Heizkessel ist eingeschaltet 🔥!"

# Räume in der Sidebar auswählen
section = st.sidebar.selectbox("Meine Räume", (Wohnzimmer, Küche, Schlafzimmer, Badzimmer))

if 'Wohnzimmer_beleuchtung' not in st.session_state:
    st.session_state['Wohnzimmer_beleuchtung'] = False

if 'Küche_beleuchtung' not in st.session_state:
    st.session_state['Küche_beleuchtung'] = False

if 'Schlafzimmer_beleuchtung' not in st.session_state:
    st.session_state['Schlafzimmer_beleuchtung'] = False

if 'Badzimmer_beleuchtung' not in st.session_state:
    st.session_state['Badzimmer_beleuchtung'] = False

if 'Wohnzimmer_temperatur' not in st.session_state:
    st.session_state['Wohnzimmer_temperatur'] = 22

if 'Küche_temperatur' not in st.session_state:
    st.session_state['Küche_temperatur'] = 22

if 'Schlafzimmer_temperatur' not in st.session_state:
    st.session_state['Schlafzimmer_temperatur'] = 22

if 'Badzimmer_temperatur' not in st.session_state:
    st.session_state['Badzimmer_temperatur'] = 22

# Funktion zur Aktualisierung der Temperatur und des Diagramms
def update_temperature(room, current_temp):
    target_temp = 22
    if current_temp < target_temp:
        new_temp = current_temp + 1
        st.session_state[f'{room}_temperatur'] = new_temp
        st.session_state['temperature_data'][room].append(new_temp)

        # Plotten des Temperaturverlaufs
        plt.figure(figsize=(10, 4))
        plt.plot(st.session_state['temperature_data'][room], marker='o')
        plt.title(f'Temperaturverlauf im {room}')
        plt.xlabel('Messung')
        plt.ylabel('Temperatur (°C)')
        st.pyplot(plt)

        time.sleep(2)  # Verzögerung von 2 Sekunden einfügen
        st.experimental_rerun()  # Seite neu laden

    else:
        st.session_state['temperature_data'][room].append(current_temp)
        st.session_state[f'{room}_temperatur'] = current_temp

        # Plotten des Temperaturverlaufs
        plt.figure(figsize=(10, 4))
        plt.plot(st.session_state['temperature_data'][room], marker='o')
        plt.title(f'Temperaturverlauf im {room}')
        plt.xlabel('Messung')
        plt.ylabel('Temperatur (°C)')
        st.pyplot(plt)

# Temperatursteuerung und Beleuchtung für das Wohnzimmer
if section == Wohnzimmer:
    Licht_An = st.checkbox(f"Beleuchtung im {Wohnzimmer} einschalten", value=st.session_state.Wohnzimmer_beleuchtung)
    st.session_state.Wohnzimmer_beleuchtung = Licht_An

    if Licht_An:
        st.success(f"Beleuchtung im {Wohnzimmer} ist eingeschaltet. {gluehbirne_an}")
    else:
        st.warning(f"Beleuchtung im {Wohnzimmer} ist ausgeschaltet. {gluehbirne_aus}")

    with st.expander("Raumtemperatur einstellen"):
        current_temp = st.slider(f"Raumtemperatur im {Wohnzimmer} einstellen (°C)", min_value=16, max_value=30, value=st.session_state['Wohnzimmer_temperatur'])
        st.info(f"Raumtemperatur im {Wohnzimmer} ist auf {current_temp}°C eingestellt.")
        update_temperature(Wohnzimmer, current_temp)

        if current_temp > 22:
            st.info(Heizung_an)
        else:
            st.info(Heizung_aus)

# Raumsteuerung für andere Räume
def room_control(room):
    Licht_An = st.checkbox(f"Beleuchtung in der {room} einschalten", value=st.session_state[f'{room}_beleuchtung'])
    st.session_state[f'{room}_beleuchtung'] = Licht_An

    if Licht_An:
        st.success(f"Beleuchtung in der {room} ist eingeschaltet. {gluehbirne_an}")
    else:
        st.warning(f"Beleuchtung in der {room} ist ausgeschaltet. {gluehbirne_aus}")

    with st.expander(f"Raumtemperatur in der {room} einstellen"):
        current_temp = st.slider(f"Raumtemperatur in der {room} einstellen (°C)", min_value=16, max_value=30, value=st.session_state[f'{room}_temperatur'])
        st.info(f"Raumtemperatur in der {room} ist auf {current_temp}°C eingestellt.")
        update_temperature(room, current_temp)

        if current_temp > 22:
            st.info(Heizung_an)
        else:
            st.info(Heizung_aus)

if section == Küche:
    room_control(Küche)

if section == Schlafzimmer:
    room_control(Schlafzimmer)

if section == Badzimmer:
    room_control(Badzimmer)







    


   


# Startet das Streamlit Dashboard
# Hinweis: Diesen Befehl im Terminal ausführen, nicht im Skript
# streamlit run dashboard.py
