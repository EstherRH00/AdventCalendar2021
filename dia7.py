f = open('input','r')
lines = f.readlines()
f.close()

lines = lines[0].split(",")
lines = [int(i) for i in lines]

rang = max(lines)

cost = float('inf')
pos = None
for i in range(rang+1):
    costAux = 0
    for numero in lines:
        aux = abs(numero - i)
        costAux += ((aux)*(aux+1))/2
    #print(i, costAux)
    if(costAux  < cost):
        cost = costAux
        pos = i
print(cost, pos)