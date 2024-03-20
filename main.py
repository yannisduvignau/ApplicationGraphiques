import re
import os
from datetime import datetime as date
from colorama import Fore, Style
import afficherGraphiques as aG


#Création du menu principal
def menu():
    """
    
    OBJECTIF : Présenter à l'utilisateur les différents choix de requete qui s'offre à lui

    """
    print(" Application python par Duvignau Yannis et Victoras Dylan")
    print("\n   S2.04 Etape 2 : 'Quel est l'impact des visites sur les actions d'une page Facebook ?'\n\n")
    print("      1 -- Quel est le nombre de visites par type de provenance ?")
    print("      2 -- Quelles sont les pages les plus consultées ?")
    print("      3 -- Quelle est la fréquentation du site ?\n\n")
    while True:
        choix = input("   Votre choix (1,2 ou 3): ")
        if choix in ["1", "2" ,"3"]: 
            return choix
        else:
            # Effacer le terminal pour Windows
            if os.name == 'nt':
                os.system('cls')
                
            print(Fore.RED + " +---------------------------------------------------------------------------------------+")
            print(" |             Saisie Incorrecte : vous ne saisissez aucune des propositions             |")
            print(" +---------------------------------------------------------------------------------------+" + Style.RESET_ALL)
            
            
            print("\n   S2.04 Etape 2 : 'Quel est l'impact des visites sur les actions d'une page Facebook ?'\n\n")
            print("      1 -- Quel est le nombre de visites par type de provenance ?")
            print("      2 -- Quelles sont les pages les plus consultées ?")
            print("      3 -- Quelle est la fréquentation du site ?\n\n")
            





