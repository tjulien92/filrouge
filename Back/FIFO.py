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
    

def FIFO():
    
    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}% pour l'application de la méthode FIFO...]".format(P))
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
    SurReseau = []

FIFO()