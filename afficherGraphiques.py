# -*- coding: utf-8 -*-
"""
Created on Sun May 14 09:06:48 2023

@author: duvig_
"""
import pyodbc as p
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime

#Connection avec la base de donnée grace au DSN
conn=p.connect('DSN=bd_perso')
cursor = conn.cursor()


def afficherGraphique1(parametre):
    debut_periode = datetime.strptime(parametre[0], "%Y-%m-%d")
    fin_periode = datetime.strptime(parametre[1], "%Y-%m-%d")
    #debut_periode = periode[0]
    #fin_periode = periode[1]
    
    sql = """SELECT Referer_type, COUNT(*) AS Nb_visites 
             FROM Visites JOIN ActionsVisites ON Visites.Id_visit = ActionsVisites.Id_visit
             WHERE Server_time BETWEEN ? AND ? 
             GROUP BY Referer_type;
          """
    param = (debut_periode,fin_periode)
    cursor.execute(sql,param)
    result = cursor.fetchall()
    
    refer_type = []
    visits = []
    for row in result:
        refer_type.append(str(row[0]))
        visits.append(row[1])
        
    
    # Création du diagramme à barres
    fig = plt.figure(num="Graphique -- requête 1",figsize=(19, 9.5))
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(refer_type, visits)
    ax.set_xlabel('Referer_type')
    ax.set_ylabel('Nombre de visites')
    ax.set_title('Nombre de visites par type de provenance')
    # Ajout des chiffres sur chaque barre
    for i, v in enumerate(visits):
        ax.text(i, v+77, str(v), ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    ax.legend(['Du ' + str(datetime.date(debut_periode)) + ' au ' + str(datetime.date(fin_periode))],loc="upper right",shadow=True)

    
    return plt.show()


def afficherGraphique2(parametre):
    debut_periode = datetime.strptime(parametre[0], "%Y-%m-%d")
    fin_periode = datetime.strptime(parametre[1], "%Y-%m-%d")
    
    sql = """SELECT Pages.Nom_page, COUNT(*) AS Nb_visites 
             FROM ActionsVisites INNER JOIN Actions ON ActionsVisites.Id_action = Actions.idaction RIGHT JOIN Pages ON Actions.idpage = Pages.Id_page 
             WHERE ActionsVisites.Server_time BETWEEN ? AND ? 
             GROUP BY Pages.Nom_page 
             ORDER BY Nb_visites DESC 
             LIMIT ?;
          """
    param = (debut_periode,fin_periode,parametre[2])
    cursor.execute(sql, param)
    
    limit=parametre[2]
    # Récupération des résultats de la requête
    result = cursor.fetchall()
    
    # Création des listes pour le graphique
    labels = []
    sizes = []
    others = 0
    
    # Si la limite est supérieure à 15, on rassemble les pages à partir de la 4ème dans la catégorie "Autres"
    if limit > 15 and limit < 361:
        for i in range(3):
            labels.append(result[i][0])
            sizes.append(result[i][1])
        for i in range(3, len(result)-3):
            others += result[i][1]
        labels.append("...")
        sizes.append(others)
        for i in range(len(result)-3, len(result)):
                labels.append(result[i][0])
                sizes.append(result[i][1])
    # Sinon, on crée la catégorie "Autres" pour les pages ayant une valeur inférieure à 1,5%
    else:
        for row in result:
            if row[1] / result[0][1] < 0.07:
                others += row[1]
            else:
                labels.append(row[0])
                sizes.append(row[1])
        if others > 0:
            labels.append("Autres")
            sizes.append(others)
    
    
        
        # Création du diagramme circulaire
    fig = plt.figure(num="Graphique -- requête 2",figsize=(19, 9.5))
    ax = fig.add_subplot(1, 1, 1)
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Pages les plus consultées')
    ax.legend(['Du ' + str(datetime.date(debut_periode)) + ' au ' + str(datetime.date(fin_periode))],loc="upper right",shadow=True)

        
    return plt.show()



def afficherGraphique3():
    
    sql = """SELECT YEAR(Server_time) AS year, MONTH(Server_time) AS month, COUNT(DISTINCT Id_visit) AS nbVisites 
             FROM ActionsVisites 
             GROUP BY YEAR(Server_time), MONTH(Server_time) 
             ORDER BY year, month;
          """
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    # Extraction des données dans des listes pour créer le diagramme
    months = []
    visits = []
    for row in result:
        months.append(str(row[1]) + '/' + str(row[0]))
        visits.append(row[2])
    
    
    
    # Création du diagramme à barres
    fig = plt.figure(num="Graphique -- requête 3",figsize=(19, 9.5))
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(months, visits)
    ax.set_xlabel('Mois')
    ax.set_ylabel('Nombre de visites')
    ax.set_title('Fréquentation du site')
    # Ajout des chiffres sur chaque barre
    for i, v in enumerate(visits):
        if i < 6:
            ax.bar(i, v, color='red')
        elif i >=6 and i<18:
            ax.bar(i, v, color='green')

        
        ax.text(i+0.05, v+77, str(v), ha='center', va='bottom', rotation=90, fontweight='bold', fontsize=7)

    #Ajout Légende
    handles = [mpatches.Patch(color='red', label='2020'), mpatches.Patch(color='green', label='2021'), mpatches.Patch(color=None, label='2022')]
    ax.legend(handles=handles, loc='upper left', shadow=True)
    
    plt.xticks(rotation=90)

    
    return plt.show()