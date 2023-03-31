##############################################################################################
#############      PROJET DE PYTHON PROPOSER PAR LE PROFESSEUR ELYSEE VILLARD    #############
#############                       Nom    : SAINTERLIN                          #############
#############                       Prenom : Edson                               #############
#############                       Date   : 31 Mars 2023                        #############
##############################################################################################

# chargement des modules 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import *

# Chargement des données de Débit 
data = pd.read_csv("data/MIREBALAIS___RIVIERE_ARTIBONITE_30202.txt", skiprows=22, sep=";")

# Chargement des données de précipitation de la station P_057_MIREBALAIS 
data_Mi = pd.read_csv("data/P_057_MIREBALAIS.txt", skiprows=21, sep=";")

#Uniformiser les données de precipitation afin qu'on a une même intervalle 
data_SMir=data_Mi.loc[1004:6939]

# Conversions les types de données objet en numerique
data_SMir['\tP'] = pd.to_numeric(data_SMir['\tP'], errors='coerce')
data['Q'] = pd.to_numeric(data['Q'], errors='coerce')

#Supprimer les valeur NaN (Not a Number) 
data_sans_na = data.dropna()
data_SMir_sNa = data_SMir.dropna()

#Formater la colonne date des Débits et des précipitations
data_sans_na["Date"] = pd.to_datetime(data_sans_na["Date"], format="%Y-%m-%d")
data_SMir_sNa["Date"] = pd.to_datetime(data_SMir_sNa["Date"], format="%Y-%m-%d")

# P.1.1-Déterminer le débit le plus faible pour chaque année
#grouper les Debit par année et calcul du minimum
Debit_min = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).min()
Debit_min["Date"] = Debit_min.index
Debit_min["Q"], Debit_min["Date"] = Debit_min["Date"], Debit_min["Q"]
Debit_min.rename(columns={"Date": "Débit"}, inplace=True)
Debit_min.rename(columns={"Q": "Date"}, inplace=True)
Debit_min.reset_index(drop=True, inplace=True) 
Debit_min_nor=Debit_min.drop([13], axis=0, inplace=True) 

#graphe du Débit minimum Annuel
plt.grid(True) 
plt.plot(Debit_min.Date, Debit_min.Débit, "b", linewidth=0.9 )
plt.title("Evolution du Débit journalier minimal Annuel")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s)")
plt.savefig("Debit_min.png", dpi=300)
plt.show()

# P.1.2-Déterminer le débit le plus élevé pour chaque années 
#grouper les Debit par année et calcul du maximum
Debit_max = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).min()
Debit_max["Date"] = Debit_max.index
Debit_max["Q"], Debit_max["Date"] = Debit_max["Date"], Debit_max["Q"]
Debit_max.rename(columns={"Date": "Débit"}, inplace=True)
Debit_max.rename(columns={"Q": "Date"}, inplace=True)
Debit_max.reset_index(drop=True, inplace=True) 
Debit_max_nor=Debit_max.drop([13], axis=0, inplace=True) 

#graphe du debit Annuel
plt.grid(True) 
print(Debit_min)
plt.plot(Debit_max.Date, Debit_max.Débit, "b", linewidth=0.9 )
plt.title("Evolution du Débit journalier maximal Annuel")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s)")
plt.savefig("Debit_max.png", dpi=300)
plt.show()

# P.1.3.1-Etude de l'évolution de la moyenne du débit mensuel en fonction du temps
#grouper par mois et calcul de la moyenne sur chaque mois
Debit_month = data_sans_na.groupby(pd.Grouper(key="Date", freq="M")).mean()
Debit_month["Date"] = Debit_month.index
Debit_month["Q"], Debit_month["Date"] = Debit_month["Date"], Debit_month["Q"]
Debit_month.rename(columns={"Date": "Débit"}, inplace=True)
Debit_month.rename(columns={"Q": "Date"}, inplace=True)
Debit_month.reset_index(drop=True, inplace=True)
Debit_month.drop(Debit_month.index[147:159], axis=0, inplace=True)

#graphe du Débit moyen journalier mensuel
plt.grid(True) 
plt.plot(Debit_month.Date, Debit_month.Débit, "g", linewidth=0.9 )
plt.title("Variation du Débit journalier moyen mensuel")
plt.xlabel("Année")
plt.ylabel("Debit (m3/s/mois)")
plt.savefig("Evolu_Debit_mensuel.png", dpi=300)
plt.show()

