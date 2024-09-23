import streamlit as st 
from time import sleep
from random import randint
import pandas as pd 

def read_sensor():
        sleep(.02)
        return randint(1,10)
place = st.empty()
place2= st.empty()

for i in range(20):
        sensor = read_sensor()
        place.write(sensor)
data=[]
for i in range(20):
    sensor = read_sensor()
    data.append(sensor)
    place.line_chart(data)

  