f = open('input','r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")

llarg = lines[:]
curt = lines[:]
for i in range(len(lines)):
    llarg[i] = lines[i][:len(lines[i])-5]
    curt[i] = lines[i][len(lines[i])-4:]
    curt[i][3] = curt[i][3][:len(curt[i][3])-1]

cont = 0
for linia in curt:
    #print(linia)
    for num in linia:
        if(len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7):
            cont+=1
    #print(cont)
print(cont)

suma = 0
for k in range(len(llarg)):
    linia = llarg[k]
    sumar = 0
    dicc = {}
    linia.sort(key = len)
    print("linia", linia)
    #Aconsegueixo la A
    for lletra in linia[1]:
        if lletra not in linia[0]:
            dicc['a'] = lletra

    #candidats a b i d
    auxBD = []
    for lletra in linia[2]:
        if lletra not in linia[0]:
            auxBD.append(lletra)
    #Trobo la g, b i d
    for lletra in linia[3]:
        if lletra in linia[4] and lletra in linia[5] and lletra!= dicc['a']:
            if lletra in auxBD:
                dicc['d'] = lletra
                auxBD.remove(lletra)
                dicc['b'] = auxBD[0]
            else:
                dicc['g'] = lletra
    # candidats a c i f
    auxCF = [linia[0][0], linia[0][1]]

    #Trobo la c i la f
    for lletra in linia[6]:
        if lletra in linia[7] and lletra in linia[8]:
            if lletra in auxCF:

                dicc['f'] = lletra
                auxCF.remove(lletra)
                dicc['c'] = auxCF[0]
    for lletra in linia[9]:
        if lletra not in dicc.values():
            dicc['e'] = lletra

    #print(dicc)

    for numero in curt[k]:
        sumar = sumar*10
        if len(numero) == 2:
            sumar+=1
        elif len(numero) == 3:
            sumar+= 7
        elif len(numero) == 4:
            sumar += 4
        elif len(numero) == 5:
            if dicc['e'] in numero:
                sumar += 2
            elif dicc['b'] in numero:
                sumar += 5
            else:
                sumar += 3
        elif len(numero) == 6:
            if dicc['c'] in numero:
                if dicc['d'] in numero:
                    sumar += 9
            else: sumar += 6
        else: sumar += 8

    print("sumo", sumar)
    suma += sumar
print(suma)