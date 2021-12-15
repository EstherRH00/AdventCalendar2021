f = open('input','r')
lines = f.readlines()
f.close()

cadena = lines[0][:len(lines[0])-1]
inserts = {}
parelles = {}

lletresDiferents = {}
for lletra in cadena:
    if lletra not in lletresDiferents.keys():
        lletresDiferents[lletra] = 0

for i in range(2, len(lines)):
    linia = lines[i][:len(lines[i])-1]
    aux = linia.split(" -> ")
    inserts[aux[0]]=aux[1]
    if(aux[0][0] not in lletresDiferents):
        lletresDiferents[aux[0][0]] = 0
    if (aux[0][1] not in lletresDiferents):
        lletresDiferents[aux[0][1]] = 0
    if (aux[1] not in lletresDiferents):
        lletresDiferents[aux[1]] = 0

for i in range(len(cadena)-1):
    aux = cadena[i]+cadena[i+1]
    parelles[aux] = 1

iteracions = 40
print(parelles)
for i in range(iteracions):
    aux = parelles.copy()
    for parella in parelles.keys():
        try:
            insertar = inserts[parella]
            aux1 = parella[0]+insertar
            aux2 = insertar+parella[1]
            aux[parella] -= parelles[parella]
            if(aux1 in aux.keys()):
                aux[aux1] += parelles[parella]
            else:
                aux[aux1] = parelles[parella]
            if (aux2 in aux.keys()):
                aux[aux2] += parelles[parella]
            else:
                aux[aux2] = parelles[parella]
        except:
            pass
    parelles = aux.copy()
    #print("fi iteracio", i+1, parelles)

print(lletresDiferents)

for parella in parelles.keys():
    lletresDiferents[parella[0]] += parelles[parella]
lletresDiferents[cadena[len(cadena)-1]] += 1
#print(parelles)
#print(lletresDiferents)

print(max(lletresDiferents.values())-min(lletresDiferents.values()))
