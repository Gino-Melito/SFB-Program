import streamlit as st 
import pandas as pd 
import time
from time import sleep
from random import randint

section=st.sidebar.radio("my Sidbare", ("Seite 1", "Seite 2", "Seite 3", "Seite 4","Seite 5", "Seite 6" )) 


if section == "Seite 1":
    Klassenliste = {          # zum eine lista machen 
  "Gino": "Melito",
  "Adnan": "Tükmen"
    }
    Klasse= pd.DataFrame(Klassenliste.items(),
                    columns=["Vorname" ,"Nachname"]
    )
    st.table(Klasse)


# neue seite 2


if section  == "Seite 2":
    st.write(st.slider("Whitch quarter?", 1,4,(2)))
    values= st.slider("please select a range of values!", 0.0 , 100.0, (0.0, 20.0))

# neue seite 3 

# Erstelle eine Liste mit 10 Zahlenwerten
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

if section == "Seite 3":
    st.write(numbers) # Stelle die Zahlenwerte auf der Seite dar
    df = pd.DataFrame(numbers, columns=["Werte"]) # Erstelle ein DataFrame für das Chart
    st.line_chart(df) # Erstelle ein Liniendiagramm


# seite 4 

# Initialization



if section == "Seite 4":

    if"count" not in st.session_state:
        st.session_state["count"] = 0

    if st.button(label="counter"):
        st.session_state.count +=1

        st.write(st.session_state.count)

#Seite 5 

if section == "Seite 5":
     
    classmates = ["Adnan", "Gino", "Sphend", "Riccardo", "Luis", "Cyriel"]
    placeholder = st.empty()

    for name in classmates:
        placeholder.text(f"Name: {name}")

        time.sleep(2)

#Seite 6 

if section == "Seite 6":

    container = st.container()
    container.write("THIS IS AH CONTAINER")
    st.write("this is outside the container")

    container.write("this is inside too")

    