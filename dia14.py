f = open('input_smol','r')
lines = f.readlines()
f.close()

cadena = lines[0][:len(lines[0])-1]
inserts = {}

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

#print(cadena)
#print(inserts)

iteracions = 10
for i in range(iteracions):
    aux = ""
    for j in range(len(cadena)-1):
        aux += cadena[j]
        parella=cadena[j]+cadena[j+1]
        try:
            aux += inserts[parella]
        except:
            pass
    aux += cadena[len(cadena)-1]
    cadena = aux
    #print("fi de la iteracio ", i+1 , cadena)

for lletra in lletresDiferents:
    lletresDiferents[lletra] = cadena.count(lletra)
print(lletresDiferents)
print(max(lletresDiferents.values())-min(lletresDiferents.values()))
