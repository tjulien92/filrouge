import random
import time
import csv
import numpy as np

def pacquetSurReseau(poucentage):    
    # alpha= int(poucentage*1000000)
    alpha= int(poucentage*1000000)

    check=0
    SurReseau=[] 
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
            break
    return SurReseau

def traitement(pacquet):
    i=[pacquet[0],pacquet[1]]
    liste = sorted(pacquet[2:])
    liste.append(sum(liste))
    return i+liste
    
    
def PQ():

    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}% pour l'application de la méthode PQ...]".format(P))
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
    
    pacNtraité2=[]
    pacNtraité3=[]
    hp =[]
    mp = []
    lw =[]
    SurReseau =[]    
        


PQ()