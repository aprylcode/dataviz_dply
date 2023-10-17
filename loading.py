import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd

def display():

    st.title("La consommation quotidienne française d'énergie ⚡")

    st.write("La question de la consommation d'énergie est un enjeu majeur de notre société. \n En effet, la consommation d'énergie est un indicateur de la santé économique d'un pays. \n C'est pourquoi nous avons décidé de nous intéresser à la consommation d'énergie en France. \n Nous avons donc récupéré des données sur la consommation d'énergie en France sur le site du gouvernement. \n Nous allons donc analyser ces données.")

    st.title('Loading the dataset')


    df = pd.read_csv('consommation-quotidienne-brute-regionale.csv', delimiter=";")


    st.write("On regarde à quoi ressemble notre dataset, ici les 5 premières lignes :")

    if st.checkbox('Show the first 5 lines of the dataframe'):
        st.dataframe(df.head())

    # Informations sur le dataset

    st.subheader('Informations sur le dataframe')
    st.write(f"Nombre total de lignes : {df.shape[0]}")
    st.write(f"Nombre total de colonnes : {df.shape[1]}")
    st.write(f"Liste des colonnes : {', '.join(df.columns)}")
    st.write("Types de données par colonne :")
    st.write(df.dtypes)
    st.write("On observe qu'il y a de nombreuses colonnes sous le format 'object' et cela peut nuire à notre analyse \n Nous devrons nous occuper de ces colonnes dans la partie de preprocessing.")
    st.write("Résumé statistique :")
    st.write(df.describe())