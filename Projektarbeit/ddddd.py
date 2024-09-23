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

Heizung_an = " Der Heizkessel ist ausgeschaltet ❄️!"
Heizung_aus = "Der Heizkessel ist eingeschaltet 🔥!"

# Räume in der Sidebar auswählen
section = st.sidebar.selectbox("Meine Räume", (Wohnzimmer, Küche, Schlafzimmer, Badzimmer))

# Initialisierung der Session State Variablen
if 'temperature_data' not in st.session_state:
    st.session_state['temperature_data'] = {Wohnzimmer: [22.5], Küche: [22.5], Schlafzimmer: [22.5], Badzimmer: [22.5]}

if 'Wohnzimmer_beleuchtung' not in st.session_state:
    st.session_state['Wohnzimmer_beleuchtung'] = False

if 'Küche_beleuchtung' not in st.session_state:
    st.session_state['Küche_beleuchtung'] = False

if 'Schlafzimmer_beleuchtung' not in st.session_state:
    st.session_state['Schlafzimmer_beleuchtung'] = False

if 'Badzimmer_beleuchtung' not in st.session_state:
    st.session_state['Badzimmer_beleuchtung'] = False

# Funktion zur Aktualisierung der Temperatur und des Diagramms
def update_temperature(room, temperature):
    st.session_state['temperature_data'][room].append(temperature)
    st.session_state[f'{room}_temperatur'] = temperature

    # Plotten des Temperaturverlaufs
    plt.figure(figsize=(10, 4))
    plt.plot(st.session_state['temperature_data'][room], marker='o')
    plt.title(f'Temperaturverlauf im {room}')
    plt.xlabel('Messung')
    plt.ylabel('Temperatur (°C)')
    st.pyplot(plt)

# Funktion zur automatischen Erhöhung der Temperatur
def auto_increase_temperature(room):
    while st.session_state['temperature_data'][room][-1] < 22:
        new_temp = st.session_state['temperature_data'][room][-1] + 1
        update_temperature(room, new_temp)
        time.sleep(1)

# Temperatursteuerung und Beleuchtung für das Wohnzimmer
if section == Wohnzimmer:
    Licht_An = st.checkbox(f"Beleuchtung im {Wohnzimmer} einschalten", value=st.session_state.Wohnzimmer_beleuchtung)
    st.session_state.Wohnzimmer_beleuchtung = Licht_An

    if Licht_An:
        st.success(f"Beleuchtung im {Wohnzimmer} ist eingeschaltet. {gluehbirne_an}")
    else:
        st.warning(f"Beleuchtung im {Wohnzimmer} ist ausgeschaltet. {gluehbirne_aus}")

    with st.expander("Raumtemperatur einstellen"):
        temperature = st.slider(f"Raumtemperatur im {Wohnzimmer} einstellen (°C)", min_value=16, max_value=30, value=st.session_state['temperature_data'][Wohnzimmer][-1])
        st.info(f"Raumtemperatur im {Wohnzimmer} ist auf {temperature}°C eingestellt.")
        update_temperature(Wohnzimmer, temperature)

        if temperature > 22:
            st.info(Heizung_an)
        else:
            st.info(Heizung_aus)

        if temperature < 22:
            if st.button("Temperatur automatisch auf 22°C erhöhen"):
                auto_increase_temperature(Wohnzimmer)

# Raumsteuerung für andere Räume
def room_control(room):
    Licht_An = st.checkbox(f"Beleuchtung in der {room} einschalten", value=st.session_state[f'{room}_beleuchtung'])
    st.session_state[f'{room}_beleuchtung'] = Licht_An

    if Licht_An:
        st.success(f"Beleuchtung in der {room} ist eingeschaltet. {gluehbirne_an}")
    else:
        st.warning(f"Beleuchtung in der {room} ist ausgeschaltet. {gluehbirne_aus}")

    with st.expander(f"Raumtemperatur in der {room} einstellen"):
        temperature = st.slider(f"Raumtemperatur in der {room} einstellen (°C)", min_value=16, max_value=30, value=st.session_state['temperature_data'][room][-1])
        st.info(f"Raumtemperatur in der {room} ist auf {temperature}°C eingestellt.")
        update_temperature(room, temperature)

        if temperature > 22:
            st.info(Heizung_an)
        else:
            st.info(Heizung_aus)

        if temperature < 22:
            if st.button(f"Temperatur in der {room} automatisch auf 22°C erhöhen"):
                auto_increase_temperature(room)

if section == Küche:
    room_control(Küche)

if section == Schlafzimmer:
    room_control(Schlafzimmer)

if section == Badzimmer:
    room_control(Badzimmer)