# P.1.3.2-Etude de l'évolution de la moyenne du débit annuel en fonction du temps
#grouper les Debit par années et calcul de la moyenne
Debit_Annuel = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).mean()
Debit_Annuel["Date"] = Debit_Annuel.index
Debit_Annuel["Q"], Debit_Annuel["Date"] = Debit_Annuel["Date"], Debit_Annuel["Q"]
Debit_Annuel.rename(columns={"Date": "Débit"}, inplace=True)
Debit_Annuel.rename(columns={"Q": "Date"}, inplace=True)
Debit_Annuel.reset_index(drop=True, inplace=True) 
Debit_Annuel_nor=Debit_Annuel.drop([13], axis=0, inplace=True) 

#graphe du debit Annuel
plt.grid(True) 
print(Debit_Annuel)
plt.plot(Debit_Annuel.Date, Debit_Annuel.Débit, "b", linewidth=0.9 )
plt.title("Evolution du Débit journalier moyen Annuel")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s/an)")
plt.savefig("Debit_Annuel.png", dpi=300)
plt.show()

# P.1.3.3-Etude de l'évolution de la moyenne du débit chaque deux ans en fonction du temps
#grouper les Debit chaque deux années et calcul de la moyenne
Debit_2Ans = data_sans_na.groupby(pd.Grouper(key="Date", freq="2Y")).mean()
Debit_2Ans["Date"] = Debit_2Ans.index
Debit_2Ans["Q"], Debit_2Ans["Date"] = Debit_2Ans["Date"],Debit_2Ans["Q"]
Debit_2Ans.rename(columns={"Date": "Débit"}, inplace=True)
Debit_2Ans.rename(columns={"Q": "Date"}, inplace=True)
Debit_2Ans.reset_index(drop=True, inplace=True) 
 

# Le graphe du Debit moyen journalier Chaque deux ans
plt.grid(True) 
plt.plot(Debit_2Ans.Date, Debit_2Ans.Débit, "r", linewidth=0.9 )
plt.title("Evolution du Débit journalier moyen chaque deux Ans")
plt.xlabel("Année")
plt.ylabel("Débit")
plt.savefig("Debit_2Ans2.png", dpi=300)
plt.show()

# P.1.4.1-Diviser les données de Débit en 4 périodes consécutives 
data1=data.loc[0:1392]
data2=data.loc[1393:2784]
data3=data.loc[2785:4177]
data4=data.loc[4178:5570]

# Exporter les données des 4 periodes consécutives dans le dossier output
fichier1 = "output/data1.txt"
data1.to_csv(fichier1, sep=";", index=False)
fichier2 = "output/data2.txt"
data2.to_csv(fichier2, sep=";", index=False)
fichier3 = "output/data3.txt"
data3.to_csv(fichier3, sep=";", index=False)
fichier4 = "output/data4.txt"
data4.to_csv(fichier4, sep=";", index=False)

#Formater les dates pour les periodes
data1["Date"] = pd.to_datetime(data1["Date"], format="%Y-%m-%d")
data2["Date"] = pd.to_datetime(data2["Date"], format="%Y-%m-%d")
data3["Date"] = pd.to_datetime(data3["Date"], format="%Y-%m-%d")
data4["Date"] = pd.to_datetime(data4["Date"], format="%Y-%m-%d")
data3=data3.dropna()

#P.1.4.2- Etudier l'évolution du débit sur la premiere période.
plt.grid(True)
plt.plot(data1.Date, data1.Q, linewidth=0.9 )
plt.title("Evolution du Débit journalier pour la premiere periode")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s")
plt.xticks(rotation=30)
plt.savefig("data1.png", dpi=300)
plt.show()

#P.1.4.3- Etudier l'évolution du débit sur la deuxieme période.
plt.grid(True)
plt.plot(data2.Date, data2.Q, linewidth=0.9 )
plt.title("Evolution du Débit journalier pour la deuxieme periode")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s")
plt.xticks(rotation=30)
plt.savefig("data2.png", dpi=300)
plt.show()

#P.1.4.4- Etudier l'évolution du débit sur la troisieme période.
plt.grid(True)
plt.plot(data3.Date, data3.Q, linewidth=0.9 )
plt.title("Evolution du Débit journalier pour la troisieme periode")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s")
plt.xticks(rotation=30)
plt.savefig("data3.png", dpi=300)
plt.show()

