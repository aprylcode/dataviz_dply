import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd


def display():

    st.title('Preprocessing the dataset Part 2')

    @st.cache_data
    def load_data():
        data = pd.read_csv("consommation-quotidienne-brute-regionale.csv", delimiter=";")
        return data

    df = load_data()

    df_cleaned_na = df.dropna()

    st.write(df_cleaned_na.isnull().sum())

    st.write("On a supprimé toutes les lignes qui contenaient des valeurs nulles donc on a que des 0 dans le tableau ci-dessus.")

    st.write(df_cleaned_na.head())

    st.write("Voici les 5 premières lignes du dataset, on remarque qu'il n'y a plus de valeur None")

    st.write("On enregistre le dataset sans les valeurs nulles :")

    code = '''df_cleaned_na.to_csv('consommation-quotidienne-brute-regionale-no_null.csv', index=False)'''
    st.code(code, language='python')

    df_cleaned_na.to_csv('consommation-quotidienne-brute-regionale-no_null.csv', index=False)

    st.write("On va regarder toutes les valeurs différentes dans les colonnes qui ne sont pas numériques :")

    for column in ['statut_grtgaz', 'statut_terega', 'statut_rte']:
        st.write(f"Valeurs uniques pour {column}:")
        st.write(df_cleaned_na[column].unique())
        st.write("\n")

    st.write("On a des valeurs qui ne sont pas des valeurs numériques, on va donc les transformer en valeurs numériques :")

    code = '''for column in ['statut_grtgaz', 'statut_terega', 'statut_rte']:
        df_cleaned_na[column], unique_encoder = pd.factorize(df_cleaned_na[column])
        label_encoders[column] = unique_encoder'''
    st.code(code, language='python')


    # Remplacement des valeurs non numériques par des valeurs numériques

    label_encoders = {}


    for column in ['statut_grtgaz', 'statut_terega', 'statut_rte']:
        df_cleaned_na[column], unique_encoder = pd.factorize(df_cleaned_na[column])
        label_encoders[column] = unique_encoder


    st.write("Pour statut_grtgaz : Définitif -> 0, Meilleur Statut -> 1")
    st.write("Pour statut_terega : Définitif -> 0")
    st.write("Pour statut_rte : Définitif -> 0, Consolidé -> 1")

    st.write(df_cleaned_na.head())


    st.write("On enregistre le dataset 'final' avec uniquement des valeurs numériques")

    code = '''df_cleaned_na.to_csv('consommation-quotidienne-brute-regionale-final.csv', index=False)'''
    st.code(code, language='python')

    df_cleaned_na.to_csv('consommation-quotidienne-brute-regionale-final.csv', index=False)