import random
import time
import csv
import numpy as np

import pandas as pd, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
import sqlite3
from prettytable import PrettyTable

tmq,ttp,tms, nphp = None, None,None,None
tmqhp, ttphp, tmshp, npmp = None, None,None,None
tmqmp, ttpmp, tmsmp, nplp = None, None,None,None 
tmqlp, ttplp, tmslp, npb1 = None, None,None,None 
tmqb1, ttpb1, tmsb1, npb2 = None, None,None,None
tmqb2, ttpb2, tmsb2, npb3 = None, None,None,None
tmqb3, ttpb3, tmsb3 = None, None, None

debit, taux_perte, lat, debithp = None, None,None,None
taux_pertehp, lathp, debitmp, taux_pertemp = None, None,None,None
latmp, debitbp, taux_pertebp, latbp, debitC1    = None, None,None,None, None
taux_perteC1, latC1, debitC2, taux_perteC2 = None, None,None,None
latC2, debitC3, taux_perteC3, latC3 = None, None,None,None

def printing(y, slicee,i, debit, taux_perte, lat, debithp, taux_pertehp, lathp, debitmp, taux_pertemp, latmp, debitbp, taux_pertebp, latbp, debitC1, taux_perteC1, latC1, debitC2, taux_perteC2, latC2, debitC3, taux_perteC3, latC3):
    
    y.field_names = ["Slice","Discipline", "Priorité", "debit en kb/s", "taux de perte en %", "latence réseau en s"]
    y.add_row(["Service " + str(i+1), "FIFO", "NEANT", debit , taux_perte, lat])
    y.add_row([" ", " ", " ", " ", " ", " "])
    y.add_row([" ", "PQ", "HAUTE", debithp , taux_pertehp, lathp])
    y.add_row([" ", " ", "MOYENNE", debitmp , taux_pertemp, latmp])
    y.add_row([" ", " ", "BASSE", debitbp , taux_pertebp, latbp])
    y.add_row([" ", " ", " ", " ", " ", " "])
    y.add_row([" ", "WFQ", "BANDE PASSANTE 1", debitC1 , taux_perteC1, latC1])
    y.add_row([" ", " ", "BANDE PASSANTE 2", debitC2 , taux_perteC2, latC2])
    y.add_row([" ", " ", "BANDE PASSANTE 3", debitC3 , taux_perteC3, latC3])
    y.add_row([" ", " ", " ", " ", " ", " "])
    y.add_row([" ", " ", " ", " ", " ", " "])
  
def affiche(x,slicee,i,P,SurReseau,tmq,ttp,tms, nphp,tmqhp, ttphp, tmshp, npmp,tmqmp, ttpmp, tmsmp, nplp, tmqlp, ttplp, tmslp, npb1, tmqb1, ttpb1, tmsb1, npb2, tmqb2, ttpb2, tmsb2, npb3, tmqb3, ttpb3, tmsb3):
    
    
    x.field_names = ["Chargmnt_Réseau", "Nb_de_paquet_sur_réseau", "Slice", "Nb_paquet", "Discipline", "Priorité", "Taille_FA", "Temps_moyen_FA en s","Temps_traitm_paquet en s", "Temps_traitm_moyen_sys en s"]
    x.add_row([str(P)+'%', len(SurReseau), "Service " + str(i+1), len(slicee), "FIFO", "NEANT",len(slicee), tmq, ttp, tms])
    x.add_row([" ", " ", " ", " ", " ", " ", " "," ", " ", " "])
    x.add_row([" ", " ", " ", " ", "PQ", "HAUTE", nphp,tmqhp, ttphp, tmshp])
    x.add_row([" ", " ", " ", " ", "PQ", "MOYENNE", npmp,tmqmp, ttpmp, tmsmp])
    x.add_row([" ", " ", " ", " ", "PQ", "BASSE", nplp, tmqlp, ttplp, tmslp])
    x.add_row([" ", " ", " ", " ", " ", " ", " "," ", " ", " "])
    x.add_row([" ", " ", " ", " ", "WFQ", "BANDE PASSANTE 1", npb1, tmqb1, ttpb1, tmsb1])
    x.add_row([" ", " ", " ", " ", "WFQ", "BANDE PASSANTE 2", npb2, tmqb2, ttpb2, tmsb2])
    x.add_row([" ", " ", " ", " ", "WFQ", "BANDE PASSANTE 3", npb3, tmqb3, ttpb3, tmsb3])
    x.add_row([" ", " ", " ", " ", " ", " ", " "," ", " ", " "])
    x.add_row([" ", " ", " ", " ", " ", " ", " "," ", " ", " "])
   
    # print(x)

