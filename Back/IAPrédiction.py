import pandas as pd, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

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
def preditNombreUserRéseau(Jour_de_la_Semaine,Heure):
    global s,h 
    return Jour_de_la_Semaine*s + Heure*h
    
def predict_all(Jour_de_la_Semaine, Heure):
    predicted_nbUser = []
    for n in range(0, len(Y)):
        predicted_nbUser.append(preditNombreUserRéseau(Jour_de_la_Semaine[n], Heure[n]))
    return predicted_nbUser

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
print("\nJe prédis approximativement {} sur le réseau un {} à {} avec une précision de {}%.".format(int(preditNombreUserRéseau(JourSemaine,Hr)),jourSemaine,heur,int((nbreUserPrédit.rsquared)*100)))        