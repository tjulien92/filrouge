import random
import time
import numpy as np

# *********************************************************************************************************************************************

#Phase 1


def génèrePacquetPopulation(NbUtilisateur):
    population = []
    # classe=[128,64,32]
    for i in range(NbUtilisateur):
        pacquet =[]
        pacquet = [random.randint(0,100) for i in range(6)]
        pacquet[0]=random.randint(1,3)
        pacquet[1]=random.randint(1,3)
        population.append(pacquet)
    return population
    
def pacquetSurReseau(poucentage,population):
    alpha= poucentage*len(population)/100
    alpha=int(alpha)
    SurReseau = [population[i] for i in range(alpha)]
    # print(SurReseau)
    return SurReseau
    
def traitement(pacquet):
    i=[pacquet[0],pacquet[1]]
    liste = sorted(pacquet[2:])
    liste.append(sum(liste))
    return i+liste
    
def FIFO(SurReseau):
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
        print('\n*****************************************************FIFO*****************************************************\n')
        print("temps de traitement moyen d'un pacquet: ", sum(tempsTraitementPacquetIndividus)/len(tempsTraitementPacquetIndividus))
        print("temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau)
        print("\n*************************************************************************************************************\n")

def PQ(SurReseau):
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
        print('\n*****************************************************PQ*****************************************************\n')
        print("Paquet haute priorité: {} \ntemps de traitement moyen d'un pacquet haute priorité: {}\n".format(len(hp),thpm))
        print("Paquet moyenne priorité: {} \ntemps de traitement moyen d'un pacquet moyenne priorité: {}\n".format(len(mp),tmpm))
        print("Paquet basse priorité: {} \ntemps de traitement moyen d'un pacquet basse priorité: {}\n".format(len(lw),tlpm))
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau)
        print("\n*************************************************************************************************************\n")

def WFQ(SurReseau):
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
        
        print('\n*****************************************************WFQ*****************************************************\n')
        print("Nombre de paquets de la classe 1 (valeurDernièreColonnePaquet > 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 1 en second: {}\n".format(len(C1),tc1m))
        print("Nombre de paquets de la classe 2 (70 <valeurDernièreColonnePaquet <= 90): {}.\nTemps de traitement moyen d'un paquet de la bande passante 2 en second: {}\n".format(len(C2),tc2m))
        print("Nombre de paquets de la classe 3 (valeurDernièreColonnePaquet <= 70): {}\nTemps de traitement moyen d'un paquet de la bande passante 3 en second: {}\n".format(len(C3),tc3m)) 
        print("Temps de traitement de tout les pacquets: ",tempsTraitementPacquetSurleReseau) 
        print("\n*************************************************************************************************************\n")

def ordonnancement(SurReseau):
    FIFO(SurReseau) #premier arrivé premier servi
    PQ(SurReseau) #ordre de priorité
    WFQ(SurReseau) #bande passante
    
# *************************************************************** MAIN 1 phase 1 ***************************************************************    

print("\n[Dimensionnement du réseau...]\n")   
NB = int(input("Entrer le nombre d'utilisateurs: "))
print("\n[Génération de data set de {} utilisateurs...]".format(NB))
start_timeR = time.time()
population = génèrePacquetPopulation(NB)
print("\nFait en: ", time.time()-start_timeR, 's\n')

print("Phase 1: [Modélisation du réseau 4G...]\n") 
print("\n[Chargement du réseau...]\n") 
P = int(input("Entrez le pourcentage de chargenment du réseau: "))
print("\n[chargement du réseau à {}%...]".format(P))
start_timeR = time.time()
SurReseau = pacquetSurReseau(P,population)
# print(SurReseau)
print("\nFait en: ", time.time()-start_timeR, 's\n{} paquets sur le réseau.\n'.format(len(SurReseau)))
print("[Traitement des paquets ...]\n")
ordonnancement(SurReseau)

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
# *********************************************************************************************************************************************  
    
    
    
    
    