def debPerte(nbpaq,ttt):
    return nbpaq/(1000*ttt),  (1 - random.randint(int(nbpaq-0.2*nbpaq),nbpaq)/nbpaq)*100

"""
def uploadDBTO(NbUtilisateur):
    baseDeDonnees = sqlite3.connect("datasetTestOrdonnancement.db")
    curseur = baseDeDonnees.cursor()
    for i in range(NbUtilisateur):
        pacquet = [random.randint(0,100) for i in range(6)]
        pacquet[0]=random.randint(1,3)#priority
        pacquet[1]=random.randint(1,3)#slicing
        curseur.execute("INSERT INTO DataOrdonnancement (Bit_1, Bit_2, Bit_3, Bit_4, Bit_5, Bit_6) VALUES (?, ?, ?, ?, ?, ?)",tuple(pacquet))
    baseDeDonnees.commit()
"""

"""
def uploadDBIA():
    baseDeDonnees = sqlite3.connect("datasetTestOrdonnancement.db")
    curseur = baseDeDonnees.cursor()
    semaine=[1,2,3,4,5,6,7]
    for i in range(3000):
        heure = time.strftime('%H', time.gmtime(random.randint(0, int(time.time()))))
        jour= random.choice(semaine)
        npac= random.randint(15000000,100000000)
        curseur.execute("INSERT INTO DataPr (Nombre_de_Paquet, JourSemaine, Heure) VALUES (?, ?, ?)",
        tuple([npac,jour,heure]))
    baseDeDonnees.commit() 
"""

def pacquetSurReseauFrmDB(poucentage):    
    alpha= int(poucentage*1000000)
    check=0
    SurReseau=[]
    baseDeDonnees = sqlite3.connect("datasetTestOrdonnancement.db")
    curseur = baseDeDonnees.cursor()
    curseur.execute("select Bit 1, Bit 2, Bit 3, Bit 4, Bit 5, Bit 6 from KNOWN_PEOPLE_DETECTED_TABLE LIMIT {} ".format(alpha))
    SurReseau= curseur.fetchall()
    '''fnames=[i[0] for i in fnames]
    reader = csv.reader(open("datasetTestOrdonnancement.csv","r"))   
    for row in reader:
        if row == ['bit 1','bit 2','bit 3','bit 4','bit 5','bit 6']:
            print('en cours de traitement...')
        elif row == []:
            pass
        else:
            SurReseau.append(list(map(int, row)))
        check+=1
        if check == alpha:
            break'''
    baseDeDonnees.commit()
    return SurReseau    
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
    
def génèreDataPrévision():
    fichier = csv.writer(open ('datasetPrevisionNombrePaquet.csv','w',newline=''))
    fichier.writerow(['Nombre_de_Paquets','Jour_de_la_Semaine','Heure'])
    #semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"] 
    semaine=[1,2,3,4,5,6,7]
    for i in range(100):
        heure = time.strftime('%H', time.gmtime(random.randint(0, int(time.time()))))
        jour= random.choice(semaine)
        npac= random.randint(1000000,100000000)
        fichier.writerow([npac,jour,heure])
    
def pacquetSurReseau(poucentage):
    
    alpha= int(poucentage*1000000)
    check=0
    SurReseau=[] 
    reader = csv.reader(open("datasetTestOrdonnancement.csv","r"))   
    for row in reader:
        if row == ['bit 1','bit 2','bit 3','bit 4','bit 5','bit 6']:
            print('[Traitement...]')
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

