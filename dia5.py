f = open('input','r')
lines = f.readlines()
f.close()
diccionari = {}

#posar dades al diccionari
for linia in lines:
    n1, n2 = linia.split(" -> ")
    n1=[int(i) for i in n1.split(",")]
    n2 = [int(i) for i in n2.split(",")]
    if(n1[0] == n2[0]):
        if(n1[1] > n2[1]):
            n1, n2 = n2, n1
        for i in range(n1[1], n2[1]+1):
            if (n1[0], i) in diccionari.keys():
                diccionari[(n1[0], i)] = diccionari[(n1[0], i)] + 1
            else:
                diccionari[(n1[0], i)] = 1
    elif (n1[1] == n2[1]):
        if (n1[0] > n2[0]):
            n1, n2 = n2, n1
        for i in range(n1[0], n2[0] + 1):
            if (i, n1[1]) in diccionari.keys():
                diccionari[(i, n1[1])] = diccionari[(i, n1[1])] + 1
            else:
                diccionari[(i, n1[1])] = 1
    else:
        #print("hey")
        if (n1[0] > n2[0]):
            n1, n2 = n2, n1
        #print("n1", n1, "n2", n2)
        if(n1[1] < n2[1]):
            for i in range(n2[1] - n1[1] + 1):
                x = n1[0]+i
                y = n1[1]+i
                #print("Considero:", (x, y))
                if (x, y) in diccionari.keys():
                    diccionari[(x, y)] = diccionari[(x, y)] + 1
                else:
                    diccionari[(x, y)] = 1
        else:
            for i in range(n1[1] - n2[1] + 1):
                x = n1[0] + i
                y = n1[1] - i
                #print("Considero:", (x, y))
                if (x, y) in diccionari.keys():
                    diccionari[(x, y)] = diccionari[(x, y)] + 1
                else:
                    diccionari[(x, y)] = 1

#print(diccionari)
contador = 0
for value in diccionari.values():
    if value >= 2:
        contador+=1
print(contador)