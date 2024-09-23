import streamlit as st           #zum streamlit starten           

# Titel und Beschreibung des kontrollpanel
st.title("Gebäudeautomatisierungs-Kontrollpanel")
st.write("Steuere die Beleuchtung und Raumtemperatur in verschiedenen Räumen.")



# Definition der Räume
Wohnzimmer = "Wohnzimmer"
Küche=        "Küche"
Schlafzimmer=  "Schlafzimmer"
Badzimmer=     "Badzimmer"
gluehbirne_an = "💡"
gluehbirne_aus = "⭕"

Heizung_aus= " Der Heizkessel ist ausgeschaltet ❄️!"
Heizung_an= "Der Heizkessel ist eingeschaltet 🔥!"
Lüftung_an=" Die Klimmaanlage ist eingeschaltet! "
Abluft_an = " Der Ventilator ist eingeschaltet !"
Abluft_aus= "Der Ventilator ist ausgeschaltet ! "


section=st.sidebar.selectbox("Meine Räume", ("Wohnzimmer", "Küche", "Schlafzimmer", "Badzimmer")) # Auf der linke Seite die Räume definiert und mit Selectbox die Boxen deklariert.

if 'Küche_temperatur' not in st.session_state:    # Die werte zuerst definiert in session state das heisst wenn ich die Seite 1 mall starte passiert das!
    st.session_state['Küche_temperatur'] = 22     # und das für jeden Raum 

if 'Schlafzimmer_temperatur' not in st.session_state:
    st.session_state['Schlafzimmer_temperatur'] = 22

if 'Wohnzimmer_temperatur' not in st.session_state:
    st.session_state['Wohnzimmer_temperatur'] = 22

if 'Badzimmer_temperatur' not in st.session_state:
    st.session_state['Badzimmer_temperatur'] = 22



if 'Wohnzimmer_beleuchtung' not in st.session_state:
    st.session_state['Wohnzimmer_beleuchtung'] = False

if 'Küche_beleuchtung' not in st.session_state:
    st.session_state['Küche_beleuchtung'] = False

if 'Schlafzimmer_beleuchtung' not in st.session_state:
    st.session_state['Schlafzimmer_beleuchtung'] = False

if 'Badzimmer_beleuchtung' not in st.session_state:
    st.session_state['Badzimmer_beleuchtung'] = False


      

if section == "Wohnzimmer":
    
    #Beleuchtungsteuerung
    Licht_An = st.checkbox(f"Beleuchtung im {Wohnzimmer} einschalten", value=st.session_state.Wohnzimmer_beleuchtung) # beleuchtung mit emogie und wert 
    st.session_state.Wohnzimmer_beleuchtung=Licht_An # den wert in session state gespeichert damit es nicht verloren geht
    if Licht_An:
        st.success(f"Beleuchtung im {Wohnzimmer} ist eingeschaltet. {gluehbirne_an}") #mit Text was passiert
        
    else:
        st.warning(f"Beleuchtung im {Wohnzimmer} ist ausgeschaltet. {gluehbirne_aus}")
        
    # Raumtemperatursteuerung
    with st.expander("Raumtemperatur einstellen"):
        temperature = st.slider(f"Raumtemperatur im {Wohnzimmer} einstellen (°C)", min_value=16, max_value=30, value=st.session_state.Wohnzimmer_temperatur) # Definiert einen min und max range
        st.info(f"Raumtemperatur im {Wohnzimmer} ist auf {temperature}°C eingestellt.")
        st.session_state.Wohnzimmer_temperatur=temperature
        if temperature > 22:
            (Heizung_aus,
            Lüftung_an)
        elif temperature < 22.9:
            (Heizung_an)
        
if section == "Küche":
        
    #Beleuchtungsteuerung
        Licht_An = st.checkbox(f"Beleuchtung im {Küche} einschalten", value=st.session_state.Küche_beleuchtung,)
        st.session_state.Küche_beleuchtung=Licht_An
        if Licht_An:
            st.success(f"Beleuchtung im {Küche} ist eingeschaltet. {gluehbirne_an}, {Abluft_an}")
        else:
         st.warning(f"Beleuchtung im {Küche} ist ausgeschaltet. {gluehbirne_aus}")
    
    # Raumtemperatursteuerung
        color1=["#fd0", "#f0f"] 
        with st.expander("Raumtemperatur einstellen"):
            temperature = st.slider (f"Raumtemperatur im {Küche} einstellen (°C)", min_value=16, max_value=30, value=st.session_state.Küche_temperatur)
            st.info(f"Raumtemperatur im {Küche} ist auf {temperature}°C eingestellt.")
            st.session_state.Küche_temperatur=temperature
            if temperature > 21.9 :
                (Heizung_an)
            elif temperature < 22.9:
                (Heizung_aus)


if section == "Schlafzimmer":
        
    #Beleuchtungsteuerung
        Licht_An = st.checkbox(f"Beleuchtung im {Schlafzimmer} einschalten", value=st.session_state.Schlafzimmer_beleuchtung)
        st.session_state.Schlafzimmer_beleuchtung=Licht_An
        if Licht_An:
            st.success(f"Beleuchtung im {Schlafzimmer} ist eingeschaltet. {gluehbirne_an}")
        else:
         st.warning(f"Beleuchtung im {Schlafzimmer} ist ausgeschaltet. {gluehbirne_aus}")
    
    # Raumtemperatursteuerung
        with st.expander("Raumtemperatur einstellen"):
            temperature = st.slider(f"Raumtemperatur im {Schlafzimmer} einstellen (°C)", min_value=16, max_value=30, value=st.session_state.Schlafzimmer_temperatur)
            st.info(f"Raumtemperatur im {Schlafzimmer} ist auf {temperature}°C eingestellt.")
            st.session_state.Schlafzimmer_temperatur=temperature
        if temperature > 22:
            (Heizung_aus,
            Lüftung_an)
        elif temperature < 22.9:
            (Heizung_an)
    


if section == "Badzimmer":
        
    #Beleuchtungsteuerung
        Licht_An = st.checkbox(f"Beleuchtung im {Badzimmer} einschalten ", value=st.session_state.Badzimmer_beleuchtung)
        st.session_state.Badzimmer_beleuchtung=Licht_An
        if Licht_An:
            st.success(f"Beleuchtung im {Badzimmer} ist eingeschaltet. {gluehbirne_an}, {Abluft_aus} ")
        else:
         st.warning(f"Beleuchtung im {Badzimmer} ist ausgeschaltet. {gluehbirne_aus}")
    
    # Raumtemperatursteuerung
        with st.expander("Raumtemperatur einstellen"):
            temperature = st.slider(f"Raumtemperatur im {Badzimmer} einstellen (°C)", min_value=16, max_value=30, value=st.session_state.Badzimmer_temperatur)
            st.info(f"Raumtemperatur im {Badzimmer} ist auf {temperature}°C eingestellt.")
            st.session_state.Badzimmer_temperatur=temperature
            if temperature > 21.9 :
                (Heizung_an)
            elif temperature < 22.9:
                (Heizung_aus)



