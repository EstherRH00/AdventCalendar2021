import util

def heuristic(coordenada, midaX, midaY):
    return midaX - coordenada[1] + midaY - coordenada[0]

def getSuccessors(coordenada, midaX, midaY):
    llista = []
    if coordenada[0] > 0:
        llista.append((coordenada[0]-1, coordenada[1]))
    if coordenada[1] > 0:
        llista.append((coordenada[0], coordenada[1]-1))
    if coordenada[0] < midaY-1:
        llista.append((coordenada[0] + 1, coordenada[1]))
    if coordenada[1] < midaX-1:
        llista.append((coordenada[0], coordenada[1] + 1))
    return llista

def allargar(linia):
    retorn = []
    for i in range(5):
        tmp = []
        for j in linia:
            num = (i+j)%9
            if num == 0: num = 9
            tmp.append(num)
        for num in tmp:
            retorn.append(num)
    return retorn

f = open('input','r')
lines = f.readlines()
f.close()

lines = [[int(i) for i in linia if i != "\n"] for linia in lines]


matLlarga = []
for linia in lines:
    aux = allargar(linia)
    matLlarga.append(aux)

matRes = matLlarga[:]
for i in range(1, 5):
    for linia in matLlarga:
        tmp = []
        for j in linia:
            num = (i + j) % 9
            if num == 0: num = 9
            tmp.append(num)
        matRes.append(tmp)
lines= matRes
maxY = len(lines)
maxX = len(lines[0])
print(maxX, maxY)
#recorda que les coordenades son lines[i][j] amb i la fila(Y) i j la columna(X)

frontera = util.PriorityQueue()  # contindra elements ((node, cost), f(n))
explorats = {}  # contindra elements (node:costAcumulat))

nodeActual = ((0,0), 0)
explorats[nodeActual[0]] = 0
frontera.push(nodeActual, heuristic(nodeActual[0], maxX, maxY))
cost = 0

while not frontera.isEmpty() and cost == 0:
    #Extraiem el node
    nodeActual = frontera.pop() #(node, direccio, cost)

    if (nodeActual[0] == (maxY-1, maxX-1)):
        cost = nodeActual[1]

    successors = getSuccessors(nodeActual[0], maxX, maxY) #node
    for successor in successors:
        nodeFill = (successor, nodeActual[1] + lines[successor[0]][successor[1]])
        if (successor not in explorats.keys()) or (explorats[successor] > nodeFill[1]):

            explorats[successor] = nodeFill[1]
            frontera.push(nodeFill, nodeFill[1] + heuristic(successor, maxX, maxY))

print(cost)