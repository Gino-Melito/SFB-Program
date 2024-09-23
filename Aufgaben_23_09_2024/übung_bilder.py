import streamlit as st

Bild1,Bild2,Bild3=st.columns(3) #damit alle bilder nebeneinander stehen


with Bild1:
    st.image('C:/Users/spit-/OneDrive/Desktop/SFB Dokumente/2. Semester/Grundlagen Programmierung 1/SFB Program/Aufgaben_23_09_2024/Einhorn.jpg')
    # wir müssen so die bilder auswàhlen zuerst den pfad und danach der name von dem Bild
with Bild2:  
    st.image('C:/Users/spit-/OneDrive/Desktop/SFB Dokumente/2. Semester/Grundlagen Programmierung 1/SFB Program/Aufgaben_23_09_2024/Download.jpeg')

with Bild3:
    st.image('C:/Users/spit-/OneDrive/Desktop/SFB Dokumente/2. Semester/Grundlagen Programmierung 1/SFB Program/Aufgaben_23_09_2024/getimgai-ki-bilder.jpg')

