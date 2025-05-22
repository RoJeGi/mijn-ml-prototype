
import streamlit as st
from pypmml import Model
import pandas as pd

# Laad het PMML-model
model = Model.load('model.pmml')

st.title('Voorspellingsapp – RapidMiner PMML')

# Gebruikersinvoer
bestellen = st.number_input("Aantal bestellingen", step=1)
week_verschil = st.number_input("Week verschil", step=1)

# Als gebruiker op 'Voorspel' klikt
if st.button("Voorspel"):
    # Maak DataFrame van invoer
    invoer = pd.DataFrame([{
        "Bestellen": bestellen,
        "Week_verschil": week_verschil
    }])

    # Voorspelling uitvoeren
    resultaat = model.predict(invoer)

    st.subheader("Voorspelling:")
    st.write(resultaat)
