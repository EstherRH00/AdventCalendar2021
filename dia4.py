def metodePrincipal():
    f = open('input', 'r')
    lines = f.readlines()
    f.close()

    numeros = lines[0]
    numeros = numeros.split(",")
    numeros = [int(j) for j in numeros if j != ' ' and j != '\n' and j != '']
    boards=[]

    taulell = []
    i = 2
    cont = 0
    while i < len(lines):
        linia = lines[i].split(" ")
        linia = [int(j) for j in linia if j != ' ' and j != '\n' and j != '']
        taulell.append(linia)
        i+=1
        cont += 1
        if(cont%5==0):
            boards.append(taulell)
            taulell = []
            i+=1
            cont = 0

    aux = []
    for numero in numeros:
        print(numero)
        i = 0
        tmp = []
        while i < (len(boards)):
            tablero = boards[i]
            boards[i] = marcar(numero, tablero)
            if (not isSolved(boards[i])):
                tmp.append(boards[i])
            i+=1

        if( len(tmp) == 0):
            return numero, boards
        boards = tmp
        print(boards)


def marcar(numero, tablero):
    #print(tablero, numero)
    for i in range(5):
        for j in range(5):
            #print(tablero[i][j], tablero[i][j] == numero)
            if tablero[i][j] == numero:
                tablero[i][j] = -1
    return tablero

def isSolved(tablero):
    for i in range(5):
        if(tablero[i][0] == tablero[i][1] == tablero[i][2] == tablero[i][3] == tablero[i][4] == -1):
            return True
        if(tablero[0][i] ==tablero[1][i] ==tablero[2][i] ==tablero[3][i] ==tablero[4][i] ==-1):
            return True
    return False


cantat, taulell= metodePrincipal()
print(cantat, taulell)
taulell = taulell[0]
suma = 0
for fila in taulell:
    for numero in fila:
        if numero != -1:
            suma += numero

print(suma, cantat, cantat*suma)