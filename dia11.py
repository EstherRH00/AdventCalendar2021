def hiHa10(taulell):
    deus = []
    for i in range(len(taulell)):
        for j in range(len(taulell[i])):
            if taulell[i][j] >= 10:
                deus.append((i, j))
    return deus

def totZeros(taulell):
    trobat =False
    i = 0
    while(i < len(taulell) and not trobat):
        j = 0
        while(j < len(taulell) and not trobat):
            if(taulell[i][j] != 0):
                trobat = True
            else:
                j+=1
        i+=1
    return not trobat

def posar0(taulell):
    for i in range(len(taulell)):
        for j in range(len(taulell[i])):
            if taulell[i][j] == -1:
                taulell[i][j] = 0
    return taulell

def brilla(taulell, x , y):
    taulell[x][y] = -1
    #fila de sobre
    if x != 0:
        if taulell[x-1][y] != -1: taulell[x-1][y]+=1
        if y!= 0:
            if taulell[x - 1][y-1] != -1: taulell[x - 1][y-1] += 1
        if y != len(taulell)-1:
            if taulell[x - 1][y+1] != -1: taulell[x - 1][y+1] += 1
    #fila de sota
    if x != len(taulell)-1:
        if taulell[x+1][y] != -1: taulell[x+1][y]+=1
        if y!= 0:
            if taulell[x + 1][y-1] != -1: taulell[x + 1][y-1] += 1
        if y != len(taulell)-1:
            if taulell[x + 1][y+1] != -1: taulell[x + 1][y+1] += 1
    #la de la esquerra
    if y != 0:
        if taulell[x][y - 1] != -1: taulell[x][y - 1] += 1
    #la de la dreta
    if y != len(taulell)-1:
        if taulell[x][y + 1] != -1: taulell[x][y + 1] += 1
    return taulell

f = open('input','r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = [int(j) for j in lines[i] if j!= '\n']


steps = 100
flashes = 0
fi = False
i = 0
while not fi :
    #incrementar en un cada pos de la grid
    for j in range(len(lines)):
        for k in range(len(lines[0])):
            lines[j][k] += 1

    #print("incremento", lines)
    #Cada un que estigui a 10 flashea, i el poso a -1
    #Quan fa flash, incrementa en 1 el del seu voltant
    deus = hiHa10(lines)
    while(len(deus) != 0):
        for pos in deus:
            lines = brilla(lines, pos[0], pos[1])
            flashes += 1
            #print("ha brillat", pos, lines)
        deus = hiHa10(lines)
    lines = posar0(lines)
    if(totZeros(lines)):
        print("tots alhora", i+1)
        fi = True

    i+= 1


print(flashes)