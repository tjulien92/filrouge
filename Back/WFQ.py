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
    

def WFQ():

    with open("pourcentage.txt","r") as file:
        P=float(file.read())
    print("\n[chargement du réseau à {}% pour l'application de la méthode WFQ...]".format(P))
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
    
    pacNtraité2=[]
    pacNtraité3=[]
    C1 =[]
    C2 = []
    C3 =[]
    SurReseau =[]
WFQ()