import streamlit as st 



if "Zahl" not in st.session_state:
    st.session_state['Zahl'] = 0

if st.button("Say hello"):
    st.session_state.Zahl +=1

st.write(st.session_state.Zahl)