#P.1.4.5- Etudier l'évolution du débit sur la quatrieme période.
plt.grid(True)
plt.plot(data4.Date, data4.Q, linewidth=0.9 )
plt.title("Evolution du Débit journalier pour la quatrieme periode")
plt.xlabel("Année")
plt.ylabel("Débit(m3/s")
plt.savefig("data4.png", dpi=300)
plt.show()


# P.2.1-Déterminer  la précipitation la plus faible pour chaque année, et faire une comparaison avec P1.1  
#grouper les Precipitations par année et calcul du minimum
precipition_Min = data_SMir_sNa.groupby(pd.Grouper(key="Date", freq="Y")).min()
precipition_Min["Date"] = precipition_Min.index
precipition_Min["\tP"], precipition_Min["Date"] = precipition_Min["Date"], precipition_Min["\tP"]
precipition_Min.rename(columns={"Date": "P"}, inplace=True)
precipition_Min.rename(columns={"\tP": "Date"}, inplace=True)
precipition_Min.reset_index(drop=True, inplace=True)  

#Afficher le graphe de la précipitation minimum Annuelle avec le titre des axes
precipition_Min.plot(x="Date", y=["P"], linewidth=0.8 )
plt.title("Evolution de la précipitation journalière minimale Annuelle")
plt.xlabel("Année")
plt.ylabel("Précipitation(mm/j)")
plt.savefig("Précipitation_Min.png", dpi=300)
plt.show()

# Comparaison des Debits et precipitations maximum
# Données des débits maximum annuels et des précipitations maximum annuelles
debit_min_precipitation_min_fusionner=pd.merge(Debit_min, precipition_Min, on="Date")
#Extraction de la liste contenant les precipitations
debit_min_annuel=debit_min_precipitation_min_fusionner["Débit"].tolist()
# Extraction de la liste contenant les Debits
precip_min_annuel=debit_min_precipitation_min_fusionner["P"].tolist()
# Création des positions des barres pour les deux jeux de données
bar_positions_debit = np.arange(len(debit_min_annuel))
bar_positions_precip = bar_positions_debit + 0.2

# Tracé des barres pour les débits maximum annuels
plt.bar(bar_positions_debit, debit_min_annuel, width=0.1, color='b', label='Débits max. annuels')
# Tracé des barres pour les précipitations maximum annuelles
plt.bar(bar_positions_precip, precip_min_annuel, width=0.1, color='g', label='Précip. max. annuelles')
# Configuration de l'axe des x
plt.xticks(bar_positions_debit + 0.01, range(1922, 1938))
# Configuration de la légende et du titre
plt.legend()
plt.title('Débits min. annuels et précip. min. annuelles')
plt.xticks(rotation=45)
plt.savefig("Debit_2Ans.png", dpi=300)
# Affichage du graphe
plt.show()

# P.2.2-Déterminer la précipitation  la plus élevée pour chaque année, et faire une comparaison avec P1.2
#grouper les Precipitations par année et calcul du maximum
precipition_Max = data_SMir_sNa.groupby(pd.Grouper(key="Date", freq="Y")).max()
precipition_Max["Date"] = precipition_Max.index
precipition_Max["\tP"], precipition_Max["Date"] = precipition_Max["Date"], precipition_Max["\tP"]
precipition_Max.rename(columns={"Date": "P"}, inplace=True)
precipition_Max.rename(columns={"\tP": "Date"}, inplace=True)
precipition_Max.reset_index(drop=True, inplace=True)  

#Afficher le graphe de la précipitation maximum Annuelle et nomme les axes
plt.grid(True) 
plt.plot(precipition_Max.Date, precipition_Max.P, "b", linewidth=0.8 )
plt.title("Evolution de la précipitation journalière maximale Annuelle")
plt.xlabel("Année")
plt.ylabel("Précipitation(mm/j)")
plt.savefig("Précipitation_Max.png", dpi=300)
plt.show()

# Comparaison des Debits et precipitation maximum
# Données des débits maximum annuels et des précipitations maximum annuelles
debit_max_precip_max_fusionner=pd.merge(Debit_max, precipition_Max, on="Date")
#Extraction de la liste contenant les precipitations
debit_max_annuel=debit_max_precip_max_fusionner["Débit"].tolist()
# Extraction de la liste contenant les Debits
precip_max_annuel=debit_max_precip_max_fusionner["P"].tolist()
# Création des positions des barres pour les deux jeux de données
bar_positions_debit = np.arange(len(debit_max_annuel))
bar_positions_precip = bar_positions_debit + 0.1