def choix_prop1():
    
    ######################
    #   Initialisation   #
    ######################
    
    ok = "n"
    relancer = "n"
    # Variables pour messages d'erreur si erreur de saisie
    erreurFormat_DebPeriode = False
    erreurFormat_FinPeriode = False
    erreurDebordement_DebPeriode = False
    erreurDebordement_FinPeriode = False
    # Tuple des parametres
    periode = (0,0)
    deb_is_ok = False
    fin_is_ok = False
    
    #####################
    #    Traitements    #
    #####################
    
    # Tant que l'utilisateur souhaite continuer
    while (ok == "n"):
        # Effacer le terminal pour Windows
        if os.name == 'nt':
            os.system('cls')
        print(" Application python par Duvignau Yannis et Victoras Dylan")
        print("\n   S2.04 Etape 2 : 'Quel est l'impact des visites sur les actions d'une page Facebook ?'\n\n")
        print(Style.BRIGHT + Fore.GREEN + "      1 -- Quel est le nombre de visites par type de provenance ?" + Style.RESET_ALL)
        print("      2 -- Quelles sont les pages les plus consultées ?")
        print("      3 -- Quelle est la fréquentation du site\n\n")
        print("   Pour quelle période (facultatif) ?            *les données commencent le 2020-07-11 et finissent le 2022-12-19\n")
        
        if erreurFormat_DebPeriode == True:
            print(Fore.RED + " +-----------------------------------------------------+")
            print(" | Date de début saisie pas au bon format : aaaa-mm-jj |")
            print(" +-----------------------------------------------------+" + Style.RESET_ALL)
            erreurFormat_DebPeriode = False
            
        if erreurDebordement_DebPeriode == True:
            print(Fore.RED + " +---------------------------------+")
            print(" | Date de début saisie incorrecte |")
            print(" +---------------------------------+" + Style.RESET_ALL)
            erreurDebordement_DebPeriode = False
            
        debut_periode = input("   Debut au format aaaa-mm-jj (taper Entrée pour ignorer) : ")
        
        if erreurFormat_FinPeriode == True:
            print(Fore.RED + " +-----------------------------------------------------+")
            print(" | Date de fin saisie pas au bon format : aaaa-mm-jj   |")
            print(" +-----------------------------------------------------+" + Style.RESET_ALL)
            erreurFormat_FinPeriode = False
            
        if erreurDebordement_FinPeriode == True:
            print(Fore.RED + " +-------------------------------+")
            print(" | Date de fin saisie incorrecte |")
            print(" +-------------------------------+" + Style.RESET_ALL)
            erreurDebordement_FinPeriode = False
            
        fin_periode = input("   Fin au format aaaa-mm-jj (taper Entrée pour ignorer) : ")
        ok = input("\n\n  Afficher le graphique  (o/n) :")
        
        
       
        if ok == "o":
            
            # Si la date de début et/ou de fin ne sont pas définis alors on leur affecte la date de début des données et la date de fin des données
            if debut_periode == "":
               debut_periode = "2020-07-11"              # date de début des données
               deb_is_ok = True
            if fin_periode == "":
               fin_periode = "2022-12-19"                # date de fin des données
               fin_is_ok = True
            
            ### Vérifications des saisies : ###
           
            # On vérifie que la date de début (saisie par l'utilisateur) soit du format adapté et attendu
            # On vérifie également que la saisie soit cohérente avec la période et les données
            if (deb_is_ok!=True) and (not re.match(r"^\d{4}-\d{2}-\d{2}$", debut_periode) or (date.strptime(debut_periode, '%Y-%m-%d') < date.strptime("2020-07-11", '%Y-%m-%d') or date.strptime(debut_periode, '%Y-%m-%d') >= date.strptime(fin_periode, '%Y-%m-%d')) ):
                
                
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", debut_periode):
                    erreurFormat_DebPeriode = True
                    ok = "n"
                elif date.strptime(debut_periode, '%Y-%m-%d') < date.strptime("2020-07-11", '%Y-%m-%d') or date.strptime(debut_periode, '%Y-%m-%d') >= date.strptime(fin_periode, '%Y-%m-%d'):
                    erreurDebordement_DebPeriode = True
                    ok = "n"
            # On vérifie que la date de fin (saisie par l'utilisateur) soit du format adapté et attendu
            # On vérifie également que la saisie soit cohérente avec la période et les données
            if (fin_is_ok!=True) and (not re.match(r"^\d{4}-\d{2}-\d{2}$", fin_periode) or (date.strptime(fin_periode, '%Y-%m-%d') > date.strptime("2022-12-19", '%Y-%m-%d') or date.strptime(fin_periode, '%Y-%m-%d') >= date.strptime(debut_periode, '%Y-%m-%d'))):
                
                
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", fin_periode):
                    erreurFormat_FinPeriode = True
                    ok = "n"
                elif date.strptime(fin_periode, '%Y-%m-%d') > date.strptime("2022-12-19", '%Y-%m-%d') or date.strptime(fin_periode, '%Y-%m-%d') <= date.strptime(debut_periode, '%Y-%m-%d') :
                    erreurDebordement_FinPeriode = True
                    ok = "n"
        
        
        
        ####### AFFICHAGE GRAPHIQUE
        
        if ok == "o":  
            print(" ####### AFFICHAGE GRAPHIQUE ####### \n")
            
            # Parametres
            periode = (debut_periode, fin_periode)
            
            # Affichage du graphique n°1 (avec ses parametres) présent dans le fichier python "afficherGraphiques"
            aG.afficherGraphique1(periode)
            
            
            reponse = input(" -> Tapez Entrée pour terminer")
            
        # Donner à l'utilisateur le choix de relancer pour tester une autre requete ou bien changer les parametres
        if ok =="o":
            relancer = input("\n\n  Relancer  (o/n) :")
            break

    return relancer





