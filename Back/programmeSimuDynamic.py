import random
import time
import csv
import numpy as np
import subprocess
import sqlite3

import pandas as pd, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
# *********************************************************************************************************************************************
#Phase 1
def génèrePacquetPopulation(NbUtilisateur):
    fichier = csv.writer(open ('datasetTestOrdonnancement.csv','a',newline=''))
    fichier.writerow(['bit 1','bit 2','bit 3','bit 4','bit 5','bit 6'])
    population = []
    for i in range(NbUtilisateur):
        pacquet = [random.randint(0,100) for i in range(6)]
        pacquet[0]=random.randint(1,3)#priority
        pacquet[1]=random.randint(1,3)#slicing
        fichier.writerow(pacquet)    

def uploadDB(NbUtilisateur):
    baseDeDonnees = sqlite3.connect(datasetTestOrdonnancement)
    curseur = baseDeDonnees.cursor()
    for i in range(NbUtilisateur):
        pacquet = [random.randint(0,100) for i in range(6)]
        pacquet[0]=random.randint(1,3)#priority
        pacquet[1]=random.randint(1,3)#slicing
        curseur.execute("INSERT INTO DataOrdonnancement (Bit 1, Bit 2, Bit 3, Bit 4, Bit 5, Bit 6) VALUES (?, ?, ?, ?, ?, ?)",
        tuple(pacquet))
    baseDeDonnees.commit()
    
def génèreDataPrévision():
    fichier = csv.writer(open ('datasetPrevisionNombrePaquet.csv','a',newline=''))
    fichier.writerow(['Nombre de Paquet','JourSemaine','Heure'])
    #semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"] 
    semaine=[1,2,3,4,5,6,7]
    for i in range(3000):
        heure = time.strftime('%H', time.gmtime(random.randint(0, int(time.time()))))
        jour= random.choice(semaine)
        npac= random.randint(20000000,100000000)
        fichier.writerow([npac,jour,heure])
    
def pacquetSurReseau(poucentage):    
    # alpha= int(poucentage*1000000)
    alpha= int(poucentage*0.3)

    check=0
    SurReseau=[] 
    reader = csv.reader(open("test.csv","r"))   
    for row in reader:
        if row == ['bit 1','bit 2','bit 3','bit 4','bit 5','bit 6']:
            print('en cours de traitement...')
        elif row == []:
            pass
        else:
            SurReseau.append(list(map(int, row)))
        check+=1
        if check == alpha:
            break
    return SurReseau
    
def traitement(pacquet):
    i=[pacquet[0],pacquet[1]]
    liste = sorted(pacquet[2:])
    liste.append(sum(liste))
    return i+liste
    