# Tracé des barres pour les débits maximum annuels
plt.bar(bar_positions_debit, debit_max_annuel, width=0.1, color='b', label='Débits max. annuels')
# Tracé des barres pour les précipitations maximum annuelles
plt.bar(bar_positions_precip, precip_max_annuel, width=0.1, color='g', label='Précip. max. annuelles')
# Configuration de l'axe des x
plt.xticks(bar_positions_debit + 0.1, range(1922, 1938))
# Configuration de la légende et du titre
plt.legend()
plt.title('Débits max. annuels et précip. max. annuelles')
plt.xticks(rotation=45)
plt.savefig("comparaison.png", dpi=300)
# Affichage du graphe
plt.show()

# P.2.3-Donner deux représentations graphiques de type “scatter” de la moyenne mensuelle de la pluviométrie et de débit.
#grouper les precipitations de Mirbalais par mois et calcul de la moyenne 
precipit_mensuel = data_SMir_sNa.groupby(pd.Grouper(key="Date", freq="M")).mean()
precipit_mensuel["Date"] = precipit_mensuel.index
precipit_mensuel["\tP"], precipit_mensuel["Date"] = precipit_mensuel["Date"], precipit_mensuel["\tP"]
precipit_mensuel.rename(columns={"Date": "P"}, inplace=True)
precipit_mensuel.rename(columns={"\tP": "Date"}, inplace=True)
precipit_mensuel.reset_index(drop=True, inplace=True) 

# P.2.3.1-Représentations graphiques de type “scatter” de la moyenne mensuelle du débit
x=Debit_month["Date"]
y=Debit_month["Débit"]
# Tracer le graphe
plt.scatter(x, y)
# Ajouter des étiquettes d'axe et un titre
plt.xlabel("Année")
plt.ylabel("Débit(mm/mois)")
plt.title("Graphiques de type “scatter” de la moyenne mensuelle du débit.")
plt.savefig("Debit_mensuel.png", dpi=300)
# Afficher le graphe
plt.show()

# P.2.3.2-Représentations graphiques de type “scatter” de la moyenne mensuelle des précipitations
x=precipit_mensuel["Date"]
y=precipit_mensuel["P"]
# Tracer le graphe
plt.scatter(x, y)
# Ajouter des étiquettes d'axe et un titre
plt.xlabel("Année")
plt.ylabel("précipitation(mm/mois)")
plt.title("Graphiques de type “scatter” de la moyenne mensuelle des précipitations.")
plt.savefig("Precipitation_mensuel.png", dpi=300)
# Afficher le graphe
plt.show()

# P.2.4-Calculer de deux manières la corrélation de Pearson entre les données de pluviométrie et de débit:

# a._ Manuellement en créant une fonction

def correlation_pearson(s1, s2):
    n = len(s1)
    
    sum_s1 = sum(s1)
    sum_s2 = sum(s2)
    
    sum_pds1 = sum([x**2 for x in s1])
    sum_pds2 = sum([x**2 for x in s2])
    
    sum_prod = sum([s1[i]*s2[i] for i in range(n)])
    
    num = n*sum_prod - sum_s1*sum_s2
    den = sqrt((n*sum_pds1 - sum_s1**2) * (n*sum_pds2 - sum_s2**2))
    
    if den == 0:
        return 0
    
    return num/den

#Fusionner les données de Debit et de pluviometrie pour avoir des listes de meme longueur
data_fusionner=pd.merge(data_sans_na, data_SMir_sNa, on="Date")
#Extraction de la liste contenant les precipitations
s1=data_fusionner["\tP"].tolist()
# Extraction de la liste contenant les Debits
s2=data_fusionner["Q"].tolist()
# Afficharge du coefficient de person pour les deux listes
print("coefficient_Pearson=", format(correlation_pearson(s1, s2), ".3f"))

# b._ Avec Pandas
coef1=data_fusionner["Q"].corr(data_fusionner["\tP"]).round(decimals=3)

print("coefficient_Pandas=", coef1)

fichier2="output/precipit_mensuel.txt"
fichier1="output/data_SMir.txt"
fichier3="output/data_fusionner.txt"
data_SMir.to_csv(fichier1, sep=";", index=False)
precipit_mensuel.to_csv(fichier2, sep=";", index=False)
data_fusionner.to_csv(fichier3, sep=";", index=False)