def FIFO(SurReseau):
    global tmq,ttp,tms, debit, taux_perte, lat
    tempsSortiFile=[]
    if SurReseau==[]:
        print ('Slice non utilisée')
    else:
        start_timeR = time.time()
        tempsTraitementPacquetIndividus=[]
        tempsTraitementPacquetSurleReseau=0
        for i in SurReseau:
            tempsSortiFile.append(time.time()- start_timeR)
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            i= traité
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            lat= time.time()- start_timeR
        tempsTraitementPacquetSurleReseau= time.time()-start_timeR
        debit, taux_perte= debPerte(len(SurReseau),tempsTraitementPacquetSurleReseau)
        lat= lat/len(SurReseau)
        
        tmq,ttp,tms = sum(tempsSortiFile)/len(tempsSortiFile), sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus),sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) + sum(tempsSortiFile)/len(tempsSortiFile)
        '''print('méthode FIFO:')
        print("Pas de priorité. Priemier arrivié, premier servi.")
        print("temps de traitement moyen d'un pacquet: ",ttp)
        print("temps moyen dans la file d'attente: ",tmq)
        print("temps de dans le système: ", tms)
        print("débit: ",debit)
        print("Taux de perte: ",taux_perte)'''  
        # print("\n*************************************************************************************************************\n")

def PQ(SurReseau):
    global nphp,tmqhp, ttphp, tmshp, npmp,tmqmp, ttpmp, tmsmp, nplp, tmqlp,  ttplp, tmslp, debithp, taux_pertehp, lathp, debitmp, taux_pertemp, latmp, debitbp, taux_pertebp, latbp
    tempsSortiFile=[]
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
                tempsSortiFile.append(time.time()- start_timeR)
                start_timeI = time.time()
                traité = traitement(i)
                traité.append('requete traité')
                hp.append(traité)
                tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
                lat= time.time()- start_timeR
            elif i[0]==2:
                pacNtraité2.append(i)
            else: 
                pacNtraité3.append(i)
        tempsTraitementPacquetSurleReseau= time.time()- start_timeR
        debithp, taux_pertehp = debPerte(len(hp),tempsTraitementPacquetSurleReseau)
        lathp=lat/len(hp)
        
        if tempsTraitementPacquetIndividus !=[]:
            thpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: thpm=0
        
        if tempsSortiFile !=[]:
            t1=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t1=0
        
        tempsTraitementPacquetIndividus=[]
        tempsSortiFile=[]
        
        for i in pacNtraité2:
            tempsSortiFile.append(time.time()- start_timeR)
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            mp.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            lat= time.time()- start_timeR
            i=[]
        
        tempsTraitementPacquetSurleReseau= time.time()- start_timeR
        debitmp, taux_pertemp = debPerte(len(pacNtraité2),tempsTraitementPacquetSurleReseau)
        
        latmp= lat/len(pacNtraité2)
        
        if tempsTraitementPacquetIndividus !=[]:
            tmpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tmpm=0
        
        if tempsSortiFile !=[]:
            t2=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t2=0
        
        tempsTraitementPacquetIndividus=[]
        tempsSortiFile=[]
        
        for i in pacNtraité3:
            tempsSortiFile.append(time.time()- start_timeR)
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            lw.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            lat= time.time()- start_timeR
            
        if tempsTraitementPacquetIndividus !=[]:
            tlpm=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tlpm=0
        
        if tempsSortiFile !=[]:
            t3=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t3=0
        
        tempsTraitementPacquetSurleReseau= time.time()- start_timeR
        debitbp, taux_pertebp = debPerte(len(pacNtraité3),tempsTraitementPacquetSurleReseau)
        latbp=lat/len(pacNtraité3)
 
        '''print(hp, len(hp))
        print("\n")
        print(mp,len(mp))
        print("\n")
        print(lw,len(lw))'''
        if len(tempsTraitementPacquetIndividus)==0:
            temp=0
        else:
            temp=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus)
        
        nphp,tmqhp, ttphp, tmshp, npmp,tmqmp, ttpmp, tmsmp, nplp, tmqlp, ttplp, tmslp = len(hp),thpm,t1, t1+thpm, len(mp),tmpm, t2, t2+ tmpm, len(lw),tlpm,t3, t3+tlpm
        '''print('\nméthode PQ')
        print("Paquets haute priorité: {} \ntemps de traitement moyen d'un pacquet haute priorité: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(hp),thpm,t1, t1+thpm))
        print("Paquets moyenne priorité: {} \ntemps de traitement moyen d'un pacquet moyenne priorité: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(mp),tmpm, t2, t2+ tmpm))
        print("Paquets basse priorité: {} \ntemps de traitement moyen d'un pacquet basse priorité: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(lw),tlpm,t3, t3+tlpm))
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau)'''
        # print("\n*************************************************************************************************************\n")

