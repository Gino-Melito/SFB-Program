# das ist ein Programm wo viele Funktionen stehen und erklärt wirt was sie machen zum visualisieren. um den program zu starten muss man
# in der konsole schreiben (streamlit run Dokumentname.py)
import streamlit as st # das muss man schrieben damit man etwas visualiesiren kann 
import pandas as pd    # das muss man machen damit man andere feetcure machen kann 




st.header("my Header") # zum ein grossen titel machen
st.subheader("my Subheader") # zum ein untertitel herstellen
st.write("test2")

thisdict = {          # zum eine lista machen 
  "brand": "Ford",
  "model": "Mustang"
}


mylist= ("name,name2,name3")

st.write(thisdict)

st.write ("my text")
st.write(mylist)

#Q2 

st.title ("sales Report")

st.header ("Q1 Result")

q1_sales= {                 # hier haben wir eine Liste deklariert
    "januar" : 100,         #q1 ist einfach eine variabel wir können alles für q1_sales und q1_sales nehmen!!
    "February" :100,
    "March" : 115,
}

st.write("January was the start of the year")   
st.write(q1_sales)
st.header("Q2 Resaults")
q2_sales= {"April" : 150,  # hier haben wir die zweite liste deklariert
           "May" :200,
           "June" :250,
}

"Q2 had better results :smile:"  # hier schreiben wir ein text mit ein emogie

q2_df= pd.DataFrame(q2_sales.items(),
                    columns=["Month" ,"Amount"]
                    )


q1_df= pd.DataFrame(q1_sales.items(),
                    columns=["Month" ,"Amount"]
                    )
                    
                    
st.table(q2_df)

st.dataframe(q2_df)

q2_df2=q2_df.astype(str)

color=["#fd0", "#f0f"] #damit man die farben wechsel kann 

st.line_chart(data=q2_df2, color=color) # wir wechseln hier die farben vom diagramm 

st.area_chart(data=q2_df2)

st.bar_chart([q1_sales.values(), q2_sales.values()])


st.button(label="My Button") #damit man ein knopf machen kann 

q2_df2=q2_df.astype(str)
q1_df2=q1_df.astype(str)

if st.button("Show Q2 Data"): #damit man ein knopf machen kann 
    st.table(q2_df)          #Auf Webseite kann man sehen das Q2 steht
else:                        # Hier kann man von zwei diagrammen wechseln
    st.table(q1_df)


if st.checkbox("Show Q2 Data"): # Damit man ein viereck herstellt wo man drauf klicken kann 
    st.line_chart(q2_df2)       # Hier kann man von zwei diagrammen wechseln
else:
    st.line_chart(q1_df2)
quarter=st.radio("whitch quarter?", ("Q1", "Q2")) # Damit man den Q1 oder Q2 ausfählen kann!

if quarter=="Q1" :
    st.line_chart(q1_df2)
elif quarter== "Q2":
    st.line_chart(q1_df2)

select_quarter=st.selectbox("whitch quarter?", ("Q1", "Q2"))

if select_quarter == "Q1" :
    st.line_chart(q1_df2)
elif select_quarter == "Q2" :
    st.line_chart(q2_df2)

st.write(st.slider("Whitch quarter?", 1,4,(2)))  # hier kann man eine range herstellen von wo bis wo ist gut für ein Temperatur fühler
values= st.slider("please select a range of values!", 0.0 , 100.0, (40.0, 80.0))
st.write(values)
st.write(st.multiselect("Choose Quarter", ["Q1", "Q2", "Q3", "Q4"])) # Hier kann man den gewünschten ergebnis zeigen lassen
st.write(st.number_input("Whitch Quarter", 1, 40))

section=st.sidebar.radio("my Sidbare", ("Seite 1", "Seite 2", "Seite 3", "Seite 4" ))   # mann kann die seiten wechseln und andere sachen auswählen. 

if section == "Selection1":      
  st.write("My Slection")
elif section ==("Selection2"):
    st.line_chart(q2_df2)

  