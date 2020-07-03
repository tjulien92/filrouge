

# Phase 1
    # un individus avec son smartphone envoie des pacquets sur le réseau modélisé ici par une liste.
    # la population modélisée par une matice (liste de liste) est un ensemble d'individus envoyant des pacquets sur le réseau.
    # un pacquet est une ligne de la matrice (1 bit = 1 élément de la liste = 1, 2, 3 respectivement priorité haute à priorité basse, 1 bit à ajouter à la fin = une réponse de traitement = None ou (1, requète traitée))
    # la population est la matrice (1 millions de pacquet)

    #deux use cases:
    # - le reseau est chargé à environ 20%
        # 20% de la population donc 20% des pacquets arrive sur le réseau
        # la file d'attente = 20% de la population
    # - le réseau est chargé à plus de 80%
        # plus de 80% de la population donc 80% des pacquets arrive sur le réseau
            #- Définir aléatoirement un nombre en 0.8 < Nombre < 1
        # la file d'attente = Nombre x 100% de la population
        
    # trois algorithme d'ordonnancement pour traiter la file d'attente à tester les un a la suite des autres
        # - FIFO
            # fonction modélisant FIFO
            # fonction de Traitement de chaque pacquets (algorithme de trie ou calcul de la somme des éléments de la liste)
            # modifier le bit de réponse du traitement et le mettre à (1, requète traitée)
            # on stocke dans une liste le temps de traitement de chaque pacquet pour ensuite faire la moyenne de traitement et avoir des statistiques en fonction de chaque use case
            # ajouter le temps de traitement du pacquet a la fin du pacquet qu'on souhaite minimiser pour une meilleur QoS
        
        # - PQ
            # on exécute les meme action que fifo
        # - WFQ
            # on exécute les meme action que fifo
            
        # on fait la comparaison de chaque algo dans un tableau recapitulatif avec temps moyen de traitement de chaque pacquet et pupulattion
    # LES EXIGENCES: faible latence (modélisation en cours de réflection, 
                   # traitement de massif de pacquet (nombre important de paquet), 
                   # haut débit ok (modélisé par le faible temps de traitement)
                   
    
        
# Phase 2 introduction du slicing 
    # designer un repartiteur des pacquets de la population en fonction des slices pour ensuite appliquer l'agorithme ci dessus
        # - définir les slices et affecter un bit propre au slice reférentiel dans les pacquets
            # - un slice va representer une tribu donc une parti de la population
      # - application de l'algo de la phase 1 au tribu ecomparaison
      
    #Analyse global des résultats afin des sélectionner de facon automatique par un algo IA ou un algo d'optimisation en fonction de la population et de la charge du réseau

# phase 3 
    # designe de l'algo de selection automatique
    #prédiction du nombre d'individus par slice en fonction des jours de la semaine, des heures, des nombre d'utilisateur au meme date antérieur, et de l'actualité avec une précision, et génération de chaque tribu
    #on fait tournber l'algo de la phase 1 et on selectionne l'algorithme adapté a la période


# si on à le temps on pourra combiner les algo d'ordonnancement pour voir comment optimiser le temps de traitement


# pour un nombre d'user donnée, on aur aura un temps de traitement de paquet respectable. ces deux paramètres sont fixé comme des valeur seuil.
# On écoute le nombre d'utilisateur sur le réseau et on controle de temps de traitement 
# si le temps de traitement est supérerieur au seuil défini:
    # on affiche temps de traitement supérieur au seuil... redimensionnement du réseau...
    # on récupère le nombre d'utilisateur
    # on sélectionne l'algorithme avec un temps de traitement inférieur au seuil.
        # si yen a pas:
            # on selectionne celui qui est le plus proche du seuil et on rajoute une nouvelle file d'attente qui se supprimera quand le nombre d'user sera redescendu à une valeur seuil  
            # seulement pour la 5G lorsqu'on atteint un deuxième seuil, on rajoute une slice imaginaire qui se supprimera quand le nombre d'user sera redescendu à une valeur seuil 

'''l =[1,2,3,3,2,1,1,4,5,3,7]
l2=sorted(l[1:])
print(l,l2)

import time
import random
print (time.strftime('%D', time.gmtime(random.randint(0, int(time.time())))))
semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
heur= int('13h'.split('h')[0])
jourSemaine=semaine.index('mercredi')+1  

print(heur, jourSemaine)'''
import time
with open("pouRcentage.txt","r") as file:
    P=float(file.read())
print("\n[chargement du réseau à {}%...]".format(P))
start_timeR = time.time()
#SurReseau = pacquetSurReseau(P)
print("Fait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
print("[Traitement des paquets ...]\n")