def FIFO():
    
    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}%...]".format(P))
    start_timeR = time.time()
    SurReseau = pacquetSurReseau(P)
    print("Fait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
    print("[Traitement des paquets ...]\n")

    
    if SurReseau==[]:
        print ('Slice non utilisée')
    else:
        start_timeR = time.time()
        tempsTraitementPacquetIndividus=[]
        tempsTraitementPacquetSurleReseau=0
        for i in SurReseau:
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            i= traité
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
        tempsTraitementPacquetSurleReseau= time.time()-start_timeR
        print('méthode FIFO:')
        print("temps de traitement moyen d'un pacquet: ", sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus))
        print("temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau)
        # print("\n*************************************************************************************************************\n")
def PQ():

    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}%...]".format(P))
    start_timeR = time.time()
    SurReseau = pacquetSurReseau(P)
    print("Fait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
    print("[Traitement des paquets ...]\n")
    
    if SurReseau==[]:
        print ('Slice non utilisée')
    else:
        start_timeR = time.time()
        tempsTraitementPacquetIndividus=[]
        tempsTraitementPacquetSurleReseau=0
        pacNtraité2=[]
        pacNtraité3=[]
        hp =[]
        mp = []
        lw =[]
        
        for i in SurReseau:
            if i[0]==1:
            
                start_timeI = time.time()
                traité = traitement(i)
                traité.append('requete traité')
                hp.append(traité)
                tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
                
            elif i[0]==2:
                pacNtraité2.append(i)
            else: 
                pacNtraité3.append(i)
        if tempsTraitementPacquetIndividus !=[]:
            thpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: thpm=0
        tempsTraitementPacquetIndividus=[]
        
        for i in pacNtraité2:
            
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            mp.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            i=[]
        
        if tempsTraitementPacquetIndividus !=[]:
            tmpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tmpm=0
        tempsTraitementPacquetIndividus=[]
        
        for i in pacNtraité3:
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            lw.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
        
        if tempsTraitementPacquetIndividus !=[]:
            tlpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tlpm=0
        
        tempsTraitementPacquetSurleReseau= time.time()-start_timeR 
        '''print(hp, len(hp))
        print("\n")
        print(mp,len(mp))
        print("\n")
        print(lw,len(lw))'''
        if len(tempsTraitementPacquetIndividus)==0:
            temp=0
        else:
            temp=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus)
        print('\n méthode PQ')
        print("Paquets haute priorités: {} \ntemps de traitement moyen d'un pacquet haute priorité: {}\n".format(len(hp),thpm))
        print("Paquets moyenne priorité: {} \ntemps de traitement moyen d'un pacquet moyenne priorité: {}\n".format(len(mp),tmpm))
        print("Paquets basse priorité: {} \ntemps de traitement moyen d'un pacquet basse priorité: {}\n".format(len(lw),tlpm))
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau)
        # print("\n*************************************************************************************************************\n")
def WFQ():

    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}%...]".format(P))
    start_timeR = time.time()
    SurReseau = pacquetSurReseau(P)
    print("Fait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
    print("[Traitement des paquets ...]\n")
    
    if SurReseau==[]:
        print ('Slice non utilisée')
    else:
        start_timeR = time.time()
        tempsTraitementPacquetIndividus=[]
        tempsTraitementPacquetSurleReseau=0
        pacNtraité2=[]
        pacNtraité3=[]
        C1 =[]
        C2 = []
        C3 =[]
        
        for i in SurReseau:
            
            if i[-1]>=90:
            
                start_timeI = time.time()
                traité = traitement(i)
                traité.append('requete traité')
                C1.append(traité)
                tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
                
            elif i[-1]>=70 and i[-1]<90:
                pacNtraité2.append(i)
            elif i[-1]<70: 
                pacNtraité3.append(i)
        
        # print(C1)
        # print("\n")
        # print(pacNtraité2)
        # print("\n")
        # print(pacNtraité3)
        
        if tempsTraitementPacquetIndividus !=[]:
            tc1m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc1m=0
        tempsTraitementPacquetIndividus=[]
        
        for i in pacNtraité2:
            
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            C2.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
        i=[]
        
        if tempsTraitementPacquetIndividus !=[]:
            tc2m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc2m=0
        tempsTraitementPacquetIndividus=[]
        
        for i in pacNtraité3:
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            C3.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
        
        if tempsTraitementPacquetIndividus !=[]:
            tc3m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc3m=0
        
        tempsTraitementPacquetSurleReseau= time.time()-start_timeR 
        
        # print(C1)
        # print("\n")
        # print(C2)
        # print("\n")
        if len(tempsTraitementPacquetIndividus)==0:
            temp=0
        else:
            temp=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus)
        # print(tempsTraitementPacquetIndividus)
        
        print('\nméthode WFQ')
        print("Nombre de paquets de la classe 1 (valeurDernièreColonnePaquet > 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 1 en second: {}\n".format(len(C1),tc1m))
        print("Nombre de paquets de la classe 2 (70 <valeurDernièreColonnePaquet <= 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 2 en second: {}\n".format(len(C2),tc2m))
        print("Nombre de paquets de la classe 3 (valeurDernièreColonnePaquet <= 70): {}\nTemps de traitement moyen d'un paquet de la bande passante 3 en second: {}\n".format(len(C3),tc3m)) 
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau) 
        print("*************************************************************************************************************\n")