def choix_prop2():
    
    ######################
    #   Initialisation   #
    ######################
    
    ok = "n"
    relancer = "n"
    # Variables pour messages d'erreur si erreur de saisie
    erreurFormat_DebPeriode = False
    erreurFormat_FinPeriode = False
    erreurDebordement_DebPeriode = False
    erreurDebordement_FinPeriode = False
    erreurLimit = False
    # Tuple des parametres
    periode_limit = (0,0,0)
    deb_is_ok = False
    fin_is_ok = False
    
    
    #####################
    #    Traitements    #
    #####################
    
    # Tant que l'utilisateur souhaite continuer
    while (ok == "n"):
        # Effacer le terminal pour Windows
        if os.name == 'nt':
            os.system('cls')
        print(" Application python par Duvignau Yannis et Victoras Dylan")
        print("\n   S2.04 Etape 2 : 'Quel est l'impact des visites sur les actions d'une page Facebook ?'\n\n")
        print("      1 -- Quel est le nombre de visites par type de provenance ?")
        print(Style.BRIGHT + Fore.GREEN + "      2 -- Quelles sont les pages les plus consultées ?" + Style.RESET_ALL)
        print("      3 -- Quelle est la fréquentation du site\n\n")
        print("   Pour quelle période (facultatif) ?            *les données commencent le 2020-07-11 et finissent le 2022-12-19\n")
        
        if erreurFormat_DebPeriode == True:
            print(Fore.RED + " +-----------------------------------------------------+")
            print(" | Date de début saisie pas au bon format : aaaa-mm-jj |")
            print(" +-----------------------------------------------------+" + Style.RESET_ALL)
            erreurFormat_DebPeriode = False
            
        if erreurDebordement_DebPeriode == True:
            print(Fore.RED + " +---------------------------------+")
            print(" | Date de début saisie incorrecte |")
            print(" +---------------------------------+" + Style.RESET_ALL)
            erreurDebordement_DebPeriode = False
            
        debut_periode = input("   Debut au format aaaa-mm-jj (taper Entrée pour ignorer) : ")
        
        if erreurFormat_FinPeriode == True:
            print(Fore.RED + " +-----------------------------------------------------+")
            print(" | Date de fin saisie pas au bon format : aaaa-mm-jj   |")
            print(" +-----------------------------------------------------+" + Style.RESET_ALL)
            erreurFormat_FinPeriode = False
            
        if erreurDebordement_FinPeriode == True:
            print(Fore.RED + " +-------------------------------+")
            print(" | Date de fin saisie incorrecte |")
            print(" +-------------------------------+" + Style.RESET_ALL)
            erreurDebordement_FinPeriode = False
            
        fin_periode = input("   Fin au format aaaa-mm-jj (taper Entrée pour ignorer) : ")
        print("\n\n\n   Nombre de résultats souhaités (facultatif) :                                                *361 pages en tout\n")
        
        if erreurLimit == True:
            print(Fore.RED + " +---------------------------------------------------------+")
            print(" | Le nombre de résultats doit être compris entre 1 et 361 |")
            print(" +---------------------------------------------------------+" + Style.RESET_ALL)
            erreurLimit = False
        
        limit = input("   Combien de résultats voulez-vous (taper Entrée pour ignorer) : ")
        
        
        ok = input("\n\n  Afficher le graphique  (o/n) :")
        
        
        if ok == "o":
            
            # Si la date de début et/ou de fin ne sont pas définis alors on leur affecte la date de début des données et la date de fin des données
            if debut_periode == "":
               debut_periode = "2020-07-11"              # date de début des données
               deb_is_ok = True
            if fin_periode == "":
               fin_periode = "2022-12-19"                # date de fin des données
               fin_is_ok = True
            
            ### Vérifications des saisies : ###
           
            # On vérifie que la date de début (saisie par l'utilisateur) soit du format adapté et attendu
            # On vérifie également que la saisie soit cohérente avec la période et les données
            if (deb_is_ok!=True) and (not re.match(r"^\d{4}-\d{2}-\d{2}$", debut_periode) or (date.strptime(debut_periode, '%Y-%m-%d') < date.strptime("2020-07-11", '%Y-%m-%d') or date.strptime(debut_periode, '%Y-%m-%d') >= date.strptime(fin_periode, '%Y-%m-%d')) ):
                
                
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", debut_periode):
                    erreurFormat_DebPeriode = True
                    ok = "n"
                elif date.strptime(debut_periode, '%Y-%m-%d') < date.strptime("2020-07-11", '%Y-%m-%d') or date.strptime(debut_periode, '%Y-%m-%d') >= date.strptime(fin_periode, '%Y-%m-%d'):
                    erreurDebordement_DebPeriode = True
                    ok = "n"
            # On vérifie que la date de fin (saisie par l'utilisateur) soit du format adapté et attendu
            # On vérifie également que la saisie soit cohérente avec la période et les données
            if (fin_is_ok!=True) and (not re.match(r"^\d{4}-\d{2}-\d{2}$", fin_periode) or (date.strptime(fin_periode, '%Y-%m-%d') > date.strptime("2022-12-19", '%Y-%m-%d') or date.strptime(fin_periode, '%Y-%m-%d') >= date.strptime(debut_periode, '%Y-%m-%d'))):
                
                
                if not re.match(r"^\d{4}-\d{2}-\d{2}$", fin_periode):
                    erreurFormat_FinPeriode = True
                    ok = "n"
                elif date.strptime(fin_periode, '%Y-%m-%d') > date.strptime("2022-12-19", '%Y-%m-%d') or date.strptime(fin_periode, '%Y-%m-%d') <= date.strptime(debut_periode, '%Y-%m-%d') :
                    erreurDebordement_FinPeriode = True
                    ok = "n"
               
            # On vérifie que la limite (saisie par l'utilisateur) soit du format adapté et attendu
            # On vérifie également que la saisie soit cohérente avec la période et les données
            if limit != "" and limit not in [str(i) for i in range(1, 362)]:
               erreurLimit = True
               ok = "n"
            # Si la limite n'as pas ete saisie on lui affecte le nombre de page present dans la base de données
            elif limit == "":
               limit = 361
            else :
               limit = int(limit)
               
           
        if ok == "o":
            ####### AFFICHAGE GRAPHIQUE
            print(" ####### AFFICHAGE GRAPHIQUE ####### \n")
            
            # Parametres
            periode_limit = (debut_periode, fin_periode, limit)
            
            # Affichage du graphique n°2 (avec ses parametres) présent dans le fichier python "afficherGraphiques"
            aG.afficherGraphique2(periode_limit)
                            
            reponse = input(" -> Tapez Entrée pour terminer")
            
            
        # Donner à l'utilisateur le choix de relancer pour tester une autre requete ou bien changer les parametres    
        if ok =="o":
            relancer = input("\n\n  Relancer  (o/n) :")
            break

    return relancer