def WFQ(SurReseau):
    
    global npb1, tmqb1, ttpb1, tmsb1, npb2, tmqb2, ttpb2, tmsb2, npb3, tmqb3, ttpb3, tmsb3, debitC1, taux_perteC1, latC1, debitC2, taux_perteC2, latC2, debitC3, taux_perteC3, latC3
    tempsSortiFile=[]
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
                tempsSortiFile.append(time.time()- start_timeR)
                start_timeI = time.time()
                traité = traitement(i)
                traité.append('requete traité')
                C1.append(traité)
                tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
                lat= time.time()- start_timeR
            elif i[-1]>=70 and i[-1]<90:
                pacNtraité2.append(i)
            elif i[-1]<70: 
                pacNtraité3.append(i)

        if tempsTraitementPacquetIndividus !=[]:
            tc1m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc1m=0
        tempsTraitementPacquetIndividus=[]
        
        tempsTraitementPacquetSurleReseau= time.time()- start_timeR
        debitC1, taux_perteC1 = debPerte(len(C1),tempsTraitementPacquetSurleReseau)
        latC1= lat/len(C1)
        
        if tempsSortiFile !=[]:
            t1=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t1=0
        
        for i in pacNtraité2:
            tempsSortiFile.append(time.time()- start_timeR)
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            C2.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            lat= time.time()- start_timeR
        i=[]
        
        tempsTraitementPacquetSurleReseau= time.time()- start_timeR
        debitC2, taux_perteC2 = debPerte(len(pacNtraité2),tempsTraitementPacquetSurleReseau)
        latC2 = lat/len(pacNtraité2)
        
        if tempsTraitementPacquetIndividus !=[]:
            tc2m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc2m=0
        
        if tempsSortiFile !=[]:
            t2=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t2=0
        
        tempsTraitementPacquetIndividus=[]
        
        for i in pacNtraité3:
            tempsSortiFile.append(time.time()- start_timeR)
            start_timeI = time.time()
            traité = traitement(i)
            traité.append('requete traité')
            C3.append(traité)
            tempsTraitementPacquetIndividus.append(time.time()-start_timeI)
            lat= time.time()- start_timeR
        
        if tempsTraitementPacquetIndividus !=[]:
            tc3m=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus) 
        else: tc3m=0
        
        if tempsSortiFile !=[]:
            t3=sum(tempsSortiFile)/len(tempsSortiFile) 
        else: t3=0
        tempsTraitementPacquetSurleReseau= time.time()-start_timeR 
        debitC3, taux_perteC3 = debPerte(len(pacNtraité3),tempsTraitementPacquetSurleReseau)
        latC3=lat/len(pacNtraité3)
        # print(C1)
        # print("\n")
        # print(C2)
        # print("\n")
        if len(tempsTraitementPacquetIndividus)==0:
            temp=0
        else:
            temp=sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus)
        # print(tempsTraitementPacquetIndividus)
        npb1, tmqb1, ttpb1, tmsb1, npb2, tmqb2, ttpb2, tmsb2, npb3, tmqb3, ttpb3, tmsb3 = len(C1),tc1m,t1,t1+tc1m, len(C2),tc2m,t2,t2+tc2m, len(C3),tc3m,t3,t3+tc3m
        '''print('\nméthode WFQ')
        print("Nombre de paquets de la classe 1 (valeurDernièreColonnePaquet > 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 1 en second: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(C1),tc1m,t1,t1+tc1m))
        print("Nombre de paquets de la classe 2 (70 <valeurDernièreColonnePaquet <= 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 2 en second: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(C2),tc2m,t2,t2+tc2m))
        print("Nombre de paquets de la classe 3 (valeurDernièreColonnePaquet <= 70): {}\nTemps de traitement moyen d'un paquet de la bande passante 3 en second: {}\ntemps moyen dans la file d'attente: {}\ntemps moyen dans le système: {}".format(len(C3),tc3m,t3,t3+tc3m)) 
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau) '''
        # print("\n***************************************************************************************************************\n")