def ordonnancement():
    subprocess.call(["C:/Program Files/Python35/python.exe", "C:/Users/admin-14697/Documents/FILE ROUGE/FIFO.py"]) #premier arrivé premier servi
    subprocess.call(["C:/Program Files/Python35/python.exe", "C:/Users/admin-14697/Documents/FILE ROUGE/PQ.py"]) #ordre de priorité
    subprocess.call(["C:/Program Files/Python35/python.exe", "C:/Users/admin-14697/Documents/FILE ROUGE/WFQ.py"]) #bande passante

# *********************************************************************************************************************************************
#Phase 2

def repartiteurSlice(surReseau):
    slice1, slice2, slice3 = [],[],[]
    for i in surReseau:
        if i[1] == 1: slice1.append(i)
        elif i[1] == 2: slice2.append(i)
        else: slice3.append(i)
    
    return [slice1, slice2, slice3]

def ordonnancementSurSlice(surReseau):
    slices = repartiteurSlice(surReseau)
    #print(slices)
    for slicee in slices:
        print("*************************************************************************************************************\n")
        print("traitement slice service {}: {} utilisateurs\n".format(slices.index(slicee)+1,len(slicee)))
        ordonnancement(slicee)

# *********************************************************************************************************************************************

#Phase 3 

s=0
h=0

def preditNombreUserRéseau(Jour_de_la_Semaine,Heure):
    global s,h 
    return Jour_de_la_Semaine*s + Heure*h
    
def predict_all(Jour_de_la_Semaine, Heure):
    predicted_nbUser = []
    for n in range(0, len(Y)):
        predicted_nbUser.append(preditNombreUserRéseau(Jour_de_la_Semaine[n], Heure[n]))
    return predicted_nbUser

def IAPrediction():
    global s,h
    df= pd.read_csv('datasetPrevisionNombrePaquet.csv')

    Y=df['Nombre_de_Paquets']
    X = df[['Jour_de_la_Semaine','Heure']]

    scale = StandardScaler()
    X_scaled = scale.fit_transform(X[['Jour_de_la_Semaine', 'Heure']])
    nbreUserPrédit = sm.OLS(Y, X).fit()
    # print (nbreUserPrédit.summary())
    '''
    print('Parameters: ', nbreUserPrédit.params)
    print('R2: ', nbreUserPrédit.rsquared)
    '''
    s = nbreUserPrédit.params[0]
    h = nbreUserPrédit.params[1]
    '''fig = plt.figure()
    ax = fig.add_subplot(1,1,1, projection='3d')
    ax.scatter(df["Jour_de_la_Semaine"], df["Heure"], df["Nombre_de_Paquets"], c='r')
     
    ax.set_xlabel('Jour_de_la_Semaine')
    ax.set_ylabel('Heure')
    ax.set_zlabel("Nbre d'utilisateur")
     
    ax = fig.add_subplot(3, 3, 3, projection='3d')
     
    ax.plot_trisurf(df["Jour_de_la_Semaine"], df["Heure"], predict_all(df["Jour_de_la_Semaine"], df["Heure"]))

    plt.show()'''

    semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    heure= [str(i)+'h' for i in range(1,25)]

    jourSemaine= input('\nEntrez le jour de la semaine :')
    jourSemaine= jourSemaine.lower()
    while jourSemaine not in semaine:
        jourSemaine= input('les jours de la semaines sont: "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche".\nEntrez le jour de la semaine: ')
        jourSemaine= jourSemaine.lower()   

    heur= input("Entrez maintenant l'heure d'affluence compris entre 0 et 24h (ex: 13h): ") 
    while heur not in heure: 
        heur= input("Entrez maintenant l'heure d'affluence compris entre 0 et 24h (ex: 13h): ")
        
    print("\nVous souhaitez estimer le nombre d'utilisateurs sur le réseau un {} à {}.\n\n[Analyse en cours...]".format(jourSemaine, heur))

    Hr = int(heur.split('h')[0])
    JourSemaine=semaine.index(jourSemaine)+1 
    
    pred = int(preditNombreUserRéseau(JourSemaine,Hr))
    preci = int((nbreUserPrédit.rsquared)*100)
    print("\nJe prédis approximativement {} sur le réseau un {} à {} avec une précision de {}%.".format(pred,jourSemaine,heur,preci))        
    
    return pred
