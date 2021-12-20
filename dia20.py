import numpy as np

def numero(matriu):
    num = ""
    for fila in matriu:
        for n in fila:
            num += str(n)
    return(int(num, 2))

def itera(matriu, chuleta, acabara):
    trad = {".": 0, "#": 1}
    retorn = matriu.copy()
    mides = matriu.shape
    for i in range(1,mides[0]-1):
        for j in range(1, mides[1]-1):
            submatriu = matriu[i-1:i+2,j-1:j+2]
            #Agafar numero
            num = numero(submatriu)
            retorn[i,j]=trad[chuleta[num]]
    ##Actualitzar la corona
    for i in range(mides[0]):
        if i == 0 or i == mides[0]-1:
            for j in range(mides[1]):
                retorn[i,j] = acabara
        else:
            retorn[i,0]=acabara
            retorn[i, mides[1]-1]= acabara
    return retorn

f = open('input','r')
lines = f.readlines()
f.close()

trad = {".":0,"#":1}

chuleta = lines[0][:len(lines[0])-1]
mida = len(chuleta)
senars = trad[chuleta[0]]
if(senars == 0):
    parells = 0
else:
    parells = trad[chuleta[mida-1]]
print(parells, senars)
matriu = []

for i in range(2,len(lines)):
    linia = lines[i]
    aux = []
    for caracter in linia:
        if caracter != "\n":
            aux.append(trad[caracter])
    matriu.append(aux)

iteracions = 50
for i in range(iteracions):
    if(i%2==0):
        matriu = np.pad(matriu,2,'constant',constant_values=parells)
        matriu = itera(matriu, chuleta, senars)
    else:
        matriu = np.pad(matriu, 2, 'constant', constant_values=senars)
        matriu = itera(matriu, chuleta, parells)


print(np.count_nonzero(matriu))


'''
#CHULETA
a = [[1,2],[2,3]]
a = "1 2; 2 3"
m = np.matrix(a)
print(m)
m = np.pad(m,2,'constant',constant_values=1)
print(m)
print(int("0101", 2))
'''