def trobaBasin(mapa, lowPoint):
    i, j = lowPoint[0], lowPoint[1]
    mapa[i][j] = 9
    val = 1
    visitar = []
    if i != 0 and mapa[i-1][j] != 9:
        mapa, aux = trobaBasin(mapa, (i-1, j))
        val += aux

    if i != maxI and mapa[i+1][j] != 9:
        mapa, aux = trobaBasin(mapa, (i+1, j))
        val += aux

    if j != 0 and mapa[i][j-1] != 9:
        mapa, aux = trobaBasin(mapa, (i, j-1))
        val += aux
    if j != maxJ and mapa[i][j+1] != 9:
        mapa, aux = trobaBasin(mapa, (i, j+1))
        val += aux

    return mapa, val


f = open('input','r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = [int(j) for j in lines[i] if j != '\n']

maxI = len(lines)-1
maxJ = len(lines[0])-1
lowPoints = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        actual = lines[i][j]
        if i == 0:
            if j == 0:
                if(lines[i+1][j] > actual and lines[i][j+1] > actual):
                    lowPoints.append((i,j))
            elif j == maxJ:
                if(lines[i+1][j] > actual and lines[i][j-1] > actual):
                    lowPoints.append((i,j))
            else:
                if (lines[i + 1][j] > actual and lines[i][j - 1] > actual and lines[i][j+1] > actual):
                    lowPoints.append((i,j))
        elif i == maxI:
            if j == 0:
                if(lines[i-1][j] > actual and lines[i][j+1] > actual):
                    lowPoints.append((i,j))
            elif j == maxJ:
                if(lines[i-1][j] > actual and lines[i][j-1] > actual):
                    lowPoints.append((i,j))
            else:
                if (lines[i - 1][j] > actual and lines[i][j - 1] > actual and lines[i][j+1] > actual):
                    lowPoints.append((i,j))
        elif j == 0:
            if (lines[i - 1][j] > actual and lines[i+1][j] > actual and lines[i][j + 1] > actual):
                lowPoints.append((i,j))
        elif j == maxJ:
            if (lines[i - 1][j] > actual and lines[i+1][j] > actual and lines[i][j - 1] > actual):
                lowPoints.append((i,j))
        else:
            if (lines[i - 1][j] > actual and lines[i+1][j] > actual and lines[i][j - 1] > actual and lines[i][j+1] > actual):
                lowPoints.append((i,j))


maxims = [0,0,0]
for punt in lowPoints:
    lines, aux = trobaBasin(lines, punt)
    maxims.sort()
    if aux > maxims[0]:
        maxims[0] = aux

res = 1
for numero in maxims:
    res  = res * numero
print(res)