# *************************************************************** MAIN Dimensionnement ***************************************************************    
'''
print("\n[Dimensionnement du réseau...]\n")   
NB = int(input("Entrer le nombre d'utilisateurs: "))
print("\n[Génération de data set de {} utilisateurs...]".format(NB))
start_timeR = time.time()
#génèrePacquetPopulation(NB)
print("\nFait en: ", time.time()-start_timeR, 's\n')
#génèreDataPrévision()
'''
# *************************************************************** MAIN 1 Phase 1 ***************************************************************    

print("\n[Dimensionnement du réseau...]\n")   
print("On souhaite traiter un paquets en 2 µs ou moins lorsque le réseau est chargé à 20% ou moins ")
print("On souhaite traiter un paquets haute priorité en 2 µs ou moins lorsque le réseau est chargé à en 20 et 50%")
print("On souhaite traiter un paquets en 2 µs ou moins lorsque le réseau est chargé à plus 50%")

print("Phase 1: [Modélisation du réseau 4G...]\n") 
print("[Chargement du réseau...]\n") 
P = float(input("Entrez le pourcentage de chargenment du réseau: "))
print("\n[chargement du réseau à {}%...\nVeuillez patienter...]".format(P))
#start_timeR = time.time()
with open("pourcentage.txt","w") as file:
    file.write(str(P))
    
#SurReseau = pacquetSurReseau(P)
# print(SurReseau)
ordonnancement()
# [Analyse des résultats...]
# quel algo adapté pour que nombre de d'utilisateurs (plage)? 
# réseau chargé à 20%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 50%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 80% ou plus:
  # temps de traitement paquets + algo d'ordonnancement
'''  
# *************************************************************** MAIN 2 phase 2 ***************************************************************    
print("*************************************************************************************************************\n")
print("\n[Phase 2: Modélisation du réseau 5G...]\n")   
start_timeR = time.time()
print("\n[recupération des paramètres du dimentionnement précédent...]\nNombre d'utilisateurs: {}".format(NB))
print("\nFait en: ", time.time()-start_timeR, 's\n')

print("\n[Chargement du réseau...]\n") 
P = int(input("Entrez le pourcentage de chargenment du réseau: "))
print("\n[chargement du réseau à {}%...]".format(P))
start_timeR = time.time()
SurReseau = pacquetSurReseau(P,population)
print("\nFait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
print("[Traitement des paquets ...]\n")
ordonnancementSurSlice(SurReseau)
[Analyse des résultats...]
# quel algo adapté pour que nombre de d'utilisateurs (plage)? 
# réseau chargé à 20%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 50%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 80% ou plus:
  # temps de traitement paquets + algo d'ordonnancement
  
# *********************************************************************************************************************************************  
      
# *************************************************************** MAIN 3 phase 3 ***************************************************************    
start_timeR = time.time()
["Estimation du nombre de paquets sur le réseau...\n"]
SurReseau=IAPrediction()
print("\nFait en {} seconds".format(time.time()-start_timeR))

#print("Nous nous situerons à priori donc dans la plage {}. l'algorithme le plus optimal serait : {}.".format(plage,algorithme)) 
'''    
    