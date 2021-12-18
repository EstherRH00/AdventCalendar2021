import ast
from itertools import combinations
def suma(n1, n2):
    return "[" + n1 + "," + n2 + "]"

def reduir(llista):
    #una parella esta dins de 4 parelles
    n = parellaDins4(llista)
    aux = True
    if( n != None):
        #print("exploto", end =" ")
        llista = explotar(llista, n)
    else:
        llista, aux = splitea10(llista)
    return llista, aux

def parellaDins4(llista):
    contador = 0
    for i in range(len(llista)):
        char = llista[i]
        if char == '[':
            contador +=1
        elif char == "]":
            contador -=1
        if contador >= 5:
            if llista[i+2] == ",":
                if llista[i + 4] == "]":
                    return (i,1,1)
                elif llista[i+5] == "]":
                    return(i,1,2)
            elif llista[i+3] == ",":
                if llista[i + 5] == "]":
                    return (i,2,1)
                elif llista[i+6] == "]":
                    return(i,2,2)
    return None

def explotar(llista, info): #index del [ precursor
    idx = info[0]
    #obtenir els nombres de la parella:
    esq = int(llista[idx+1:idx+1+info[1]])
    dre = int(llista[idx+2+info[1]: idx+2+info[1] + info[2]])
    #print(esq, dre)

    #sumar a l'esquerra
    i = idx
    trobat = False
    augment = 0
    d = 0
    while i > 0 and not trobat:
        if esNumero(llista[i]):
            aux = int(llista[i])
            if(esNumero(llista[i-1])):
                aux = int(llista[i-1:i+1])
                d = 1
            suma = aux + esq
            #print("aux", aux, "suma", suma)
            augment += len(str(suma))-len(str(aux))
            llista = llista[:i-d] + str(suma) + llista[i-d+len(str(aux)):]
            trobat = True
        i-=1
    #print("sumo1", llista)
    #sumar a la dreta
    i = idx + 3+info[1] + info[2]
    trobat = False
    while i < len(llista) and not trobat:

        if esNumero(llista[i]):
            aux = int(llista[i])
            if (esNumero(llista[i + 1])):
                aux = int(llista[i:i + 2])
            suma = aux + dre
            #augment += len(str(suma)) - len(str(aux))
            llista = llista[:i] + str(suma) + llista[i+len(str(aux)):]
            trobat = True
        i += 1
    #print("sumo2", llista)
    #canviar per un zero
    llista = llista[:idx+augment] + "0" + llista[augment+idx+3+info[1]+info[2]:]
    return llista

def splitea10(llista):
    #trobar el primer 10 o superior
    i = 0
    trobat = False
    while i < len(llista)-1 and not trobat:
        char = llista[i]
        next = llista[i+1]
        if(esNumero(char) and esNumero(next)):
            trobat = True
        else: i+=1
    if(trobat):
        num = int(llista[i:i+2])
        if(num%2 == 0):
            tupla = "["+str(num//2)+","+str(num//2)+"]"
        else:
            tupla = "["+str(num//2)+","+str((num//2)+1)+"]"
        llista = llista[:i] + tupla + llista[i+2:]
    return llista, trobat


def esNumero(char):
    return char!= "[" and char != "," and char != "]"

def calculaMagintud(llista):
    n1 = llista[0]
    n2 = llista[1]
    prod = 0
    if type(n1)==int:
        prod += 3*n1
    else:
        prod += 3*(calculaMagintud(n1))
    if type(n2)==int:
        prod += 2*n2
    else:
        prod += 2*(calculaMagintud(n2))
    return prod


f = open('input','r')
lines = f.readlines()
f.close()

res = ""
'''
for linia in lines:
    #print(linia)
    linia = linia[:len(linia)-1]
    if res == "":
        res = linia
    else:
        res = suma(res, linia)
    res, aux = reduir(res)
    while aux:
        res, aux = reduir(res)
        #print(res)
print(res)
print(calculaMagintud(ast.literal_eval(res)))
'''

maxim = 0
combinacions = combinations(lines, 2)
for x,y in combinacions:
    x = x[:len(x) - 1]
    y = y[:len(y) - 1]

    res = suma(x, y)
    res, aux = reduir(res)
    while aux:
        res, aux = reduir(res)
    val = calculaMagintud(ast.literal_eval(res))
    if(val > maxim):
        maxim = val
    res = suma(y, x)
    res, aux = reduir(res)
    while aux:
        res, aux = reduir(res)
    val = calculaMagintud(ast.literal_eval(res))
    if (val > maxim):
        maxim = val
print(maxim)