f = open('input','r')
lines = f.readlines()
f.close()

lines = lines[0].split(",")
lines = [int(i) for i in lines]
diccionari = {}
for i in range(9):
    diccionari[i] = 0

dies = 256
for num in lines:
    diccionari[num] = diccionari[num] + 1

print("inici", diccionari)

for j in range(dies):
    diccionari_aux = {}
    for i in range(9):
        diccionari_aux[i] = 0
    for clau in diccionari.keys():
        if(clau == 0):
            diccionari_aux[6] = diccionari[0]
            diccionari_aux[8] = diccionari[0]
        else:
            diccionari_aux[clau -1] = diccionari_aux[clau -1] + diccionari[clau]

    diccionari = diccionari_aux
    #print("Dia", j+1, diccionari)
contador = 0
for valor in diccionari.values():
    contador+= valor
print(contador)