def ordonnancement(SurReseau):
    FIFO(SurReseau) #premier arrivé premier servi
    PQ(SurReseau) #ordre de priorité
    WFQ(SurReseau) #bande passante

# *********************************************************************************************************************************************
#Phase 2

def repartiteurSlice(surReseau):
    slice1, slice2, slice3 = [],[],[]
    for i in surReseau:
        if i[1] == 1: slice1.append(i)
        elif i[1] == 2: slice2.append(i)
        else: slice3.append(i)
    
    return [slice1, slice2, slice3]

x = PrettyTable()
y = PrettyTable()


def ordonnancementSurSlice(surReseau):
    global x
    start_timeR = time.time()
    slices = repartiteurSlice(surReseau)
    #print(slices)
    i=0
    for slicee in slices:
        # print("===============================================================================================================\n")
        # print("traitement slice service {}: {} utilisateurs\n".format(slices.index(slicee)+1,len(slicee)))
        ordonnancement(slicee)
        affiche(x,slicee,i,P,SurReseau,tmq,ttp,tms, nphp,tmqhp, ttphp, tmshp, npmp,tmqmp, ttpmp, tmsmp, nplp, tmqlp, ttplp, tmslp, npb1, tmqb1, ttpb1, tmsb1, npb2, tmqb2, ttpb2, tmsb2, npb3, tmqb3, ttpb3, tmsb3)
        printing(y, slicee,i, debit, taux_perte, lat, debithp, taux_pertehp, lathp, debitmp, taux_pertemp, latmp, debitbp, taux_pertebp, latbp, debitC1, taux_perteC1, latC1, debitC2, taux_perteC2, latC2, debitC3, taux_perteC3, latC3)
        i = i + 1
        
    print("traitement réalisé en: ", time.time() - start_timeR, " s")
    print("[Résultats des tests ...]\n")
    print(x)
    print("\n")
    print(y)
    return slices
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

def analyse():
        print(["Analyse des résultats..."])
        print("Les tests on été réalisés pour avec un nombre de paquets de 10, 20, et 30, 40, 50, 60, 70, et 80 millions.\n")
        print("[Analyse 4G...]\n")
        print("Pour un nombre de paquet inférieur ou égale à 30% des paquet: l'algorithme FIFO prédomine au niveau du temps de traitement d'un paquet et celui du traitement de tous les paquets.")
        print("Pour les tests sur 10, 20, 30 millions de paquets:\nSynthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 2.4 µs\nTemps de traitement total moyen des paquets: 52.4 s")
        print("\nSi on souhaite faire de la segmentation l'algorithme PQ est le plus adapté.")
        print("Synthèse méthode PQ:\nTemps de traitement moyen d'un paquet haute priorité: 1.4 µs\nTemps de traitement moyen d'un paquet moyenne priorité: 3.2 µs\nTemps de traitement moyen d'un paquet basse priorité: 5.1 µs\nTemps de traitement total des paquets: 238.5 s")
        print("Pour un nombre de paquet supérieur à 30% même si son temps de traitement total est largement supérieur à celui de FIFO, le temps de traitement de chaque paquet avec PQ est 10 fois inférieur a celui de FIFO")
        print("C'est le bon compromis entre segmentation et traitement rapide de chaque paquet")
        print("Pour les tests sur 40, 50, 60, 70 et 80 millions de paquets:\n")
        print("Synthèse méthode PQ:\nTemps de traitement moyen d'un paquet haute priorité: 0.18 µs\nTemps de traitement moyen d'un paquet moyenne priorité: 0.23 µs\nTemps de traitement moyen d'un paquet basse priorité: 1.5 µs\nTemps de traitement total des paquets: 1260 s")
        print("\nSi vous souhaitez traiter tous les paquets le plus rapidement possible, l'algorithme FIFO est le plus adapté.")
        print("Synthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 3.1 µs\nTemps de traitement total moyen des paquets: 197 s")
        print("\n[Analyse 5G...]\n")
        print("Les résultats sont pareils que sur la 4G. Ils dependent de la population.\nSeulement ici le temps de traitement de tous les paquets est ultra court du faite du principe de slicing.")
                
