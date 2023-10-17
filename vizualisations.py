import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns


def display():


    st.title('Visualisations')

    st.write("On fait des visualisations sur notre dataset afin de comprendre plus en détail les données et faire des interprétations pertinentes :")

    @st.cache_data
    # Charger les données
    def load_data():
        data = pd.read_csv("consommation-quotidienne-brute-regionale-final.csv")
        data['date_heure'] = pd.to_datetime(data['date_heure'])
        return data

    data = load_data()

    st.write(data.head())


    st.write("On va donc commencer notre analyse visuelle, on va afficher de nombreux graphiques et les expliquer :")

    ############################################################################################################

    with st.expander("Explications pour la consommation totale pour la région"):
        st.title('Évolution de la consommation au fil du temps')

        st.code('''time_series_data = data.groupby('date_heure').sum()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=time_series_data, ax=ax)
        ax.set_title('Évolution de la consommation au fil du temps')
        ax.set_ylabel('Consommation')
        ax.set_xlabel('Date')
        ax.legend(title='Type de consommation', labels=['Consommation Gaz Totale', 'Consommation Électricité', 'Consommation Totale'])
        st.pyplot(fig)''', language='python')

        time_series_data = data.groupby('date_heure').sum()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=time_series_data, ax=ax)
        ax.set_title('Évolution de la consommation au fil du temps')
        ax.set_ylabel('Consommation')
        ax.set_xlabel('Date')
        ax.legend(title='Type de consommation', labels=['Consommation Gaz Totale', 'Consommation Électricité', 'Consommation Totale'])
        st.pyplot(fig)

        st.write("Avec ce graphique on peut observer la consommation des 3 différentes régions qu'il reste dans notre dataset.\nIl faut noter qu'il y a un pic de consommation en 2017 et 2018. \n De plus, on remarque que le COVID-19 n'a pas beaucoup impacté notre consommation même si elle est plus elevée que la moyenne.")

    ############################################################################################################

    with st.expander("Visualisation de la répartition de la consommation par région"):

        st.title('Répartition de la consommation par région')

        st.code('''region_data = data.groupby('code_insee_region').sum()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        region_data.plot(kind='bar', stacked=True, ax=ax)
        ax.set_title('Répartition de la consommation par région')
        ax.set_ylabel('Consommation')
        ax.set_xlabel('Code INSEE Région')
        ax.legend(title='Type de consommation', labels=['Consommation Gaz Totale', 'Consommation Électricité', 'Consommation Totale'])
        st.pyplot(fig)''', language='python')

        region_data = data.groupby('code_insee_region').sum()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        region_data.plot(kind='bar', stacked=True, ax=ax)
        ax.set_title('Répartition de la consommation par région')
        ax.set_ylabel('Consommation')
        ax.set_xlabel('Code INSEE Région')
        ax.legend(title='Type de consommation', labels=['Consommation Gaz Totale', 'Consommation Électricité', 'Consommation Totale'])
        st.pyplot(fig)

        st.write("Avec ce graphique on observe la consommation de chaque région qu'il reste dans notre dataset c'est-à-dire 75, 76 et 84. \n On remarque que la région 84 a une consommation plus élevée que les autres régions. \n De plus, on remarque que la consommation d'électricité est plus élevée que la consommation de gaz. \n On découvre ainsi que la région 84 est une région qui consomme beaucoup.")

    ############################################################################################################

    with st.expander("Visualisation des statistiques de statut"):

        st.title('Statistiques de statut')

        status_counts_grtgaz = data['statut_grtgaz'].value_counts()
        status_counts_terega = data['statut_terega'].value_counts()
        status_counts_rte = data['statut_rte'].value_counts()

        fig, axes = plt.subplots(3, 1, figsize=(14, 15))

        # GRTgaz status
        status_counts_grtgaz.plot(kind='bar', ax=axes[0], color='blue')
        axes[0].set_title('Statut pour GRTgaz')
        axes[0].set_ylabel('Nombre d\'occurrences')
        axes[0].set_xlabel('Statut')

        # Teréga status
        status_counts_terega.plot(kind='bar', ax=axes[1], color='green')
        axes[1].set_title('Statut pour Teréga')
        axes[1].set_ylabel('Nombre d\'occurrences')
        axes[1].set_xlabel('Statut')

        # RTE status
        status_counts_rte.plot(kind='bar', ax=axes[2], color='red')
        axes[2].set_title('Statut pour RTE')
        axes[2].set_ylabel('Nombre d\'occurrences')
        axes[2].set_xlabel('Statut')

        st.pyplot(fig)

        st.write("Pour statut_grtgaz : Définitif -> 0, Meilleur Statut -> 1")
        st.write("Pour statut_terega : Définitif -> 0")
        st.write("Pour statut_rte : Définitif -> 0, Consolidé -> 1")
        st.write("Ce graphique est assez falcultatif, il nous permet de comprendre un peu plus en détail les statuts de données des fournisseurs de gaz dans notre dataset.")

    ############################################################################################################

    with st.expander("Visualisation de la distribution de la consommation totale"):

        st.code('''fig, ax = plt.subplots(figsize=(14,7))
        sns.histplot(data['consommation_brute_totale'], bins=70, kde=True, color='lime', ax=ax)
        ax.set_title('Distribution de la consommation totale')
        ax.set_ylabel('Nombre d\'observations')
        ax.set_xlabel('Consommation totale')
        st.pyplot(fig)''', language='python')

        
        st.title('Distribution de la consommation totale')

        fig, ax = plt.subplots(figsize=(14,7))
        sns.histplot(data['consommation_brute_totale'], bins=70, kde=True, color='lime', ax=ax)
        ax.set_title('Distribution de la consommation totale')
        ax.set_ylabel('Nombre d\'observations')
        ax.set_xlabel('Consommation totale')
        st.pyplot(fig)

        st.write("Ce graphique nous permet de voir la distribution de la consommation dans notre dataset \n Cela nous permet de voir que la consommation brute moyenne est entre 4000 et 7000")

    ############################################################################################################

    with st.expander("Visualisation de la distribution de la consommation par région"):

        st.title('Boxplot de la consommation par région')

        st.code('''fig, ax = plt.subplots(figsize=(14,7))
        sns.boxplot(x='code_insee_region', y='consommation_brute_totale', data=data, palette='viridis', ax=ax)
        ax.set_title('Boxplot de la consommation par région')
        ax.set_ylabel('Consommation totale')
        ax.set_xlabel('Code INSEE Région')
        st.pyplot(fig)

        regions = data['code_insee_region'].unique()
        statistics = {}
        for region in regions:
            region_data = data[data['code_insee_region'] == region]['consommation_brute_totale']
            Q1 = region_data.quantile(0.25)
            Q3 = region_data.quantile(0.75)
            median = region_data.median()
            statistics[region] = {"Q1": Q1, "Q3": Q3, "Mediane": median}

        st.write("Statistiques des boxplots :")
        for region, stats in statistics.items():
            st.write(f"Région {region}: Q1 = {stats['Q1']:.2f}, Médiane = {stats['Mediane']:.2f}, Q3 = {stats['Q3']:.2f}")''', language='python')   

        fig, ax = plt.subplots(figsize=(14,7))
        sns.boxplot(x='code_insee_region', y='consommation_brute_totale', data=data, palette='viridis', ax=ax)
        ax.set_title('Boxplot de la consommation par région')
        ax.set_ylabel('Consommation totale')
        ax.set_xlabel('Code INSEE Région')
        st.pyplot(fig)

        regions = data['code_insee_region'].unique()
        statistics = {}
        for region in regions:
            region_data = data[data['code_insee_region'] == region]['consommation_brute_totale']
            Q1 = region_data.quantile(0.25)
            Q3 = region_data.quantile(0.75)
            median = region_data.median()
            statistics[region] = {"Q1": Q1, "Q3": Q3, "Mediane": median}

        st.write("Statistiques des boxplots :")
        for region, stats in statistics.items():
            st.write(f"Région {region}: Q1 = {stats['Q1']:.2f}, Médiane = {stats['Mediane']:.2f}, Q3 = {stats['Q3']:.2f}")

        st.write("Avec ces boxplots et l'affichage des quartiles et de la médiane on peut comprendre en détail la consommation de chaque région de notre dataset. \n Par exemple la région 76 à la médianne la plus faible donc on peut en déduire que c'est la région qui consomme le moins. \n Au contraire pour la région 84, on a encore une confirmation que c'est la région qui consomme le plus. \n Un autre point important à noter : les outliers. On remarque que les outliers sont très élevés dans la région 84. \n On ne les a pas nettoyés car ici on ne fait pas d'analyse de Machine Learning mais si on en faisait, il faudrait les nettoyer.")

    ############################################################################################################

    with st.expander("Visualisation de la consommation par heure"):

        st.title('Consommation moyenne par heure')

        st.code('''hourly_data = data.groupby('heure').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=hourly_data, ax=ax)
        ax.set_title('Consommation moyenne par heure')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Heure')
        st.pyplot(fig)''', language='python')

        hourly_data = data.groupby('heure').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=hourly_data, ax=ax)
        ax.set_title('Consommation moyenne par heure')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Heure')
        st.pyplot(fig)

        st.write("Ce graphique nous permet de voir que la consommation a une corrélation avec le temps. En effet, on voit qu'il y a un pic entre 6h et 8h ce qui est normal car c'est le moment où les gens se lèvent pour aller travailler. \n On voit aussi un pic entre 18h et 20h ce qui est aussi normal car c'est le moment où les gens rentrent du travail.")

    ############################################################################################################

    with st.expander("Visualisation de la consommation  par jour"):

        st.title('Consommation moyenne par jour de la semaine')

        st.code('''data['jour_semaine'] = data['date_heure'].dt.day_name()

        order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        weekday_data = data.groupby('jour_semaine').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]

        weekday_data = weekday_data.reindex(order_days)

        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=weekday_data, ax=ax)
        ax.set_title('Consommation moyenne par jour de la semaine')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Jour de la semaine')
        st.pyplot(fig)''', language='python')

        data['date_heure'] = pd.to_datetime(data['date_heure'], utc=True)
        data['jour_semaine'] = data['date_heure'].dt.day_name()

        order_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        weekday_data = data.groupby('jour_semaine').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]

        weekday_data = weekday_data.reindex(order_days)

        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=weekday_data, ax=ax)
        ax.set_title('Consommation moyenne par jour de la semaine')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Jour de la semaine')
        st.pyplot(fig)

        st.write("On remarque une baisse de consommation le week-end ce qui est normal car les gens consomment moins en fin de semaine.")


    ############################################################################################################

    with st.expander("Visualisation de la consommation par mois"):

        st.title('Consommation moyenne par mois')

        st.code('''data['mois'] = data['date_heure'].dt.month_name()

        ordered_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        month_data = data.groupby('mois').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        month_data = month_data.reindex(ordered_months)

        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=month_data, ax=ax)
        ax.set_title('Consommation moyenne par mois')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Mois')
        st.pyplot(fig)''', language='python')

        data['mois'] = data['date_heure'].dt.month_name()

        ordered_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        month_data = data.groupby('mois').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        month_data = month_data.reindex(ordered_months)

        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=month_data, ax=ax)
        ax.set_title('Consommation moyenne par mois')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Mois')
        st.pyplot(fig)

        st.write("Avec ce graphique on peut voir que la consommation est plus élevée en hiver qu'en été. \n Cela est normal car en hiver les gens consomment plus de chauffage. En été, les gens consomment moins de chauffage et moins de lumière car il fait jour plus longtemps. \n De plus, la climatisation est peu répandue ce qui explique également la 'faible' consomation en été.")

    ############################################################################################################

    with st.expander("Visualisation de la consommation par mois avec plotly"):
        st.title('Consommation moyenne par mois')

        st.code('''
        data['mois'] = data['date_heure'].dt.month_name()
        ordered_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month_data = data.groupby('mois').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        month_data = month_data.reindex(ordered_months)
        ''', language='python')

        data['mois'] = data['date_heure'].dt.month_name()
        ordered_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        month_data = data.groupby('mois').mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        month_data = month_data.reindex(ordered_months)

        fig = px.line(month_data, x=month_data.index, y=month_data.columns, title='Consommation moyenne par mois', labels={'value': 'Consommation Moyenne', 'mois': 'Mois', 'variable': 'Type de consommation'})
        fig.update_layout(yaxis_title="Consommation Moyenne", xaxis_title="Mois")
        
        st.plotly_chart(fig)



    ############################################################################################################

    with st.expander("Visualisation de la consommation par année"):

        st.title('Consommation moyenne par année')

        st.code('''year_data = data.groupby(data['date_heure'].dt.year).mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=year_data, ax=ax)
        ax.set_title('Consommation moyenne par année')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Année')
        st.pyplot(fig)''', language='python')
        
        year_data = data.groupby(data['date_heure'].dt.year).mean()[['consommation_brute_gaz_totale', 'consommation_brute_electricite_rte', 'consommation_brute_totale']]
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=year_data, ax=ax)
        ax.set_title('Consommation moyenne par année')
        ax.set_ylabel('Consommation Moyenne')
        ax.set_xlabel('Année')
        st.pyplot(fig)

        st.write("Ce graphique permet de voir les commations selon les années, on peut voir que le confinement à fait baisser les consommations en 2020. \n On peut aussi voir que la consommation reste stable au fil des années.")

    ############################################################################################################


    with st.expander("Visualisation de la consommation totale par région avec un pie chart plotly"):
        pie_data = data.groupby('code_insee_region').sum()['consommation_brute_totale']
        
        st.title('Répartition de la consommation totale par région')

        fig = px.pie(pie_data, values='consommation_brute_totale', names=pie_data.index, title='Répartition de la consommation totale par région', color_discrete_sequence=px.colors.sequential.Plasma)
        
        st.plotly_chart(fig)

        st.write("Ce graphique nous permet de voir la répartition de la consommation totale par région avec un pie chart. Cela confirme que le région 84 est la région")


    ############################################################################################################


    with st.expander("Visualisation de la consommation totale avec une side bar plotly"):
    
        selected_date = st.sidebar.date_input('Sélectionnez une date', data['date_heure'].dt.date.iloc[0])
        regions = data['code_insee_region'].unique()
        selected_region = st.sidebar.selectbox('Sélectionnez une région', regions)
        
        filtered_data = data[(data['date_heure'].dt.date == selected_date) & (data['code_insee_region'] == selected_region)]
        
        st.title(f'Consommation totale pour la région {selected_region} le {selected_date}')
        
        fig = px.bar(filtered_data, x='heure', y='consommation_brute_totale', title=f'Consommation totale pour la région {selected_region} le {selected_date}', labels={'consommation_brute_totale': 'Consommation Totale', 'heure': 'Heure'}, color_discrete_sequence=['skyblue'])
        
        st.plotly_chart(fig)

        st.write("Ce graphique permet de choisir une date et une région et de voir la consommation par heure sous la forme d'un bar chart.")

    ############################################################################################################

    with st.expander("Visualisation de la consommation totale avec un line chart"):

        selected_date_hourly = st.sidebar.date_input("Sélectionnez une date pour l'analyse horaire", data['date_heure'].dt.date.iloc[0])
        filtered_data_hourly = data[data['date_heure'].dt.date == selected_date_hourly]
        st.title(f'Consommation par heure le {selected_date_hourly}')
        fig, ax = plt.subplots(figsize=(14,7))
        sns.barplot(data=filtered_data_hourly, x='heure', y='consommation_brute_totale', ax=ax, palette='magma')
        ax.set_title(f'Consommation par heure le {selected_date_hourly}')
        ax.set_ylabel('Consommation Totale')
        ax.set_xlabel('Heure')
        st.pyplot(fig)

        st.write("Ce graphique permet à l'utilisateur de choisir une date et d'avoir les informations de consommation par heure sous la forme d'un bar chart.")

    ############################################################################################################

    with st.expander("Visualisation d'une comparaison de la consommation entre deux régions"):

        region1, region2 = st.sidebar.multiselect('Sélectionnez deux régions pour la comparaison', regions, default=[regions[0], regions[1]])
        data_region1 = data[data['code_insee_region'] == region1]
        data_region2 = data[data['code_insee_region'] == region2]
        st.title(f'Comparaison de la consommation entre {region1} et {region2}')
        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=data_region1, x='date_heure', y='consommation_brute_totale', ax=ax, label=region1)
        sns.lineplot(data=data_region2, x='date_heure', y='consommation_brute_totale', ax=ax, label=region2)
        ax.set_title(f'Comparaison de la consommation entre {region1} et {region2}')
        ax.set_ylabel('Consommation Totale')
        ax.set_xlabel('Date')
        ax.legend()
        st.pyplot(fig)

        st.write("Ce graphique nous permet de comparer la consommation entre deux régions sur toutes les dates disponibles.")

    ############################################################################################################

    with st.expander("Visualisation de la corrélation entre la consommation de gaz et d'électricité"):

        selected_region_corr = st.sidebar.selectbox('Choisir une région pour la corrélation', regions)
        data_corr = data[data['code_insee_region'] == selected_region_corr]
        st.title(f'Corrélation entre la consommation de gaz et d\'électricité pour {selected_region_corr}')
        fig, ax = plt.subplots(figsize=(14,7))
        sns.scatterplot(data=data_corr, x='consommation_brute_gaz_totale', y='consommation_brute_electricite_rte', ax=ax, hue='heure')
        ax.set_title(f'Corrélation entre la consommation de gaz et d\'électricité pour {selected_region_corr}')
        ax.set_ylabel('Consommation Électricité')
        ax.set_xlabel('Consommation Gaz')
        ax.legend(title='Heure')
        st.pyplot(fig)

        st.write("Ce graphique nous permet de visualiser facilement la corrélation entre la consommation d'électricité et de gaz pour une région donnée.")

    ############################################################################################################

    with st.expander("Visualisation de la consommation totale par région avec un pie chart"):

        pie_data = data.groupby('code_insee_region').sum()['consommation_brute_totale']

        st.title('Répartition de la consommation totale par région')
        fig, ax = plt.subplots(figsize=(14,7))
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel", n_colors=len(pie_data)))
        ax.axis('equal') 
        st.pyplot(fig)

        st.write("Ce graphique nous permet de voir la répartition de la consommation totale par région avec un pie chart. Cela confirme que le région 84 est la région")

    ############################################################################################################

    with st.expander("Visualisation de la consommation par heure pour une data spécifique avec slider"):

        st.title('Consommation par heure pour une journée spécifique')

        selected_date = st.slider('Sélectionnez une date', min_value=data['date_heure'].min().date(), max_value=data['date_heure'].max().date(), value=data['date_heure'].min().date())

        filtered_data = data[data['date_heure'].dt.date == selected_date]

        fig, ax = plt.subplots(figsize=(14,7))
        sns.lineplot(data=filtered_data, x=filtered_data['date_heure'].dt.hour, y='consommation_brute_totale', ax=ax)
        ax.set_title(f'Consommation par heure le {selected_date}')
        ax.set_ylabel('Consommation Totale')
        ax.set_xlabel('Heure')
        st.pyplot(fig)

        st.write("Ce graphique permet à l'utilisateur de choisir une date et d'avoir les informations de consommation par heure sous la forme d'un line chart.")

    ############################################################################################################

    with st.expander("Visualisation à l'aide d'une heatmap de la consommation totale pendant une journée"):

        data['jour'] = data['date_heure'].dt.day
        data['heure'] = data['date_heure'].dt.hour

        years = sorted(data['date_heure'].dt.year.unique())
        selected_year = st.sidebar.selectbox("Sélectionnez une année", years, index=len(years)-1)
        months = sorted(data[data['date_heure'].dt.year == selected_year]['date_heure'].dt.month.unique())
        selected_month = st.sidebar.selectbox("Sélectionnez un mois", months, index=len(months)-1)

        filtered_data = data[(data['date_heure'].dt.year == selected_year) & (data['date_heure'].dt.month == selected_month)]

        heatmap_data = filtered_data.groupby(['jour', 'heure']).mean()['consommation_brute_totale'].unstack()

        fig, ax = plt.subplots(figsize=(14,10))
        sns.heatmap(heatmap_data, cmap='YlGnBu', ax=ax)
        ax.set_title(f'Consommation pour {selected_month}/{selected_year}')
        ax.set_xlabel('Heure')
        ax.set_ylabel('Jour du mois')
        st.pyplot(fig)

        st.write("Ce graphique permet à l'utilisateur de choisir une année et un mois et d'avoir les informations de consommation par heure sous la forme d'un heatmap.")

    ############################################################################################################

    with st.expander("Évolution de la consommation totale sur l'ensemble des données"):

        daily_consumption = data.groupby(data['date_heure'].dt.date)['consommation_brute_totale'].sum().reset_index()

        fig = px.line(
            daily_consumption,
            x='date_heure',
            y='consommation_brute_totale',
            title="Évolution de la consommation totale sur l'ensemble des données",
            labels={'date_heure': 'Date', 'consommation_brute_totale': 'Consommation Totale'},
        )
        
        fig.update_xaxes(title_text='Date')
        fig.update_yaxes(title_text='Consommation Totale')
        st.plotly_chart(fig)

        st.write("Ce graphique permet de voir l'évolution de la consommation totale sur l'ensemble des données. On remarque une baisse à étudier plus tard en 2022 ce qui peut être un axe d'appronfondissement.")