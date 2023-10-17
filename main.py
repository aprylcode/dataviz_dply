# main.py
import streamlit as st
import preprocessing, preprocessing_2, loading, vizualisations

st.sidebar.title("Consommation quotidienne française")

st.sidebar.image("logo.png", use_column_width=True)

st.sidebar.title("Navigation")

st.sidebar.write("Website application made by : Ahyl PRADHAN")

github_url = "https://github.com/aprylcode" 
st.sidebar.markdown(f"[View My GitHub]({github_url})")

# Définir un dictionnaire pour les pages
PAGES = {
    "Loading Dataset": loading,
    "Preprocessing 1": preprocessing,
    "Preprocessing 2": preprocessing_2,
    "Visualisations": vizualisations
}

# Utiliser un radio bouton dans la sidebar pour choisir la page
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Appeler la fonction 'display' du module sélectionné pour afficher son contenu
page = PAGES[selection]
page.display()