def choix_prop3():
    
    ######################
    #   Initialisation   #
    ######################
    
    ok = "n"
    relancer = "n"
    
    #####################
    #    Traitements    #
    #####################
    
    # Tant que l'utilisateur souhaite continuer
    while (ok == "n"):
        # Effacer le terminal pour Windows
        if os.name == 'nt':
            os.system('cls')
        print(" Application python par Duvignau Yannis et Victoras Dylan")
        print("\n   S2.04 Etape 2 : 'Quel est l'impact des visites sur les actions d'une page Facebook ?'\n\n")
        print("      1 -- Quel est le nombre de visites par type de provenance ?")
        print("      2 -- Quelles sont les pages les plus consultées ?")
        print(Style.BRIGHT + Fore.GREEN + "      3 -- Quelle est la fréquentation du site" + Style.RESET_ALL)
        ok = input("\n\n  Afficher le graphique  (o/n) :")
        
        if ok == "o":
            ####### AFFICHAGE GRAPHIQUE
            print(" ####### AFFICHAGE GRAPHIQUE ####### \n")
            
            # Affichage du graphique n°3 présent dans le fichier python "afficherGraphiques"
            aG.afficherGraphique3()
            
            reponse = input(" -> Tapez Entrée pour terminer")
        
        
        # Donner à l'utilisateur le choix de relancer pour tester une autre requete ou bien changer les parametres
        if ok =="o":
            relancer = input("\n\n  Relancer  (o/n) :")
            break
    return relancer



relancer="o"
while (relancer=="o") :
    # Effacer le terminal pour Windows
    if os.name == 'nt':
        os.system('cls')
    choix_prop = menu()
    if choix_prop == "1":
        if choix_prop1()=="n":
            quit()
    if choix_prop == "2":
        if choix_prop2()=="n":
            quit()
    if choix_prop == "3":
        if choix_prop3()=="n":
            quit()
            
"""
    CONTINUER A COMMENTER LE CODE !!! 
"""