def selectAlgo(Nbre_pac,pourcent):
    if Nbre_pac<= 30000000:
        print("\nLes tests on été réalisés pour avec un nombre de paquets de 10, 20 et 30 millions.\nLes résultats si après sont les valeurs moyennes des résultats de ces trois jeux de données.\n")
        print("[Analyse 4G...]\n")
        print("{} utilisateurs prévus sur le réseau.\nD'après nos analyses l'algorithme FIFO serait le plus adapté pour traiter les files d'attentes.\n".format(Nbre_pac))
        print("Synthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 2.14 µs\nTemps de traitement total moyen des paquets: 52.4 s")
        print("\nSi vous souhaitez faire de la segmentation l'algorithme PQ est le plus adapté.")
        print("Synthèse méthode PQ:\nTemps de traitement moyen d'un paquet haute priorité: 1.4 µs\nTemps de traitement moyen d'un paquet moyenne priorité: 3.2 µs\nTemps de traitement moyen d'un paquet basse priorité: 5.1 µs\nTemps de traitement total des paquets: 238.5 s")
        print("\n[Analyse 5G...]\n")
        print("D'après nos analyses l'algorithme FIFO serait le plus adapté pour traiter les files d'attentes.\n")
        print("Synthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 2.5 µs\nTemps de traitement total moyen des paquets: 14 s")
        print("\nCi après les tests avec les méthodes FIFO et PQ:\n")
        FIFO(pacquetSurReseau(pourcent))
        PQ(pacquetSurReseau(pourcent))
        print("\nQuel est donc votre choix?")
        choix = input("Entrez 'FIFO' ou 'PQ': ")
        choix=choix.upper()
        while choix not in ['FIFO','PQ']:
            choix = input("Entrex 'FIFO' ou 'PQ': ")
            choix=choix.upper()
        print("Application de de l'algorithme {}".format(choix.upper()))
        print("Fait !")
    else:
        print("\nLes tests on été réalisés pour avec un nombre de paquets de 40, 50, 60 et 70 millions.\nLes résultats ci après sont les valeurs moyennes des résultats de ces quatre jeux de données.\n")

        print("[Analyse 4G...]\n")
        print("{} utilisateurs prévus sur le réseau.\nD'après nos analyses l'algorithme PQ serait le plus adapté pour traiter les files d'attentes\n".format(Nbre_pac))
        print("Synthèse méthode PQ:\nTemps de traitement moyen d'un paquet haute priorité: 0.18 µs\nTemps de traitement moyen d'un paquet moyenne priorité: 0.23 µs\nTemps de traitement moyen d'un paquet basse priorité: 1.5 µs\nTemps de traitement total des paquets: 1260 s")
        print("\nSi vous souhaitez traiter tous les paquets le plus rapidement possible, l'algorithme FIFO est le plus adapté.")
        print("Synthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 3.1 µs\nTemps de traitement total moyen des paquets: 197 s")
        print("\n[Analyse 5G...]\n")
        print("D'après nos analyses l'algorithme FIFO serait le plus adapté pour traiter les files d'attentes.\n")
        print("Synthèse méthode FIFO:\nTemps de traitement moyen d'un paquet: 2.5 µs\nTemps de traitement total moyen des paquets: 14 s")       
        print("\nCi après les tests avec les méthodes FIFO et PQ:\n")
        FIFO(pacquetSurReseau(pourcent))
        PQ(pacquetSurReseau(pourcent))
        print("\nQuel est donc votre choix?")
        choix = input("Entrez 'FIFO' ou 'PQ': ")
        choix=choix.upper()
        while choix not in ['FIFO','PQ']:
            choix = input("Entrex 'FIFO' ou 'PQ': ")
            choix=choix.upper()
        print("Application de de l'algorithme {}".format(choix.upper()))
        print("Fait !")

