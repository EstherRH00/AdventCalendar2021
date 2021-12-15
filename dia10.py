f = open('input','r')
lines = f.readlines()
f.close()

punts = {")": 3, "]": 57, "}": 1197, ">" : 25137}
puntsCompletar = {"(": 1, "[": 2, "{": 3, "<" : 4}
correcte =  {")": "(", "]": "[", "}": "{", ">" : "<"}

contador = 0
valorsCompletar = []

for linia in lines:
    pila = []
    i = 0
    fi = False
    while(i < len(linia) and not fi):
        caracter = linia[i]
        #print(caracter)
        #Si es obertura el poso
        if(caracter in correcte.values()):
            pila.append(caracter)
        elif(caracter != '\n'):
            parella = pila.pop()
            if(correcte[caracter] != parella):
                #print("expected", parella,", but found", caracter)
                fi = True
                contador += punts[caracter]
        i+=1

    if (len(pila) != 0 and not fi):
        #print(pila)
        valorCompletar = 0
        while(len(pila)):
            aux = pila.pop()
            valorCompletar = (valorCompletar * 5) + puntsCompletar[aux]
            #print(valorCompletar)
        valorsCompletar.append(valorCompletar)
        #print(valorsCompletar)

valorsCompletar.sort()
print(valorsCompletar[len(valorsCompletar)//2])