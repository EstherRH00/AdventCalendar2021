f = open('input','r')
lines = f.readlines()
f.close()

coords = []
instruccions = []
maxX = 655*2
maxY = 447*2
co = True

for linia in lines:
    if linia == "\n": co = False
    if co:
        aux = [int(i) for i in linia.split(",")]
        coords.append(aux)
        if aux[0] > maxX: maxX = aux[0]
        if aux[1] > maxY: maxY = aux[1]
    else:
        if(len(linia) != 1):
            instruccions.append(linia[:len(linia)-1])
print(maxX, maxY)
for instruccio in instruccions:
    fer = instruccio.split("=")
    lletra = fer[0][len(fer[0])-1]
    num = int(fer[1])
    print(lletra, num)
    resultat = []

    if(lletra == "x"):
        for coordenada in coords:
            if coordenada[0] > num:
                aux = [maxX - coordenada[0], coordenada[1]]
                if aux not in resultat:
                    resultat.append(aux)
            elif coordenada not in resultat and coordenada[0] != num:
                resultat.append(coordenada)
        maxX = num-1
    else:
        for coordenada in coords:
            if coordenada[1] > num:
                aux = [coordenada[0], maxY - coordenada[1]]
                if aux not in resultat:
                    resultat.append(aux)
            elif coordenada not in resultat and coordenada[1] != num:
                resultat.append(coordenada)
        maxY = num-1
    print(maxX, maxY)
    coords = resultat

mat = []
for i in range(maxY+1):
    fila = [" "]*(maxX+1)
    mat.append(fila)

for coordenada in coords:
    mat[coordenada[1]][coordenada[0]] = "#"

for fila in mat:
    for element in fila:
        print(element, end="")
    print()