# *************************************************************** MAIN Dimensionnement ***************************************************************    
'''

print("\n[Dimensionnement du réseau...]\n")   
NB = int(input("Entrer le nombre d'utilisateurs: "))
print("\n[Génération de data set de {} utilisateurs...]".format(NB))
start_timeR = time.time()
#génèrePacquetPopulation(NB)
# uploadDBTO(NB)
print("\nFait en: ", time.time()-start_timeR, 's\n')
start_timeR = time.time()
# uploadDBIA()
print("\nFait en: ", time.time()-start_timeR, 's\n')
#génèreDataPrévision()

'''
# *************************************************************** MAIN 1 Phase 1 ***************************************************************    

print("===============================================================================================================")
print("==============================                            TEST                           ======================")
print("===============================================================================================================\n")
'''print("On souhaite traiter un paquet en 2 µs ou moins lorsque le réseau est chargé à 20% ou moins ")
print("On souhaite traiter un paquet haute priorité en 2 µs ou moins lorsque le réseau est chargé à en 20 et 80%")
print("On souhaite traiter un paquet haute priorité en 3 µs ou moins lorsque le réseau est chargé à plus 80%\n")
print("\n===============================================================================================================")'''
for P in [60, 70, 80]:
    print("\n[Dimensionnement du réseau...]\n") 
    #génèreDataPrévision() 
    print("[Chargement du réseau...]\n") 
    # P = float(input("Entrez le pourcentage de chargement du réseau: "))
    print("\n[chargement du réseau à {}%...]".format(P))
    start_timeR = time.time()
    SurReseau = pacquetSurReseau(P)
    print("Fait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))   
    # print("==============================   Phase 1: Modélisation du réseau 4G   =========================================\n")  
    # print("[Traitement des paquets ...]\n")
    # ordonnancement(SurReseau)
    
    # *************************************************************** MAIN 2 phase 2 ***************************************************************    
    # print("***************************************************************************************************************\n")
    print("[Phase 2: Modélisation du réseau 5G...]\n")   
    start_timeR = time.time()
    # print("[recupération des paramètres du dimensionnement précédent...]\n")
    # print("[chargement du réseau à {}%...]".format(P))
    # print("{} paquets sur le réseau.\n".format(len(SurReseau)))
    # print("Fait en: ", time.time()-start_timeR, 's\n')
    start_timeR = time.time()
    print("[Traitement des paquets ...]\n")
    slices=ordonnancementSurSlice(SurReseau)
    with open("EvaluationQoS_{}.txt".format(P),"a") as f:
        f.write(str(x))
        f.write("\n")
        f.write(str(y))
        x = PrettyTable()
        y = PrettyTable()
    print("===============================================================================================================")
    print("============================           FIN DES TESTS POUR UN Nb DE PAQUETS = {}        ========================".format(P))
    print("===============================================================================================================\n")
# print("Recap:\n")

# quel algo adapté pour que nombre de d'utilisateurs (plage)? 
# réseau chargé à 20%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 50%:
  # temps de traitement paquets + algo d'ordonnancement
# réseau chargé à 80% ou plus:
  # temps de traitement paquets + algo d'ordonnancement
  
# *********************************************************************************************************************************************  
      
# *************************************************************** MAIN 3 phase 3 ***************************************************************    
'''
analyse()
start_timeR = time.time()
print("Estimation du nombre de paquets sur le réseau par notre IA...")
P=IAPrediction()
Pourcent=P/1000000
print("\nFait en {} seconds".format(time.time()-start_timeR))
print("\n[Analyse des résultats de prédiction...]\n")
selectAlgo(P,Pourcent)
#print("Nous nous situerons à priori donc dans la plage {}. l'algorithme le plus optimal serait : {}.".format(plage,algorithme)) 
'''    
    