import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd
import plotly.express as px




def display():

    st.title('Preprocessing the dataset')


    @st.cache_data
    def load_data():
        data = pd.read_csv("consommation-quotidienne-brute-regionale.csv", delimiter=";")
        return data

    df = load_data()

    st.dataframe(df.head())

    st.write("On regarde s'il y a des valeurs nulles dans notre dataset")

    st.subheader("Types de données par colonne :")
    st.write(df.dtypes)

    st.subheader('Nombre de valeurs nulles par colonne')

    code = '''null_counts = df.isnull().sum()
    st.write(null_counts)'''
    st.code(code, language='python')

    null_counts = df.isnull().sum()
    st.write(null_counts)

    st.write('On va changer le type des colonnes data_heure et date :')

    code = '''df['date_heure'] = pd.to_datetime(df['date_heure'], utc=True)
    df['date'] = pd.to_datetime(df['date'])
    df['heure'] = pd.to_datetime(df['heure'], format='%H:%M')'''
    st.code(code, language='python')


    df['date_heure'] = pd.to_datetime(df['date_heure'], utc=True)
    df['date'] = pd.to_datetime(df['date'])
    df['heure'] = pd.to_datetime(df['heure'], format='%H:%M')

    st.write(df.dtypes)

    st.write('On reregarde notre dataset avec les colonnes changées :')

    st.dataframe(df.head())

    st.write('On doit changer la colonne heure pour ne garder que l\'heure et non la date et l\'heure :')

    code = '''df['heure'] = df['heure'].dt.strftime('%H:%M')'''
    st.code(code, language='python')

    df['heure'] = df['heure'].dt.strftime('%H:%M')

    st.dataframe(df.head())

    st.write('On va maintenant changer le type des colonnes de type object car on remarque qu\' il y a beaucoup de colonnes de ce type')

    st.write('On remarque que pour les régions, on a déjà les valeurs INSEE, on va donc supprimer la colonne region')

    st.code('df.drop(columns=["region"], inplace=True)', language='python')

    df.drop(columns=["region"], inplace=True)

    st.write("On sauvegarde notre nouveau dataset dans un fichier csv")

    code = '''df.to_csv('consommation-quotidienne-brute-regionale-preprocessed.csv', index=False)
    df = pd.read_csv('consommation-quotidienne-brute-regionale-preprocessed.csv')'''
    st.code(code, language='python')

    df.to_csv('consommation-quotidienne-brute-regionale-preprocessed.csv', index=False)

    df = pd.read_csv('consommation-quotidienne-brute-regionale-preprocessed.csv')


    st.dataframe(df.head())

    st.write(df.isnull().sum())
    st.write(df.shape)

    df_cleaned_na = df.dropna()

    st.write(df_cleaned_na.isnull().sum())

    st.write(df_cleaned_na.shape)

    st.write(df_cleaned_na.head()) 
